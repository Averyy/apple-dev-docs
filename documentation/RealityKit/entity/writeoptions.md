# Entity.WriteOptions

**Framework**: RealityKit  
**Kind**: struct

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

Use [`Entity.WriteOptions`](entity/writeoptions.md) to tune the tradeoff between export speed, file size, and runtime cost when you save a scene to a `.reality` file.

Pass a value of this type to [`write(to:options:)`](entity/write(to:options:).md) or [`write(to:options:)`](entity/configurationcatalog/write(to:options:).md) as an array literal containing one or more option values.

```swift
let combinedOptions: Entity.WriteOptions = [
    .preferFastExport,
    .preferSmallTextureFiles(quality: .standard)
]
```

#### Expediting Reality File Exports

The [`preferFastExport`](entity/writeoptions/preferfastexport.md) reduces the time required to write a reality file but produces a larger file on disk.

#### Reducing Texture File Size

The [`preferSmallTextureFiles(quality:)`](entity/writeoptions/prefersmalltexturefiles(quality:).md) method returns options that instruct RealityKit to encode textures using smaller file representations,  at the cost of longer load times and higher memory usage. Specify a [`Entity.WriteOptions.TextureQuality`](entity/writeoptions/texturequality.md) level to control the tradeoff between visual fidelity and file size.

## Topics

### Configuring export options
- [static var preferFastExport: Entity.WriteOptions](entity/writeoptions/preferfastexport.md)
  Expedite the reality file export when possible.
- [static func preferSmallTextureFiles(quality: Entity.WriteOptions.TextureQuality) -> Entity.WriteOptions](entity/writeoptions/prefersmalltexturefiles(quality:).md)
  Reduce textures’ file size while preserving its dimensions.
- [Entity.WriteOptions.TextureQuality](entity/writeoptions/texturequality.md)
  A texture quality level.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func write(to: URL, options: Entity.WriteOptions) async throws](entity/write(to:options:).md)
- [static func write([Entity], to: URL, options: Entity.WriteOptions) async throws](entity/write(_:to:options:).md)
  Exports an array of entities as separate scenes within a single RealityKit file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/writeoptions)*