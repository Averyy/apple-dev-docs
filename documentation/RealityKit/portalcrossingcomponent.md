# PortalCrossingComponent

**Framework**: RealityKit  
**Kind**: struct

A component that allows entities to cross portal boundaries.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
struct PortalCrossingComponent
```

#### Overview

You use this with [`PortalComponent.CrossingMode`](portalcomponent/crossingmode-swift.enum.md) to enable portal crossing features.

When you set this on an entity, this component defines whether the entity is capable of crossing the portal boundary.

Entities without this component, entities where [`isEnabled`](entity/isenabled.md) is `false`, and entities without a containing entity that specifies inherited portal crossing, aren’t able to cross portals.

See [`PortalComponent`](portalcomponent.md) for detailed usage.

## Topics

### Initializers
- [init()](portalcrossingcomponent/init.md)

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [struct PortalMaterial](portalmaterial.md)
  A material that makes the mesh part a portal to a different world.
- [PortalMaterial.FaceCulling](portalmaterial/faceculling-swift.typealias.md)
  An alias for the cull mode object that’s appropriate for this material class.
- [PortalMaterial.TriangleFillMode](portalmaterial/trianglefillmode-swift.typealias.md)
  An alias for the triangle fill mode object that’s appropriate for this material class.
- [struct PortalComponent](portalcomponent.md)
  A component that turns mesh surfaces into portals to a different world.
- [struct WorldComponent](worldcomponent.md)
  A component that defines a portal world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcrossingcomponent)*