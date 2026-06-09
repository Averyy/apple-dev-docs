# worldEntity

**Framework**: RealityKit  
**Kind**: property

The world entity with `WorldComponent` configured.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
let worldEntity: Entity
```

#### Discussion

Add child entities to this entity to populate the portal’s world. Content added here will be visible through the portal. This entity is a child of `rootEntity`.

## See Also

- [let portalEntity: Entity](portalfactory/portalsetup/portalentity.md)
  The portal entity with `ModelComponent` and `PortalComponent` configured.
- [let rootEntity: Entity](portalfactory/portalsetup/rootentity.md)
  The root entity containing both portal and world entities as children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalfactory/portalsetup/worldentity)*