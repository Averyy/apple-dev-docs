# LightmapResource.BakeType

**Framework**: RealityKit  
**Kind**: enum  
**Role**: Enumeration

Specifies the type of data contained within a lightmap.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum BakeType
```

## Topics

### Specifying the bake type
- [LightmapResource.BakeType.finalShadedColor](./baketype/finalshadedcolor.md)
  Lightmaps with this type contain the final shaded color. No runtime shading calculations are performed for objects using this type of lightmap.
- [LightmapResource.BakeType.indirectDiffuseIrradiance](./baketype/indirectdiffuseirradiance.md)
- [LightmapResource.BakeType.ambientOcclusion](./baketype/ambientocclusion.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lightmapresource/baketype)*