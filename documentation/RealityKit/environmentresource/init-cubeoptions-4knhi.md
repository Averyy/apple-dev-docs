# init(cube:options:)

**Framework**: Realitykit  
**Kind**: init

Synchronously generates an environment resource from a cube texture resource.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(cube cubeTexture: TextureResource, options: EnvironmentResource.CreateOptions) throws
```

#### Discussion

Loading an [`EnvironmentResource`](environmentresource.md) with this method blocks the main actor because it’s synchronous, so only call it from a command-line application. The method can stall a regular app, which makes it visibly hitch, and the system terminates an app if its UI becomes unresponsive.

RealityKit generates an environment resource from a skybox cube texture of the environment. The created environment shares the input skybox.

See [`init(cube:options:)`](environmentresource/init(cube:options:)-4xqiz.md) for more details.

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

- `cubeTexture`: A skybox cube texture of type   and   or   semantics.
- `options`: A configuration for generating the environment resource.

## See Also

- [convenience init(named: String, in: Bundle?) async throws](environmentresource/init(named:in:).md)
  Asynchronously loads an environment resource from a bundle.
- [convenience init(equirectangular: CGImage, withName: String?) throws](environmentresource/init(equirectangular:withname:)-9g602.md)
  Synchronously creates an environment resource from an equirectangular image.
- [convenience init(equirectangular: CGImage, withName: String?) async throws](environmentresource/init(equirectangular:withname:)-3xxrz.md)
  Asynchronously generates an environment resource from an equirectangular image.
- [convenience init(cube: TextureResource, options: EnvironmentResource.CreateOptions) async throws](environmentresource/init(cube:options:)-4xqiz.md)
  Asynchronously creates an environment resource from a cube texture.
- [static func load(named: String, in: Bundle?) throws -> EnvironmentResource](environmentresource/load(named:in:).md)
  Synchronously loads an environment resource from a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/init(cube:options:)-4knhi)*