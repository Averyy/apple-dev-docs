# makePortal(surfaceStyle:boundaryStyle:boundaryMode:)

**Framework**: RealityKit  
**Kind**: method

Creates a complete portal with new entities.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func makePortal(surfaceStyle: PortalComponent.SurfaceStyle, boundaryStyle: PortalComponent.BoundaryStyle = .infinitePlane(), boundaryMode: PortalComponent.BoundaryMode = .disabled) -> PortalComponent.Portal
```

#### Return Value

A [`PortalComponent.Portal`](portalcomponent/portal.md) containing both configured entities

#### Discussion

Creates both a portal entity and a world entity, then configures them. Use this when you don’t have pre-existing entities to configure.

## Parameters

- `surfaceStyle`: The size of the portal mesh
- `boundaryStyle`: The clipping and crossing boundary shape (default: `.infinitePlane()`)
- `boundaryMode`: Whether to enable clipping, crossing, both, or neither (default: `.disabled`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/makeportal(surfacestyle:boundarystyle:boundarymode:))*