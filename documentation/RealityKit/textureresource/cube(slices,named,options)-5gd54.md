# cube(slices:named:options:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Type Method

Synchronously creates a cube texture resource from face images.

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
@preconcurrency static func cube(slices: [CGImage], named resourceName: String? = nil, options: TextureResource.CreateOptions) throws -> TextureResource
```

**Other overloads**:

```swift
@MainActor
@preconcurrency static func cube(slices: [CGImage], named resourceName: String? = nil, options: TextureResource.CreateOptions) async throws -> TextureResource
```

## Discussion

Provide the cube faces in the following order: [`+X`, `-X`, `+Y`, `-Y`, `+Z`, `-Z`]. See `cube(slices:named:options:)-57yj1` for more details.

Loading a [`TextureResource`](../textureresource.md) with this method blocks the main actor because it’s synchronous, so only call it from a command-line application. The method can stall a regular app, which makes it visibly hitch, and the system terminates an app if its UI becomes unresponsive. See [`init(named:in:)`](./init%28named,in%29.md) for an example that demonstrates how to safely load content.

```swift
// Create a cube texture from image slices.
let cube = try TextureResource.cube(
    slices: [posXImage, negXImage, posYImage, negYImage, posZImage, negZImage],
    options: TextureResource.CreateOptions(semantic: .hdrColor)
)

// Create an environment resource from the cube texture.
let environment = try EnvironmentResource(
    cube: cube,
    options: EnvironmentResource.CreateOptions()
)

// Assign the environment to an image-based light component.
let lightEntity = Entity()
lightEntity.components.set(ImageBasedLightComponent(source: .single(environment)))
...
```

## Parameters

- `slices`: The source images for each cube face in [`+X`, `-X`, `+Y`, `-Y`, `+Z`, `-Z`] order. All images need to be square, and of equal size and format.
- `resourceName`: A unique name for syncing the texture resource across the network. The name is empty if you don’t include one.
- `options`: A configuration for generating the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/cube(slices:named:options:)-5gd54)*