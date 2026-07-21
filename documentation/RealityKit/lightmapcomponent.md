# LightmapComponent

**Framework**: RealityKit  
**Kind**: struct

Describes how a lightmap is applied to parts of the scene.

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

#### Overview

[`LightmapComponent`](lightmapcomponent.md) specifies which children of its owning entity should have a lightmap applied to them, and connects those children to their corresponding data in a [`LightmapResource`](lightmapresource.md).

To use [`LightmapComponent`](lightmapcomponent.md), first create a [`LightmapResource`](lightmapresource.md) using textures produced by an offline baking process. Then, create a new [`LightmapComponent`](lightmapcomponent.md) backed by the [`LightmapResource`](lightmapresource.md), and use the [`entityIndexInLightmapResource`](lightmapcomponent/entityindexinlightmapresource.md) property to map each entity that you wish to be lightmapped, to its corresponding slot in the lightmap resource. Finally, add the [`LightmapComponent`](lightmapcomponent.md) to an entity that sits above all of the lightmapped entities in the hierachy.

## Topics

### Classes
- [LightmapComponent.SurfaceExtractor](lightmapcomponent/surfaceextractor.md)
  This is a helper for extracting certain surface properties from entities within a lightmapped scene and rendering them out into the atlas defined by the light map.
### Structures
- [LightmapComponent.FinalShadedColorBakeMaterial](lightmapcomponent/finalshadedcolorbakematerial.md)
  Material that should be used on lightmapped entities using the “beauty” bake type. This material only reads the lightmap data and does not perform shading calculations at runtime.
### Initializers
- [init(resource: LightmapResource)](lightmapcomponent/init(resource:).md)
  Creates a new LightmapComponent backed by the given LightmapResource.
### Instance Properties
- [var entityIndexInLightmapResource: [Entity : LightmapComponent.EntityIndex]](lightmapcomponent/entityindexinlightmapresource.md)
  A dictionary mapping the descendants of the LightmapComponent-holding entity to their corresponding slot in the Lightmap resource.
- [var indirectIrradianceContributionScale: Float](lightmapcomponent/indirectirradiancecontributionscale.md)
  Multiplies the indirect irradiance contribution stored in the lightmap by the given value.
- [var lightmap: LightmapResource](lightmapcomponent/lightmap.md)
  The LightmapResource backing this component.
### Type Aliases
- [LightmapComponent.EntityIndex](lightmapcomponent/entityindex.md)

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [class LightmapResource](lightmapresource.md)
  A resource containing references to lightmap texture atlases and descriptions of how parts of the atlases map to meshes in the scene.
- [class LightmapResource](lightmapresource.md)
  A resource containing references to lightmap texture atlases and descriptions of how parts of the atlases map to meshes in the scene.
- [class DiffuseProbeResource](diffuseproberesource.md)
  A resource containing baked diffuse lighting data organized as a tetrahedral probe mesh.
- [struct DiffuseLightProbeGroupComponent](diffuselightprobegroupcomponent.md)
  A component that stores diffuse probe data for a spatial region.
- [struct DiffuseLightProbeReceiverComponent](diffuselightprobereceivercomponent.md)
  A component that receives diffuse lighting from a referenced probe group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lightmapcomponent)*