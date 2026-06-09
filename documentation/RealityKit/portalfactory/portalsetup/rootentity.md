# rootEntity

**Framework**: RealityKit  
**Kind**: property

The root entity containing both portal and world entities as children.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
let rootEntity: Entity
```

#### Discussion

Add this entity to your scene to display the complete portal setup. Position and orient this entity to place the portal in your 3D space.

## See Also

- [let portalEntity: Entity](portalfactory/portalsetup/portalentity.md)
  The portal entity with `ModelComponent` and `PortalComponent` configured.
- [let worldEntity: Entity](portalfactory/portalsetup/worldentity.md)
  The world entity with `WorldComponent` configured.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalfactory/portalsetup/rootentity)*