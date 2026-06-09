# LightmapComponent

**Framework**: RealityKit  
**Kind**: struct

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct LightmapComponent
```

## Topics

### Creating a lightmap component
- [init(resource: LightmapResource)](lightmapcomponent/init(resource:).md)
- [var lightmap: LightmapResource](lightmapcomponent/lightmap.md)
  The LightmapResource backing this component.
### Mapping entities to the lightmap
- [var entityIndexInLightmapResource: [Entity : LightmapComponent.EntityIndex]](lightmapcomponent/entityindexinlightmapresource.md)
  A dictionary mapping the descendants of the LightmapComponent-holding entity to their corresponding slot in the Lightmap resource.
- [LightmapComponent.EntityIndex](lightmapcomponent/entityindex.md)
### Adjusting indirect lighting
- [var indirectIrradianceContributionScale: Float](lightmapcomponent/indirectirradiancecontributionscale.md)
### Extracting baked surfaces
- [LightmapComponent.SurfaceExtractor](lightmapcomponent/surfaceextractor.md)
  This is a helper for extracting certain surface properties from entities within a lightmapped scene and rendering them out into the atlas defined by the light map.
- [LightmapComponent.FinalShadedColorBakeMaterial](lightmapcomponent/finalshadedcolorbakematerial.md)
  Material that should be used on lightmapped entities using the “beauty” bake type. This material only reads the lightmap data and does not perform shading calculations at runtime.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [class LightmapResource](lightmapresource.md)
  A resource containing references to lightmap texture atlases and descriptions of how parts of the atlases map to meshes in the scene. At a high level, this resource comprises two parts:
- [class DiffuseProbeResource](diffuseproberesource.md)
  A resource containing baked diffuse lighting data organized as a tetrahedral probe mesh.
- [struct DiffuseLightProbeGroupComponent](diffuselightprobegroupcomponent.md)
  A component that stores diffuse probe data for a spatial region.
- [struct DiffuseLightProbeReceiverComponent](diffuselightprobereceivercomponent.md)
  A component that receives diffuse lighting from a referenced probe group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lightmapcomponent)*