# LowLevelTexture

**Framework**: RealityKit  
**Kind**: class

A container for texture data allowing you to create and update textures using your own format.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
class LowLevelTexture
```

## Mentions

- [Creating a dynamic height and normal map with low-level texture](creating-a-dynamic-height-map-with-low-level-texture.md)

#### Overview

Use `LowLevelTexture` when you want to bring your own texture data to RealityKit, or update your data frequently. You update the data on the GPU with Metal compute shaders. This is ideal for bringing your own textures to RealityKit as-is, or when you intend to update your data frequently.

> **Note**: For a simpler alternative, consider creating your [`TextureResource`](textureresource.md) from a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) with `TextureResource/init(image:withName:options:)-4qz9s`, `TextureResource/texture2DArray(slices:named:options:)-50g10`, `TextureResource/cube(slices:named:options:)-57yj1`, or `TextureResource/texture3D(slices:named:options:)-6pude`.

Express your texture by creating a [`LowLevelTexture.Descriptor`](lowleveltexture/descriptor-swift.struct.md) that describes how the data is laid out, along with the size of the texture.  This descriptor is similar to [`MTLTextureDescriptor`](https://developer.apple.com/documentation/Metal/MTLTextureDescriptor).

To use `LowLevelTexture`, first configure the descriptor with the desired characteristics of your texture.

```swift
var textureDescriptor: LowLevelTexture.Descriptor {
    var desc = LowLevelTexture.Descriptor()

    desc.textureType = .type2D
    desc.arrayLength = 1

    desc.width = 2048
    desc.height = 2048
    desc.depth = 1

    desc.mipmapLevelCount = 1
    desc.pixelFormat = .bgra8Unorm
    desc.textureUsage = [.shaderRead, .shaderWrite]
    desc.swizzle = .init(red: .red, green: .green, blue: .blue, alpha: .alpha)

    return desc
}
```

Then, you can initialize the `LowLevelTexture` from its descriptor and provide it to a [`TextureResource`](textureresource.md).

```swift
let texture = try LowLevelTexture(descriptor: textureDescriptor)
let resource = try TextureResource(from: texture)
```

You update the contents of a `LowLevelTexture` on the GPU, using a Metal Command Buffer and Compute Command Encoder. For example, you can write a compute kernel in Metal Shading Language to generate the color of each pixel:

```cpp
kernel void
lowLevelTextureKernel(
    texture2d<half, access::write> outTexture [[texture(0)]],
    uint2 gid [[thread_position_in_grid]])
{
    // Compute texture coordinate ranging from 0 to 1 along each axis.
    half2 texCoord {
        half(gid[0]) / (outTexture.get_width() - 1),
        half(gid[1]) / (outTexture.get_height() - 1)
    };

    // Compute the color as a linear gradient from top to bottom.
    half3 color = mix(
        half3 { 0.2, 0.2, 0.8 },
        half3 { 0.7, 0.7, 0.9 },
        texCoord.y);

    // Specify an opacity of 1 if the pixel is within a circle
    // spanning the image bounds.
    half alpha = length(texCoord - 0.5) < 0.5 ? 1.0h : 0.0h;

    // Write the color and opacity to the texture.
    outTexture.write(half4(color, alpha), gid);
}
```

You can use this compute kernel to populate the `LowLevelTexture`:

```swift
func populate(texture: LowLevelTexture, device: MTLDevice) {
    // Set up the Metal command queue and compute command encoder, 
    // or abort if that fails.
    guard let commandQueue = device.makeCommandQueue(),
          let commandBuffer = commandQueue.makeCommandBuffer(),
          let computeEncoder = commandBuffer.makeComputeCommandEncoder() else {
        return
    }

    // Load a Metal compute kernel written in Metal Shading Language, 
    // or abort if that fails.
    guard let library = device.makeDefaultLibrary(),
          let function = library.makeFunction(name: "lowLevelTextureKernel"),
          let computePipelineState = try? device.makeComputePipelineState(function: function) else {
        return
    }

    // Enqueue the Metal command buffer.
    commandBuffer.enqueue()

    // Set up the Metal compute command encoder with the app's compute kernel.
    computeEncoder.setComputePipelineState(computePipelineState)

    // Retrieve a MTLTexture from LowLevelTexture.
    // This texture will be directly consumed by RealityKit's renderer.
    let outTexture: MTLTexture = texture.replace(using: commandBuffer)
    computeEncoder.setTexture(outTexture, index: 0)

    // Disptach the GPU compute work.
    // Note: threadGroupCount and threadGroupSize determined elsewhere.
    computeEncoder.dispatchThreadgroups(
        threadGroupCount,
        threadsPerThreadgroup: threadGroupSize)

    // End the encoding and commit the command buffer.
    // When the command buffer completes, RealityKit automatically applies the changes.
    computeEncoder.endEncoding()
    commandBuffer.commit()
}
```

To finish, add your [`TextureResource`](textureresource.md) to a [`Material`](material.md) and display it on an [`Entity`](entity.md).

```swift
func textureEntity(device: MTLDevice) throws -> Entity {
    // Create the LowLevelTexture and populate it on the GPU.
    let texture = try LowLevelTexture(descriptor: textureDescriptor)
    populate(texture: texture, device: device)

    // Create a TextureResource from the LowLevelTexture.
    let resource = try TextureResource(from: texture)

    // Create a material that uses the texture.
    var material = UnlitMaterial(texture: resource)
    material.opacityThreshold = 0.5

    // Return an entity of a plane which uses the generated texture.
    return ModelEntity(mesh: .generatePlane(width: 1, depth: 1), materials: [material])
}
```

![A screenshot of a circle.  The color of the circle is a linear gradient; the top is light blue and the bottom is close to white.](https://docs-assets.developer.apple.com/published/4e518125eb1798957de0f8855cab1a35/lowleveltexture-circle-unlit.png)

The [`TextureResource`](textureresource.md) retains a reference to the `LowLevelTexture`, and presents changes made to the `LowLevelTexture` when the renderer updates.

## Topics

### Structures
- [LowLevelTexture.Descriptor](lowleveltexture/descriptor-swift.struct.md)
  An object that you use to configure new `LowLevelTexture` objects.
### Initializers
- [init(descriptor: LowLevelTexture.Descriptor) throws](lowleveltexture/init(descriptor:).md)
  Creates a low-level texture from a descriptor.
### Instance Properties
- [let descriptor: LowLevelTexture.Descriptor](lowleveltexture/descriptor-swift.property.md)
  The descriptor that you use to initialize the `LowLevelTexture`.
### Instance Methods
- [func read() -> any MTLTexture](lowleveltexture/read.md)
  Retrieves the current texture for GPU reading.
- [func replace(using: any MTLCommandBuffer) -> any MTLTexture](lowleveltexture/replace(using:).md)
  Retrieves a Metal texture that your app’s shaders can write to when they run on a GPU.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Rendering a windowed game in stereo](rendering-a-windowed-game-in-stereo.md)
  Bring an iOS or iPadOS game to visionOS and enhance it.
- [Creating a dynamic height and normal map with low-level texture](creating-a-dynamic-height-map-with-low-level-texture.md)
  Create a low-level texture and update its pixel data on the GPU to form a dynamic height and normal map.
- [LowLevelTexture.Descriptor](lowleveltexture/descriptor-swift.struct.md)
  An object that you use to configure new `LowLevelTexture` objects.
- [TextureResource.Drawable](textureresource/drawable.md)
  A drawable associated with a drawable queue
- [TextureResource.DrawableQueue](textureresource/drawablequeue-swift.class.md)
  A drawable queue that may be used to update a texture resource dynamically
- [TextureResource.DrawableQueue.Descriptor](textureresource/drawablequeue-swift.class/descriptor.md)
  Describes the texture managed by the drawable queue


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveltexture)*