# PortalFactory.PortalSetup

**Framework**: RealityKit  
**Kind**: struct

Contains the portal and world entities created by `PortalFactory`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct PortalSetup
```

#### Overview

The setup includes a root entity containing both the portal and world entities as children. Simply add `rootEntity` to your scene to display the portal.

## Topics

### Accessing portal entities
- [let portalEntity: Entity](portalfactory/portalsetup/portalentity.md)
  The portal entity with `ModelComponent` and `PortalComponent` configured.
- [let worldEntity: Entity](portalfactory/portalsetup/worldentity.md)
  The world entity with `WorldComponent` configured.
- [let rootEntity: Entity](portalfactory/portalsetup/rootentity.md)
  The root entity containing both portal and world entities as children.

## See Also

- [PortalFactory.Style](portalfactory/style.md)
  Defines the visual appearance and geometry of a portal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalfactory/portalsetup)*