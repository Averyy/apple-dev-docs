# LightmapResource.BakeDescriptor

**Framework**: RealityKit  
**Kind**: enum

Specifies parameters necessary to fetch a particular type of light map data for a given instance of a given mesh part.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum BakeDescriptor
```

## Topics

### Specifying the bake type
- [case finalShadedColor(LightmapResource.FinalShadedColorBakeDescriptor)](lightmapresource/bakedescriptor/finalshadedcolor(_:).md)
- [case indirectDiffuseIrradiance(LightmapResource.IndirectDiffuseIrradianceBakeDescriptor)](lightmapresource/bakedescriptor/indirectdiffuseirradiance(_:).md)
- [case ambientOcclusion(LightmapResource.AmbientOcclusionBakeDescriptor)](lightmapresource/bakedescriptor/ambientocclusion(_:).md)
- [var bakeType: LightmapResource.BakeType](lightmapresource/bakedescriptor/baketype.md)

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lightmapresource/bakedescriptor)*