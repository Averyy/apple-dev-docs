# DiffuseLightProbeReceiverComponent

**Framework**: RealityKit  
**Kind**: struct

A component that receives diffuse lighting from a referenced probe group.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct DiffuseLightProbeReceiverComponent
```

#### Overview

Attach this component to entities that should receive spatially-varying diffuse indirect lighting. As the entity moves through the scene, the system automatically interpolates diffuse lighting from the probe group based on the entity’s current position.

This follows the same receiver pattern as `ImageBasedLightReceiverComponent`.

```swift
character.components[DiffuseLightProbeReceiverComponent.self] =
    DiffuseLightProbeReceiverComponent(probeGroup: probeGroupEntity)
```

## Topics

### Initializers
- [init(probeGroup: Entity)](diffuselightprobereceivercomponent/init(probegroup:).md)
  Creates a diffuse light probe receiver component.
### Instance Properties
- [var probeGroup: Entity](diffuselightprobereceivercomponent/probegroup.md)
  The entity providing diffuse probe lighting to this receiver.

## Relationships

### Conforms To
- [Component](component.md)
- [Equatable](../Swift/Equatable.md)

## See Also

- [struct DiffuseLightProbeGroupComponent](diffuselightprobegroupcomponent.md)
  A component that stores diffuse probe data for a spatial region.
- [class DiffuseProbeResource](diffuseproberesource.md)
  A resource containing baked diffuse lighting data organized as a tetrahedral probe mesh.
- [class LightmapResource](lightmapresource.md)
  A resource containing references to lightmap texture atlases and descriptions of how parts of the atlases map to meshes in the scene. At a high level, this resource comprises two parts:
- [struct LightmapComponent](lightmapcomponent.md)
- [class DiffuseProbeResource](diffuseproberesource.md)
  A resource containing baked diffuse lighting data organized as a tetrahedral probe mesh.
- [struct DiffuseLightProbeGroupComponent](diffuselightprobegroupcomponent.md)
  A component that stores diffuse probe data for a spatial region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/diffuselightprobereceivercomponent)*