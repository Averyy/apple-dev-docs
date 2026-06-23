# LightmapResource.BakeType

**Framework**: RealityKit  
**Kind**: enum

Specifies the type of data contained within a lightmap.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum BakeType
```

## Topics

### Specifying the bake type
- [LightmapResource.BakeType.finalShadedColor](lightmapresource/baketype/finalshadedcolor.md)
  Lightmaps with this type contain the final shaded color. No runtime shading calculations are performed for objects using this type of lightmap.
- [LightmapResource.BakeType.indirectDiffuseIrradiance](lightmapresource/baketype/indirectdiffuseirradiance.md)
- [LightmapResource.BakeType.indirectDiffuseSHL1Irradiance](lightmapresource/baketype/indirectdiffuseshl1irradiance.md)
- [LightmapResource.BakeType.ambientOcclusion](lightmapresource/baketype/ambientocclusion.md)

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var bakeTypes: [LightmapResource.BakeType]](lightmapresource/baketypes.md)
  All bake types used by entities in this lightmap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lightmapresource/baketype)*