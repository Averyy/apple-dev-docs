# configure(world:portalEntity:surfaceStyle:boundaryStyle:boundaryMode:)

**Framework**: RealityKit  
**Kind**: method

Sets components on an existing portal surface entity and its world entity, replacing any previously set `WorldComponent`, `ModelComponent`, or `PortalComponent`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func configure(world: Entity, portalEntity: Entity, surfaceStyle: PortalComponent.SurfaceStyle, boundaryStyle: PortalComponent.BoundaryStyle = .infinitePlane(), boundaryMode: PortalComponent.BoundaryMode = .disabled)
```

#### Discussion

This method configures both entities in place:

- Sets `WorldComponent` on `world`
- Sets `ModelComponent` with a flat plane mesh sized by `surfaceStyle`
- Applies `PortalMaterial` to the portal surface
- Configures `PortalComponent` with clipping and crossing modes from `boundaryStyle` and `boundaryMode`

## Parameters

- `world`: The entity that will contain portal content (`WorldComponent` set automatically)
- `portalEntity`: The entity that will act as the portal surface
- `surfaceStyle`: The size of the portal mesh
- `boundaryStyle`: The clipping and crossing boundary shape (default: `.infinitePlane()`)
- `boundaryMode`: Whether to enable clipping, crossing, both, or neither (default: `.disabled`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/configure(world:portalentity:surfacestyle:boundarystyle:boundarymode:))*