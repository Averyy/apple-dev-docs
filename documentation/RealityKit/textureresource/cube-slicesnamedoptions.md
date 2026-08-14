# cube(slices:named:options:)

**Framework**: RealityKit  
**Kind**: method

Asynchronously creates a cube texture resource from face images.

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
@preconcurrency static func cube(slices: [CGImage], named resourceName: String? = nil, options: TextureResource.CreateOptions) async throws -> TextureResource
```

#### Discussion

Provide the cube faces in the following order: [`+X`, `-X`, `+Y`, `-Y`, `+Z`, `-Z`].

| ![An illustration of the +X cube face orientation.](/images/com.apple.RealityKit/textureresource-cube-x-orientation.jpg) | ![An illustration of the -X cube face orientation.](/images/com.apple.RealityKit/textureresource-cube-negx-orientation.jpg) | ![An illustration of the +Y cube face orientation.](/images/com.apple.RealityKit/textureresource-cube-y-orientation.jpg) | ![An illustration of the -Y cube face orientation.](/images/com.apple.RealityKit/textureresource-cube-negy-orientation.jpg) | ![An illustration of the +Z cube face orientation.](/images/com.apple.RealityKit/textureresource-cube-z-orientation.jpg) | ![An illustration of the -Z cube face orientation.](/images/com.apple.RealityKit/textureresource-cube-negz-orientation.jpg) |
| --- | --- | --- | --- | --- | --- |

Use the resulting texture to create an [`EnvironmentResource`](environmentresource.md), or assign it to a material in Reality Composer Pro that requires a cube texture type.

```swift
// Create a cube texture from image slices.
let cube = try await TextureResource.cube(
    slices: [posXImage, negXImage, posYImage, negYImage, posZImage, negZImage],
    options: TextureResource.CreateOptions(semantic: .hdrColor)
)

// Create an environment resource from the cube texture.
let environment = try await EnvironmentResource(
    cube: cube,
    options: EnvironmentResource.CreateOptions()
)

await MainActor.run {
    // Assign the environment to an image-based light component.
    let lightEntity = Entity()
    lightEntity.components.set(ImageBasedLightComponent(
        source: .single(environment)))
    ...
}
```

## Parameters

- `slices`: The source images for each cube face in [`+X`, `-X`, `+Y`, `-Y`, `+Z`, `-Z`] order. All images need to be square, and of equal size.
- `resourceName`: A unique name for syncing the texture resource across the network. The name is empty if you don’t include one.
- `options`: A configuration for generating the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/cube(slices:named:options:))*