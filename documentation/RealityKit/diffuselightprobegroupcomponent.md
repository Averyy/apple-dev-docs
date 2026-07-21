# DiffuseLightProbeGroupComponent

**Framework**: RealityKit  
**Kind**: struct

A component that stores diffuse probe data for a spatial region.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct DiffuseLightProbeGroupComponent
```

#### Overview

Attach this component to an entity to designate it as a diffuse probe group — a positioned source of baked diffuse lighting. Other entities can reference this group via [`DiffuseLightProbeReceiverComponent`](diffuselightprobereceivercomponent.md) to receive spatially-varying diffuse illumination.

This follows the same source/receiver pattern as `ImageBasedLightComponent` / `ImageBasedLightReceiverComponent`.

```swift
let probeGroup = Entity()
probeGroup.components[DiffuseLightProbeGroupComponent.self] =
    DiffuseLightProbeGroupComponent(resource: probeResource)
```

## Topics

### Initializers
- [init(resource: DiffuseProbeResource)](diffuselightprobegroupcomponent/init(resource:).md)
  Creates a diffuse light probe group component.
### Instance Properties
- [var resource: DiffuseProbeResource](diffuselightprobegroupcomponent/resource.md)
  The diffuse probe resource containing baked lighting data for this group.

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [class DiffuseProbeResource](diffuseproberesource.md)
  A resource containing baked diffuse lighting data organized as a tetrahedral probe mesh.
- [struct DiffuseLightProbeReceiverComponent](diffuselightprobereceivercomponent.md)
  A component that receives diffuse lighting from a referenced probe group.
- [class LightmapResource](lightmapresource.md)
  A resource containing references to lightmap texture atlases and descriptions of how parts of the atlases map to meshes in the scene.
- [struct LightmapComponent](lightmapcomponent.md)
  Describes how a lightmap is applied to parts of the scene.
- [class DiffuseProbeResource](diffuseproberesource.md)
  A resource containing baked diffuse lighting data organized as a tetrahedral probe mesh.
- [struct DiffuseLightProbeReceiverComponent](diffuselightprobereceivercomponent.md)
  A component that receives diffuse lighting from a referenced probe group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/diffuselightprobegroupcomponent)*