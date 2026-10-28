# init(cube:options:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Synchronously generates an environment resource from a cube texture resource.

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
@preconcurrency convenience init(cube cubeTexture: TextureResource, options: EnvironmentResource.CreateOptions) throws
```

**Other overloads**:

```swift
@MainActor
@preconcurrency convenience init(cube cubeTexture: TextureResource, options: EnvironmentResource.CreateOptions) async throws
```

## Discussion

Loading an [`EnvironmentResource`](../environmentresource.md) with this method blocks the main actor because it’s synchronous, so only call it from a command-line application. The method can stall a regular app, which makes it visibly hitch, and the system terminates an app if its UI becomes unresponsive.

RealityKit generates an environment resource from a skybox cube texture of the environment. The created environment shares the input skybox.

See `init(cube:options:)-4xqiz` for more details.

```swift
// Use compression and high quality options to export optimized resources.
let cube = try await TextureResource(
    cubeFromEquirectangular: image,
    quality: .high,
    options: TextureResource.CreateOptions(semantic: .hdrColor)
)

let options = EnvironmentResource.CreateOptions(
    samplingQuality: .high,
    specularCubeDimension: cube.width/2,
    compression: .astc(blockSize: .block4x4, quality: .high)
)

// Create an environment resource from the cube texture.
let environment = try await EnvironmentResource(
    cube: cube, options: EnvironmentResource.CreateOptions(
            samplingQuality: .high,
            specularCubeDimension: cube.width/2,
            compression: .astc(blockSize: .block4x4, quality: .high)
    )
)

await MainActor.run {
    // Assign the environment to an image-based light component.
    let lightEntity = Entity()
    lightEntity.components.set(ImageBasedLightComponent(
        source: .single(environment)
    ))
    ...
}
```

> **Note**: If you request `.astc` compression and `cubeTexture` isn’t already compressed, RealityKit compresses it.

## Parameters

- `cubeTexture`: A skybox cube texture of type `.cubeType` and `.color` or `.hdrColor` semantics.
- `options`: A configuration for generating the environment resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/init(cube:options:)-5e5gr)*