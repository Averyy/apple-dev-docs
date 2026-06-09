# Entity.WriteOptions

**Framework**: RealityKit  
**Kind**: struct

Options for writing an entity to a RealityKit file.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct WriteOptions
```

## Topics

### Configuring export options
- [static var preferFastExport: Entity.WriteOptions](entity/writeoptions/preferfastexport.md)
  Expedite the reality file export when possible. This may disable reality file compression, resulting in larger file size.
- [static func preferSmallTextureFiles(quality: Entity.WriteOptions.TextureQuality) -> Entity.WriteOptions](entity/writeoptions/prefersmalltexturefiles(quality:).md)
  Reduce textures’ file size.
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
- [Entity.WriteError](entity/writeerror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/writeoptions)*