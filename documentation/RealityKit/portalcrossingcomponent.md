# PortalCrossingComponent

**Framework**: RealityKit  
**Kind**: struct

A component that allows entities to cross portal boundaries.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct PortalCrossingComponent
```

#### Overview

Set this component on an entity inside the portal world to opt that entity — and its descendants — into the portal’s crossing behavior. RealityKit then renders parts of the entity inside the portal as portal content and parts outside in the host scene.

Crossing-eligible entities cross the boundary configured by [`crossingMode`](portalcomponent/crossingmode-swift.property.md) on the portal entity:

- With [`PortalComponent.CrossingMode.plane(_:)`](portalcomponent/crossingmode-swift.enum/plane(_:).md), entities cross an infinite plane.
- With [`PortalComponent.CrossingMode.volume(_:)`](portalcomponent/crossingmode-swift.enum/volume(_:).md), entities cross the faces of a box.

The component has no configurable state; its presence on an entity is what enables crossing.

##### Inheritance

[`PortalCrossingComponent`](portalcrossingcomponent.md) propagates down the entity hierarchy. Setting it on an ancestor makes every descendant crossing-eligible without setting it on each one individually:

```swift
let world = Entity()
world.components.set(WorldComponent())

let group = Entity()
group.components.set(PortalCrossingComponent())

let body = Entity()
let head = Entity()
group.addChild(body)
group.addChild(head)

world.addChild(group)
// `body` and `head` both cross the portal because their ancestor `group` opts in.
```

An entity isn’t crossing-eligible if no ancestor in its chain (including itself) has [`PortalCrossingComponent`](portalcrossingcomponent.md), if [`isEnabled`](entity/isenabled.md) is `false` on any ancestor in the chain, or if it isn’t a descendant of an entity with [`WorldComponent`](worldcomponent.md).

See [`PortalComponent`](portalcomponent.md) for an end-to-end portal setup.

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