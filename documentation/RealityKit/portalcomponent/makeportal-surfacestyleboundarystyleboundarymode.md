# makePortal(surfaceStyle:boundaryStyle:boundaryMode:)

**Framework**: RealityKit  
**Kind**: method

Creates a portal entity and a world entity, and configures them.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func makePortal(surfaceStyle: PortalComponent.SurfaceStyle, boundaryStyle: PortalComponent.BoundaryStyle = .infinitePlane(), boundaryMode: PortalComponent.BoundaryMode = .disabled) -> PortalComponent.Portal
```

#### Return Value

A [`PortalComponent.Portal`](portalcomponent/portal.md) containing the new portal entity and world entity.

#### Discussion

This is the simplest way to set up a portal. The returned [`PortalComponent.Portal`](portalcomponent/portal.md) value contains a fresh portal entity and a fresh world entity that you add to your scene. To add portal world content, parent it under the returned `worldEntity`.

```swift
let portal = PortalComponent.makePortal(
    surfaceStyle: .init(width: 0.5, height: 0.5),
    boundaryStyle: .infinitePlane(),
    boundaryMode: .clippingAndCrossing
)

content.add(portal.worldEntity)
content.add(portal.portalEntity)
```

To configure entities you already own — for example, a portal entity that has gesture components, or a world entity that’s already in your scene hierarchy — use [`configure(world:portalEntity:surfaceStyle:boundaryStyle:boundaryMode:)`](portalcomponent/configure(world:portalentity:surfacestyle:boundarystyle:boundarymode:).md) instead.

## Parameters

- `surfaceStyle`: The size of the portal surface mesh.
- `boundaryStyle`: The shape of the clipping and crossing boundary. Defaults to [`infinitePlane()`](portalcomponent/boundarystyle/infiniteplane().md).
- `boundaryMode`: The combination of clipping and crossing behaviors to enable. Defaults to [`PortalComponent.BoundaryMode.disabled`](portalcomponent/boundarymode/disabled.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/makeportal(surfacestyle:boundarystyle:boundarymode:))*