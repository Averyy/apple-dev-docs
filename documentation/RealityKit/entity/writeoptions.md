# Entity.WriteOptions

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A set of options that control how RealityKit writes entities to a reality file.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct WriteOptions
```

#### Overview

Use [`Entity.WriteOptions`](./writeoptions.md) to tune the tradeoff between export speed, file size, and runtime cost when you save a scene to a `.reality` file.

Pass a value of this type to [`write(to:options:)`](./write%28to,options%29.md) or [`write(to:options:)`](./configurationcatalog/write%28to,options%29.md) as an array literal containing one or more option values.

```swift
let combinedOptions: Entity.WriteOptions = [
    .preferFastExport,
    .preferSmallTextureFiles(quality: .standard)
]
```

#### Expediting Reality File Exports

The [`preferFastExport`](./writeoptions/preferfastexport.md) reduces the time required to write a reality file but produces a larger file on disk.

#### Reducing Texture File Size

The [`preferSmallTextureFiles(quality:)`](./writeoptions/prefersmalltexturefiles%28quality%29.md) method returns options that instruct RealityKit to encode textures using smaller file representations,  at the cost of longer load times and higher memory usage. Specify a [`Entity.WriteOptions.TextureQuality`](./writeoptions/texturequality.md) level to control the tradeoff between visual fidelity and file size.

## Topics

### Configuring export options
- [static var preferFastExport: Entity.WriteOptions](./writeoptions/preferfastexport.md)
  Expedite the reality file export when possible.
- [static func preferSmallTextureFiles(quality: Entity.WriteOptions.TextureQuality) -> Entity.WriteOptions](./writeoptions/prefersmalltexturefiles%28quality%29.md)
  Reduce textures’ file size while preserving its dimensions.
- [Entity.WriteOptions.TextureQuality](./writeoptions/texturequality.md)
  A texture quality level.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Writing an entity to a file
- [func write(to: URL, options: Entity.WriteOptions) async throws](./write%28to,options%29.md)
- [static func write([Entity], to: URL, options: Entity.WriteOptions) async throws](./write%28_,to,options%29.md)
  Exports an array of entities as separate scenes within a single RealityKit file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/writeoptions)*