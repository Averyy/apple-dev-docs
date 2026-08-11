# configure(world:portalEntity:surfaceStyle:boundaryStyle:boundaryMode:)

**Framework**: RealityKit  
**Kind**: method

Configures an existing pair of entities as a portal and its target world.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func configure(world: Entity, portalEntity: Entity, surfaceStyle: PortalComponent.SurfaceStyle, boundaryStyle: PortalComponent.BoundaryStyle = .infinitePlane(), boundaryMode: PortalComponent.BoundaryMode = .none)
```

#### Discussion

This method writes a coordinated set of components onto the two entities you provide. Use it when you already own both entities — for example, when the portal entity holds gestures or other components, or when the world entity is a child of an existing scene.

On the world entity, this method sets:

- [`WorldComponent`](worldcomponent.md)

On the portal entity, this method sets:

- [`ModelComponent`](modelcomponent.md) with a flat plane mesh sized by `surfaceStyle`, applied with [`PortalMaterial`](portalmaterial.md)
- [`PortalComponent`](portalcomponent.md) with [`clippingMode`](portalcomponent/clippingmode-swift.property.md) and [`crossingMode`](portalcomponent/crossingmode-swift.property.md) configured from `boundaryStyle` and `boundaryMode`

This method replaces any existing [`WorldComponent`](worldcomponent.md), [`ModelComponent`](modelcomponent.md), or [`PortalComponent`](portalcomponent.md) on the entities. Other components on either entity are preserved.

To create both entities at once, use [`makePortal(surfaceStyle:boundaryStyle:boundaryMode:)`](portalcomponent/makeportal(surfacestyle:boundarystyle:boundarymode:).md) instead.

## Parameters

- `world`: The entity that contains the portal’s content. Place portal world descendants under this entity.
- `portalEntity`: The entity that displays the portal surface in the host scene.
- `surfaceStyle`: The size of the portal surface mesh.
- `boundaryStyle`: The shape of the clipping and crossing boundary. Defaults to [`infinitePlane()`](portalcomponent/boundarystyle/infiniteplane().md).
- `boundaryMode`: The combination of clipping and crossing behaviors to enable. Defaults to [`PortalComponent.BoundaryMode.none`](portalcomponent/boundarymode/none.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/configure(world:portalentity:surfacestyle:boundarystyle:boundarymode:))*