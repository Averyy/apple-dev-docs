# PortalFactory

**Framework**: RealityKit  
**Kind**: enum

A factory for creating portal entities with simplified configuration.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum PortalFactory
```

#### Overview

`PortalFactory` provides a convenient way to create complete portal setups by automatically configuring all necessary components including `WorldComponent`, `ModelComponent` with mesh and `PortalMaterial`, and `PortalComponent` with appropriate clipping and crossing modes.

The factory returns a `PortalSetup` containing a root entity with both the portal and world entities as children. Simply add the root entity to your scene to display the portal.

#### Example Usage

Create a simple flat portal:

```swift
let setup = PortalFactory.createPortal(
    style: .plane(width: 2.0, height: 1.5)
)
content.add(setup.rootEntity)

// Add content to the portal world
let sphere = ModelEntity(mesh: .generateSphere(radius: 0.3), materials: [SimpleMaterial()])
setup.worldEntity.addChild(sphere)
```

## Topics

### Creating a portal
- [static func createPortal(style: PortalFactory.Style, enableClipping: Bool, enableCrossing: Bool) -> PortalFactory.PortalSetup](portalfactory/createportal(style:enableclipping:enablecrossing:).md)
  Creates a complete portal setup with new entities.
- [static func createPortal(world: Entity, portalEntity: Entity?, style: PortalFactory.Style, enableClipping: Bool, enableCrossing: Bool) -> PortalFactory.PortalSetup](portalfactory/createportal(world:portalentity:style:enableclipping:enablecrossing:).md)
  Creates a portal targeting an existing world entity.
### Configuring the portal
- [PortalFactory.Style](portalfactory/style.md)
  Defines the visual appearance and geometry of a portal.
- [PortalFactory.PortalSetup](portalfactory/portalsetup.md)
  Contains the portal and world entities created by `PortalFactory`.

## See Also

- [struct RenderLayerComponent](renderlayercomponent.md)
  A component that defines which layers an entity participates in.
- [struct RenderLayer](renderlayer.md)
  A structured representation of render layers that provides type safety and clear semantics.
- [struct ClippingComponent](clippingcomponent.md)
  A component that clips entities and their children to a customizable bounding box volume with feathered edges.
- [struct ClippingPrimitiveComponent](clippingprimitivecomponent.md)
  Use ClippingComponent instead
- [struct OcclusionCullingComponent](occlusioncullingcomponent.md)
  A component that controls whether the system performs occlusion culling on the owning Entity and its descendants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalfactory)*