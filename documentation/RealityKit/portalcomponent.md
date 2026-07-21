# PortalComponent

**Framework**: RealityKit  
**Kind**: struct

A component that turns mesh surfaces into portals to a different world.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct PortalComponent
```

#### Overview

A RealityKit portal defines a way to look into a different, immersive world. You define an entity as a portal when it also has a [`ModelComponent`](modelcomponent.md) that contains a mesh part with [`PortalMaterial`](portalmaterial.md).

To create a portal, set its [`targetEntity`](portalcomponent/targetentity.md) property to an entity with a [`WorldComponent`](worldcomponent.md). Entities under that world only render within the portal.

##### Quick Start

On iOS 27, macOS 27, tvOS 27, visionOS 27, and later, [`makePortal(surfaceStyle:boundaryStyle:boundaryMode:)`](portalcomponent/makeportal(surfacestyle:boundarystyle:boundarymode:).md) creates a configured portal entity and its target world entity in a single call:

```swift
let portal = PortalComponent.makePortal(
   surfaceStyle: .init(width: 0.5, height: 0.5),
   boundaryStyle: .infinitePlane(),
   boundaryMode: .clippingAndCrossing
)

content.add(portal.worldEntity)
content.add(portal.portalEntity)
```

To configure existing entities, use [`configure(world:portalEntity:surfaceStyle:boundaryStyle:boundaryMode:)`](portalcomponent/configure(world:portalentity:surfacestyle:boundarystyle:boundarymode:).md).

##### Manual Construction

On earlier OS releases, or when you need direct control over the portal’s mesh, material, or boundary geometry, set the components yourself:

```swift
let world = Entity()
world.components.set(WorldComponent())

let portal = Entity()
portal.components.set(
   ModelComponent(
       mesh: .generatePlane(width: 0.5, height: 0.5, cornerRadius: 0.1),
       materials: [PortalMaterial()]
   )
)
portal.components.set(PortalComponent(target: world))

content.add(world)
content.add(portal)
```

##### Clipping and Crossing

You can enable clipping by configuring [`clippingMode`](portalcomponent/clippingmode-swift.property.md) to something other than [`PortalComponent.ClippingMode.disabled`](portalcomponent/clippingmode-swift.enum/disabled.md). For example, you can use [`PortalComponent.ClippingMode.plane(_:)`](portalcomponent/clippingmode-swift.enum/plane(_:).md) to clip portal content to an infinite half-space, or [`PortalComponent.ClippingMode.volume(_:)`](portalcomponent/clippingmode-swift.enum/volume(_:).md) to clip to a box-bounded region of space. Clipping prevents portal world content from rendering beyond the portal boundary and causing depth confusion.

Entities inside the portal world with a [`PortalCrossingComponent`](portalcrossingcomponent.md) can freely cross in and out of the portal boundary in any of the following platforms:

- iOS 18 and later
- macOS 15 and later
- visionOS 2 and later

You can enable the crossing feature by configuring [`crossingMode`](portalcomponent/crossingmode-swift.property.md) to something other than [`PortalComponent.CrossingMode.disabled`](portalcomponent/crossingmode-swift.enum/disabled.md). Such as [`PortalComponent.CrossingMode.plane(_:)`](portalcomponent/crossingmode-swift.enum/plane(_:).md) for an infinite-plane crossing, or [`PortalComponent.CrossingMode.volume(_:)`](portalcomponent/crossingmode-swift.enum/volume(_:).md) for a box-bounded crossing.

```swift
let world = Entity()
world.components.set(WorldComponent())

// Create an entity that doesn't cross beyond the portal bounds.
let notCrossing = Entity()

// Create an entity that crosses beyond the portal bounds.
let willCross = Entity()
willCross.components.set(PortalCrossingComponent())

world.addChild(notCrossing)
world.addChild(willCross)

// Set up a crossable portal, without a near clip.
let portal = Entity()
portal.components.set(
   ModelComponent(
       mesh: .generatePlane(width: 0.5, height: 0.5, cornerRadius: 0.1),
       materials: [PortalMaterial()]
   )
)
var portalComp = PortalComponent(target: world)
portalComp.clippingMode = .plane(.positiveZ)
portalComp.crossingMode = .plane(.positiveZ)
portal.components.set(portalComp)

content.add(world)
content.add(portal)
```

The spaceships below have a [`PortalCrossingComponent`](portalcrossingcomponent.md).

The spaceships below *don’t* have a [`PortalCrossingComponent`](portalcrossingcomponent.md).

##### Lighting

You define the lighting in a portal world with [`ImageBasedLightComponent`](imagebasedlightcomponent.md) and [`ImageBasedLightReceiverComponent`](imagebasedlightreceivercomponent.md).

RealityKit provides a default IBL if you don’t specify one with [`ImageBasedLightReceiverComponent`](imagebasedlightreceivercomponent.md).

Contents within a portal world don’t receive real-world probe lighting. However, you can achieve a  similar effect in the portal world using [`VirtualEnvironmentProbeComponent`](virtualenvironmentprobecomponent.md).

You can configure this virtual probe lighting contribution with [`EnvironmentLightingConfigurationComponent`](environmentlightingconfigurationcomponent.md).

Dynamic lights, such as [`PointLightComponent`](pointlightcomponent.md) and [`DirectionalLightComponent`](directionallightcomponent.md), don’t cross world bounds.

Different lighting environments light the portal crossing entities based on which side of the portal they are on:

- When inside the portal, the portal world’s lighting lights the entity.
- When outside the portal, the default world’s lighting lights the entity.

## Topics

### Defining the portal volume
- [PortalComponent.Volume](portalcomponent/volume.md)
  A box-shaped region in portal-local space that defines a volumetric portal boundary.
### Configuring lighting blend
- [var lightingBlendDistance: Float](portalcomponent/lightingblenddistance.md)
  The distance over which crossing-entity lighting blends between the host scene and the portal world.
### Structures
- [PortalComponent.BoundaryStyle](portalcomponent/boundarystyle.md)
  The shape of a portal’s clipping and crossing boundary.
- [PortalComponent.ClippingPlane](portalcomponent/clippingplane-swift.struct.md)
  A representation of a portal as an infinite plane.
- [PortalComponent.Options](portalcomponent/options.md)
  Options to toggle the portal features on and off.
- [PortalComponent.Plane](portalcomponent/plane.md)
  A representation of a portal as an infinite plane.
- [PortalComponent.Portal](portalcomponent/portal.md)
  A pair of related entities that make up a configured portal.
- [PortalComponent.SurfaceStyle](portalcomponent/surfacestyle.md)
  The size of the flat plane mesh that RealityKit generates for a portal.
### Initializers
- [init(target: Entity, clippingMode: PortalComponent.ClippingMode, crossingMode: PortalComponent.CrossingMode)](portalcomponent/init(target:clippingmode:crossingmode:).md)
  Creates a portal component with a target entity, clipping mode, and crossing mode.
- [init(target: Entity, clippingPlane: PortalComponent.ClippingPlane?)](portalcomponent/init(target:clippingplane:).md)
  Creates a portal component with a target entity and an optional clipping plane.
- [init(target: Entity, plane: PortalComponent.Plane, options: PortalComponent.Options)](portalcomponent/init(target:plane:options:).md)
  Creates a portal component with a target entity, a single planar definition, and portal options.
### Instance Properties
- [var clippingMode: PortalComponent.ClippingMode](portalcomponent/clippingmode-swift.property.md)
  The clipping behavior of the portal component.
- [var clippingPlane: PortalComponent.ClippingPlane?](portalcomponent/clippingplane-swift.property.md)
  The clipping plane of the portal, in the entity’s local coordinates.
- [var crossingMode: PortalComponent.CrossingMode](portalcomponent/crossingmode-swift.property.md)
  The crossing behavior of the portal component.
- [var targetEntity: Entity?](portalcomponent/targetentity.md)
  The root entity for the portal’s target world.
### Type Methods
- [static func configure(world: Entity, portalEntity: Entity, surfaceStyle: PortalComponent.SurfaceStyle, boundaryStyle: PortalComponent.BoundaryStyle, boundaryMode: PortalComponent.BoundaryMode)](portalcomponent/configure(world:portalentity:surfacestyle:boundarystyle:boundarymode:).md)
  Configures an existing pair of entities as a portal and its target world.
- [static func makePortal(surfaceStyle: PortalComponent.SurfaceStyle, boundaryStyle: PortalComponent.BoundaryStyle, boundaryMode: PortalComponent.BoundaryMode) -> PortalComponent.Portal](portalcomponent/makeportal(surfacestyle:boundarystyle:boundarymode:).md)
  Creates a portal entity and a world entity, and configures them.
### Enumerations
- [PortalComponent.BoundaryMode](portalcomponent/boundarymode.md)
  A combination of clipping and crossing behaviors to apply to a portal boundary.
- [PortalComponent.ClippingMode](portalcomponent/clippingmode-swift.enum.md)
  Specifies the mode of clipping for a portal.
- [PortalComponent.CrossingMode](portalcomponent/crossingmode-swift.enum.md)
  Specifies the mode of crossing for a portal.

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
- [struct WorldComponent](worldcomponent.md)
  A component that defines a portal world.
- [struct PortalCrossingComponent](portalcrossingcomponent.md)
  A component that allows entities to cross portal boundaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent)*