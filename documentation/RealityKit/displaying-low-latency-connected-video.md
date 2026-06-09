# Displaying low-latency connected video

**Framework**: RealityKit

Render connected camera feeds in visionOS with minimal latency.

**Availability**:
- visionOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

#### Overview

Your visionOS app can access video from USB Video Class (UVC) devices connected with the Developer Strap for Apple Vision Pro. You can use [`AVFoundation`](https://developer.apple.com/documentation/AVFoundation) to capture and display connected camera feeds, as demonstrated in [`Displaying video from connected devices`](https://developer.apple.com/documentation/visionOS/displaying-video-from-connected-devices). Although this sample captures from a UVC device, you can apply the same low-latency rendering technique to video frames from other sources, such as a wireless camera stream.

This sample code shows you how to combine AVFoundation with additional frameworks to render connected video with lower latency and support for stereoscopic cameras:

- **[`Core Image`](https://developer.apple.com/documentation/CoreImage)**: Converts camera pixel buffers into Metal textures.
- **[`Metal`](https://developer.apple.com/documentation/Metal)**: Provides GPU-private shared textures that avoid data copies.
- **[`RealityKit`](RealityKit.md)**: Displays textures in your scene using low-level textures and device resources.
- **[`ShaderGraph`](https://developer.apple.com/documentation/ShaderGraph)**: Combines left and right eye textures into a single material for stereoscopic display.

This article uses [`LowLevelTexture`](lowleveltexture.md) and [`LowLevelDeviceResource`](lowleveldeviceresource.md) resources, which improve rendering latency for camera feeds. The technique works for both mono and stereo camera images.

> **Note**: Displaying low-latency connected camera feeds is not supported in the simulator.

#### Review the Rendering Pipeline

The low-latency rendering pipeline consists of four main components:

- **`CameraCoordinator`**: Receives camera frames from the capture session.
- **`LowLatencyRenderer`**: Converts pixel buffers to Metal textures using Core Image.
- **`CameraFeedSharedTexture`**: Manages shared textures between Metal and RealityKit.
- **`Entity+CameraFeed`**: Creates entities that display camera feed textures.

This architecture minimizes latency by using shared texture handles to avoid copying data between Metal and RealityKit. It renders directly to GPU-private memory and signals frame updates efficiently through device resource replacement.

#### Create Shared Textures for Low Latency Rendering

Create a `CameraFeedSharedTexture` class that manages the low-level textures and their associated device resources. This class bridges Metal and RealityKit by creating shared texture handles that both frameworks can access.

```swift
enum TextureConfiguration {
    case mono(TextureSet)
    case stereo(left: TextureSet, right: TextureSet)

    struct TextureSet {
        let metalTexture: MTLTexture
        let lowLevelTexture: LowLevelTexture
        let textureResource: TextureResource
        let deviceResourceFirst: LowLevelDeviceResource
        let deviceResourceSecond: LowLevelDeviceResource
    }
}

@MainActor
final class CameraFeedSharedTexture {
    private(set) var configuration: TextureConfiguration
    ...

    init(width: Int, height: Int, isStereo: Bool) throws {
        // Get a Metal device.
        guard let device = MTLCreateSystemDefaultDevice() else {
            throw SharedTextureError.metalDeviceNotAvailable
        }

        if isStereo {
            // Create textures for the left and right eyes.
            let leftSet = try Self.createTextureSet(
                width: width,
                height: height,
                device: device
            )

            let rightSet = try Self.createTextureSet(
                width: width,
                height: height,
                device: device
            )

            self.configuration = .stereo(left: leftSet, right: rightSet)
        } else {
            // Create the mono texture.
            let monoSet = try Self.createTextureSet(
                width: width,
                height: height,
                device: device
            )

            self.configuration = .mono(monoSet)
        }
    }

    private static func createTextureSet(
        width: Int,
        height: Int,
        device: MTLDevice
    ) throws -> TextureConfiguration.TextureSet {
        let (metalTexture, lowLevelTexture, deviceRes1, deviceRes2) = try createSharedTexture(
            width: width,
            height: height,
            device: device
        )

        let textureResource = try TextureResource(from: lowLevelTexture)

        return TextureConfiguration.TextureSet(
            metalTexture: metalTexture,
            lowLevelTexture: lowLevelTexture,
            textureResource: textureResource,
            deviceResourceFirst: deviceRes1,
            deviceResourceSecond: deviceRes2
        )
    }
}
```

The `TextureConfiguration` enumeration stores either a single texture set for mono cameras or separate left and right texture sets for stereo cameras. Each texture set contains a Metal texture for rendering and a RealityKit low-level texture for display. Each texture set also includes two device resources that signal updates.

#### Initialize Low Level Textures with Shared Texture Handles

Create a method to initialize the [`LowLevelTexture`](lowleveltexture.md) using a shared Metal texture handle. This allows both Metal (for rendering) and RealityKit (for display) to access the same texture memory without copying data.

```swift
private static func createSharedTexture(
    width: Int,
    height: Int,
    device: MTLDevice
) throws -> (MTLTexture, LowLevelTexture, LowLevelDeviceResource, LowLevelDeviceResource) {
    #if targetEnvironment(simulator)
    // Do not use shared-texture APIs on the visionOS Simulator, they are not available.
    throw SharedTextureError.notSupportedOnSimulator
    #else
    // Create an `MTLTextureDescriptor` with the correct pixel format.
    let metalTextureDescriptor = MTLTextureDescriptor()
    metalTextureDescriptor.width = width
    metalTextureDescriptor.height = height
    metalTextureDescriptor.pixelFormat = .bgra8Unorm_srgb
    metalTextureDescriptor.mipmapLevelCount = 1
    metalTextureDescriptor.storageMode = .private
    metalTextureDescriptor.usage = [.shaderRead, .shaderWrite, .pixelFormatView]

    // Create the shared `MTLTexture` using the `MTLTextureDescriptor`, created above.
    guard let sharedMetalTexture = device.makeSharedTexture(descriptor: metalTextureDescriptor) else {
        throw SharedTextureError.sharedTextureCreationFailed
    }

    // Create a `LowLevelTexture` with a matching descriptor.
    let lowLevelTextureDescriptor = LowLevelTexture.Descriptor(
        pixelFormat: .bgra8Unorm_srgb,
        width: width,
        height: height,
        depth: 1,
        mipmapLevelCount: 1,
        textureUsage: [.shaderRead, .shaderWrite, .pixelFormatView]
    )
    let lowLevelTexture = try LowLevelTexture(descriptor: lowLevelTextureDescriptor)

    // Get the shared texture handle from the shared Metal texture.
    guard let sharedTextureHandle = sharedMetalTexture.makeSharedTextureHandle() else {
        throw SharedTextureError.sharedTextureHandleCreationFailed
    }

    // Replace the device resource of the `LowLevelTexture` with a shared texture handle.
    let deviceResource1 = try LowLevelDeviceResource(sharedTextureHandle: sharedTextureHandle)
    let deviceResource2 = try LowLevelDeviceResource(sharedTextureHandle: sharedTextureHandle)

    lowLevelTexture.replace(deviceResource: deviceResource1)

    return (sharedMetalTexture, lowLevelTexture, deviceResource1, deviceResource2)
    #endif
}
```

The `createSharedTexture` method:

- Creates matching [`MTLTexture`](https://developer.apple.com/documentation/Metal/MTLTexture) and [`LowLevelTexture`](lowleveltexture.md) objects with identical pixel formats and dimensions. The storage mode must be [`MTLStorageMode.private`](https://developer.apple.com/documentation/Metal/MTLStorageMode/private) to create shared textures that reside entirely in GPU memory.
- Creates two separate device resource instances from the same shared texture handle. You use these to signal frame updates to RealityKit.

#### Signal Frame Updates By Toggling Device Resources

Create a method that alternates between two device resources on each frame. This signals to RealityKit that the texture content has changed and needs redrawing:

```swift
func replaceTexture() {
    frameCount += 1

    // Alternate between two distinct LowLevelDeviceResource instances each frame to tell
    // RealityKit that the texture content has changed, causing it to re-read and
    // display the latest camera frame. Both resources reference the same shared
    // texture handle and therefore the same underlying GPU memory, but `RealityKit`
    // treats a `replace(deviceResource:)` call with the same instance as a no-op.
    let useFirstResource = frameCount % 2 == 0

    switch configuration {
    case .mono(let textureSet):
        if useFirstResource {
            textureSet.lowLevelTexture.replace(deviceResource: textureSet.deviceResourceFirst)
        } else {
            textureSet.lowLevelTexture.replace(deviceResource: textureSet.deviceResourceSecond)
        }
    case .stereo(let left, let right):
        if useFirstResource {
            left.lowLevelTexture.replace(deviceResource: left.deviceResourceFirst)
            right.lowLevelTexture.replace(deviceResource: right.deviceResourceFirst)
        } else {
            left.lowLevelTexture.replace(deviceResource: left.deviceResourceSecond)
            right.lowLevelTexture.replace(deviceResource: right.deviceResourceSecond)
        }
    }
}
```

RealityKit updates the display each time you call `replace(deviceResource:)`, even though both device resources point to the same underlying shared texture. This mechanism ensures frame-accurate updates without copying texture data. Call this method before rendering each new camera frame.

#### Create an Entity to Display Camera Textures

Create [`Entity`](entity.md) factory methods that build camera feed entities for your scene. For mono cameras, use [`UnlitMaterial`](unlitmaterial.md) with a single texture. For stereo cameras, use [`ShaderGraphMaterial`](shadergraphmaterial.md) that combines left and right eye textures:

```swift
extension Entity {
    static func makeCameraFeed(
        texture: TextureResource,
        width: Float,
        height: Float
    ) -> Entity {
        var material = UnlitMaterial()
        material.color = .init(texture: .init(texture))

        let entity = Entity()
        entity.components.set(
            ModelComponent(
                mesh: .generatePlane(width: width, height: height),
                materials: [material]
            )
        )
        return entity
    }

    static func makeStereoCameraFeed(
        leftEyeTexture: LowLevelTexture,
        rightEyeTexture: LowLevelTexture,
        width: Float,
        height: Float,
        material: ShaderGraphMaterial
    ) async -> Entity {
        var material = material
        do {
            try await material.setParameter(
                name: "leftEye",
                value: .textureResource(TextureResource(from: leftEyeTexture))
            )
            try await material.setParameter(
                name: "rightEye",
                value: .textureResource(TextureResource(from: rightEyeTexture))
            )
        } catch {
            Self.logger.error("Failed to set material parameters: \(error.localizedDescription)")
        }

        let entity = Entity()
        entity.components.set(
            ModelComponent(
                mesh: .generatePlane(width: width, height: height),
                materials: [material]
            )
        )
        return entity
    }
}
```

The `makeCameraFeed(texture:width:height:)` method creates a plane with an unlit material displaying the camera texture. The `makeStereoCameraFeed(leftEyeTexture:rightEyeTexture:width:height:material:)` method assigns separate textures to a shader graph material’s left and right eye parameters. This enables proper stereo presentation in visionOS. To learn how the app uses [`ShaderGraphMaterial`](shadergraphmaterial.md) to render stereo images, see [`Displaying a stereoscopic image`](https://developer.apple.com/documentation/visionOS/displaying-a-stereoscopic-image-in-visionos).

#### Add the Camera Feed Entity to Your Scene

Create a [`RealityView`](realityview.md) that reads the shared texture from the renderer, builds the appropriate camera feed entity, and adds it to the scene:

```swift
RealityView { content in
    guard let renderer = appModel.renderer else { return }

    guard let cameraFeedSharedTexture = renderer.cameraFeedSharedTexture else {
        logger.warning("No camera feed texture available")
        return
    }

    // Calculate the plane dimensions based on its aspect ratio.
    let textureWidth = appModel.isStereo ? appModel.textureWidth / 2 : appModel.textureWidth
    let heightToWidthRatio = Float(textureWidth) / Float(appModel.textureHeight)
    let texturePlaneWidth = texturePlaneHeight * heightToWidthRatio

    let cameraFeedEntity: Entity

    switch cameraFeedSharedTexture.configuration {
    case .mono(let textureSet):
        cameraFeedEntity = Entity.makeCameraFeed(
            texture: textureSet.textureResource,
            width: texturePlaneWidth,
            height: texturePlaneHeight
        )

    case .stereo(let left, let right):
        guard let material = appModel.stereoMaterial else {
            return
        }

        cameraFeedEntity = await Entity.makeStereoCameraFeed(
            leftEyeTexture: left.lowLevelTexture,
            rightEyeTexture: right.lowLevelTexture,
            width: texturePlaneWidth,
            height: texturePlaneHeight,
            material: material
        )
    }

    content.add(cameraFeedEntity)
}
```

The code calculates plane dimensions based on the camera’s aspect ratio. For stereo cameras, it divides the texture width by two because the camera provides side-by-side stereo images in a single buffer. The code then calls the appropriate factory method to create either a mono or stereo entity depending on the texture configuration.

#### Render Pixel Buffers to Textures

Use Core Image to convert incoming [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/cvpixelbuffer-q2e) frames to Metal textures. Create a Metal command buffer and use [`CIRenderDestination`](https://developer.apple.com/documentation/CoreImage/CIRenderDestination) to render directly to the shared texture.

```swift
func renderWithCoreImage(
    imageBuffer: CVPixelBuffer,
    isStereo: Bool
) {
    guard let commandBuffer = commandQueue.makeCommandBuffer() else {
        logger.error("Unable to create command buffer.")
        return
    }

    defer {
       commandBuffer.commit()
    }

    guard let textureLeft = cameraFeedSharedTexture?.metalTextureLeft else {
        logger.error("No texture available")
        return
    }

    // Signal `RealityKit` that new frame data is available.
    cameraFeedSharedTexture?.replaceTexture()

    let ciImage = CIImage(cvPixelBuffer: imageBuffer)

    do {
        if isStereo {
            guard let textureRight = cameraFeedSharedTexture?.metalTextureRight else {
                logger.error("No right stereo texture available")
                return
            }

            // Split the side-by-side stereo image.
            let fullWidth = ciImage.extent.width
            let halfWidth = fullWidth / 2
            let height = ciImage.extent.height

            let leftImage = ciImage.cropped(to: CGRect(x: 0, y: 0, width: halfWidth, height: height))
            let rightImage = ciImage
                .cropped(to: CGRect(x: halfWidth, y: 0, width: halfWidth, height: height))
                .transformed(by: CGAffineTransform(translationX: -halfWidth, y: 0))

            try renderImage(leftImage, to: textureLeft, using: ciContext, commandBuffer: commandBuffer, colorSpace: colorSpace)
            try renderImage(rightImage, to: textureRight, using: ciContext, commandBuffer: commandBuffer, colorSpace: colorSpace)

        } else {
            try renderImage(ciImage, to: textureLeft, using: ciContext, commandBuffer: commandBuffer, colorSpace: colorSpace)
        }
    } catch {
        logger.error("Render failed: \(error.localizedDescription)")
    }
}

private func renderImage(
    _ image: CIImage,
    to texture: MTLTexture,
    using context: CIContext,
    commandBuffer: MTLCommandBuffer,
    colorSpace: CGColorSpace
) throws {
    let destination = CIRenderDestination(
        width: Int(texture.width),
        height: Int(texture.height),
        pixelFormat: texture.pixelFormat,
        commandBuffer: commandBuffer,
        mtlTextureProvider: { texture }
    )
    destination.isFlipped = true
    destination.colorSpace = colorSpace

    _ = try context.startTask(toRender: image, to: destination)
}
```

Core Image handles color space conversion automatically, transforming YCbCr camera data to RGB for display. For stereo cameras, the code crops the side-by-side stereo image into separate left and right images before rendering each to its respective texture. The `replaceTexture()` call toggles the device resource before rendering, ensuring RealityKit detects the new frame.

#### Process Camera Frames From the Capture Session

Extract the pixel buffer from each [`CMSampleBuffer`](https://developer.apple.com/documentation/CoreMedia/CMSampleBuffer) you receive from the camera capture session and send it to the renderer:

```swift
private func processFrame(_ sampleBuffer: CMSampleBuffer) {
    guard let imageBuffer = sampleBuffer.imageBuffer else {
        logger.warning("Failed to get image buffer from sample buffer.")
        return
    }

    renderer?.renderWithCoreImage(imageBuffer: imageBuffer, isStereo: isStereo)
}
```

The `CameraCoordinator` receives frames from `CameraCaptureSession` through an asynchronous event stream. It extracts the pixel buffer from each sample buffer and forwards it to the `LowLatencyRenderer`. The renderer updates the shared textures, which RealityKit displays in your scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/displaying-low-latency-connected-video)*