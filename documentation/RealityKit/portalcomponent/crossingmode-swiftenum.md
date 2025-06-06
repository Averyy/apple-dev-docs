# PortalComponent.CrossingMode

**Framework**: RealityKit  
**Kind**: enum

Specifies the mode of crossing for a portal.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
enum CrossingMode
```

#### Overview

You pass this type to [`crossingMode`](portalcomponent/crossingmode-swift.property.md) to configure the portal component’s crossing feature.

Use [`PortalComponent.CrossingMode.disabled`](portalcomponent/crossingmode-swift.enum/disabled.md) to disallow contents within the portal to cross out of the portal boundary.

Use [`PortalComponent.CrossingMode.plane(_:)`](portalcomponent/crossingmode-swift.enum/plane(_:).md) to allow contents within the portal world with a [`PortalCrossingComponent`](portalcrossingcomponent.md) to cross out of this planar definition of the portal boundary.

## Topics

### Operators
- [static func == (PortalComponent.CrossingMode, PortalComponent.CrossingMode) -> Bool](portalcomponent/crossingmode-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [PortalComponent.CrossingMode.disabled](portalcomponent/crossingmode-swift.enum/disabled.md)
  Disallows contents within the portal to cross out of the portal boundary.
- [PortalComponent.CrossingMode.plane(_:)](portalcomponent/crossingmode-swift.enum/plane(_:).md)
  Allows contents within the portal to cross out of the portal along the provided plane.
### Default Implementations
- [Equatable Implementations](portalcomponent/crossingmode-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/crossingmode-swift.enum)*