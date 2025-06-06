# WorldComponent

**Framework**: RealityKit  
**Kind**: struct

A component that defines a portal world.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct WorldComponent
```

#### Overview

This component separates an entity and its descendants from the default world, allowing it to only be visible through a portal.

Use a [`PortalComponent`](portalcomponent.md) and point its [`targetEntity`](portalcomponent/targetentity.md) to this entity to render this world.

See [`PortalComponent`](portalcomponent.md) for information about example usage, clipping, crossing, and lighting.

## Topics

### Initializers
- [init()](worldcomponent/init.md)
### Default Implementations
- [Component Implementations](worldcomponent/component-implementations.md)

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
- [struct PortalCrossingComponent](portalcrossingcomponent.md)
  A component that allows entities to cross portal boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/worldcomponent)*