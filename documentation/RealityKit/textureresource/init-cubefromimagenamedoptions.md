# init(cubeFromImage:named:options:)

**Framework**: RealityKit  
**Kind**: init

Asynchronously creates a cube texture resource from a 2D image of cube faces.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(cubeFromImage cgImage: CGImage, named resourceName: String? = nil, options: TextureResource.CreateOptions) async throws
```

#### Discussion

RealityKit extracts the cube faces from the source 2D image using a convention based on its aspect ratio, which needs to be one of the following:

- If `height == 6 * width`, RealityKit treats the source image as a vertical strip of the cube faces, containing [+X, -X, +Y, -Y, +Z, -Z]  from top to bottom:

![A cube source image showing the expected cube face’s orientation for a vertical strip](https://docs-assets.developer.apple.com/published/f291c9574e4130d8540555b0f321ac86/textureresource-cube-vstrip-orientation.jpg)

- If `6 * height == width`, RealityKit treats the source image as a horizontal strip of the cube faces, containing [+X, -X, +Y, -Y, +Z, -Z] from left to right:

![A cube source image showing the expected cube face’s orientation for a vertical strip](https://docs-assets.developer.apple.com/published/3010520f97600c24a2a1cadf5ccf84ed/textureresource-cube-hstrip-orientation.jpg)

- If `height / 3 == width / 4`, RealityKit treats the source image as a cross layout of the cube faces as follows:

```None
    [+Y]
[+X][-Z][-X][+Z]
    [-Y]
```

![A cube source image showing the expected cube face’s orientation and layout for a cross](https://docs-assets.developer.apple.com/published/50894b5906edd417d6b7e3467625f5b6/textureresource-cube-cross-orientation.jpg)

Use the resulting texture to create an [`EnvironmentResource`](environmentresource.md), or assign it to a material in Reality Composer Pro that requires a cube texture type.

```swift
if let source = CGImageSourceCreateWithURL(url as CFURL, nil),
    let image = CGImageSourceCreateImageAtIndex(source, 0, nil) {

    // Create a cube texture from the image.
    let cube = try await TextureResource(
        cubeFromImage: image, options: TextureResource.CreateOptions(semantic: .hdrColor))

    // Create an environment resource from the cube texture.
    let environment = try await EnvironmentResource(
        cube: cube, options: EnvironmentResource.CreateOptions())

    await MainActor.run {
        // Assign the environment to an image-based light component.
        let lightEntity = Entity()
        lightEntity.components.set(
            ImageBasedLightComponent(source: .single(environment)))
        ...
    }
}
```

## Parameters

- `cgImage`: The source image.
- `resourceName`: A unique name for syncing the texture resource across the network.   The name is empty if you don’t include one.
- `options`: A configuration for generating the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/init(cubefromimage:named:options:))*