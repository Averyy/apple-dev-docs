# init(cube:options:)

**Framework**: Realitykit  
**Kind**: init

Asynchronously creates an environment resource from a cube texture.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency convenience init(cube cubeTexture: TextureResource, options: EnvironmentResource.CreateOptions) async throws
```

#### Discussion

RealityKit generates an environment resource from a skybox cube texture of the environment. The created environment shares the input skybox.

> **Note**: [`EnvironmentResource.CreateOptions.SamplingQuality.high`](environmentresource/createoptions/samplingquality-swift.enum/high.md) and [`EnvironmentResource.CreateOptions.SamplingQuality.veryHigh`](environmentresource/createoptions/samplingquality-swift.enum/veryhigh.md), along with [`astc(blockSize:quality:)`](textureresource/compression/astc(blocksize:quality:).md) compression options, are only available in macOS. Use these options to write optimized scenes for all target platforms when exporting from macOS with [`write(to:)`](entity/write(to:).md). Compression options also significantly reduce an environmental resource’s memory and disk usage.

```swift
// Use compression and high quality options to export optimized resources.
let cube = try TextureResource(
    cubeFromEquirectangular: image,
    quality: .high,
    options: TextureResource.CreateOptions(semantic: .color)
)

let options = EnvironmentResource.CreateOptions(
    samplingQuality: .high,
    specularCubeDimension: cube.width/2,
    compression: .astc(blockSize: .block4x4, quality: .high)
)

let environment = try EnvironmentResource(
    cube: cube,
    options: EnvironmentResource.CreateOptions(
        samplingQuality: .high,
        specularCubeDimension: cube.width/2,
        compression: .astc(blockSize: .block4x4, quality: .high)
    )
)

let lightEntity = Entity()
lightEntity.components.set(ImageBasedLightComponent(
    source: .single(environment)
))
...
```

> **Note**: If you request `.astc` compression and `cubeTexture` isn’t already compressed, RealityKit compresses it.

## Parameters

- `cubeTexture`: A skybox cube texture of type   with   or   semantics.
- `options`: A configuration for generating the environment resource.

## See Also

- [convenience init(named: String, in: Bundle?) async throws](environmentresource/init(named:in:).md)
  Asynchronously loads an environment resource from a bundle.
- [convenience init(equirectangular: CGImage, withName: String?) throws](environmentresource/init(equirectangular:withname:)-9g602.md)
  Synchronously creates an environment resource from an equirectangular image.
- [convenience init(equirectangular: CGImage, withName: String?) async throws](environmentresource/init(equirectangular:withname:)-3xxrz.md)
  Asynchronously generates an environment resource from an equirectangular image.
- [convenience init(cube: TextureResource, options: EnvironmentResource.CreateOptions) throws](environmentresource/init(cube:options:)-4knhi.md)
  Synchronously generates an environment resource from a cube texture resource.
- [static func load(named: String, in: Bundle?) throws -> EnvironmentResource](environmentresource/load(named:in:).md)
  Synchronously loads an environment resource from a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentresource/init(cube:options:)-4xqiz)*