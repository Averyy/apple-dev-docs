# LightmapResource.BakeDescriptor

**Framework**: RealityKit  
**Kind**: enum

Specifies parameters necessary to fetch a particular type of light map data for a given instance of a given mesh part.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum BakeDescriptor
```

## Topics

### Specifying the bake type
- [case finalShadedColor(LightmapResource.FinalShadedColorBakeDescriptor)](lightmapresource/bakedescriptor/finalshadedcolor(_:).md)
- [case indirectDiffuseIrradiance(LightmapResource.IndirectDiffuseIrradianceBakeDescriptor)](lightmapresource/bakedescriptor/indirectdiffuseirradiance(_:).md)
- [case indirectDiffuseSHL1Irradiance(LightmapResource.IndirectDiffuseIrradianceSHBakeDescriptor)](lightmapresource/bakedescriptor/indirectdiffuseshl1irradiance(_:).md)
- [case ambientOcclusion(LightmapResource.AmbientOcclusionBakeDescriptor)](lightmapresource/bakedescriptor/ambientocclusion(_:).md)
- [var bakeType: LightmapResource.BakeType](lightmapresource/bakedescriptor/baketype.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [LightmapResource.FinalShadedColorBakeDescriptor](lightmapresource/finalshadedcolorbakedescriptor.md)
- [LightmapResource.AmbientOcclusionBakeDescriptor](lightmapresource/ambientocclusionbakedescriptor.md)
- [LightmapResource.IndirectDiffuseIrradianceBakeDescriptor](lightmapresource/indirectdiffuseirradiancebakedescriptor.md)
- [LightmapResource.IndirectDiffuseIrradianceSHBakeDescriptor](lightmapresource/indirectdiffuseirradianceshbakedescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lightmapresource/bakedescriptor)*