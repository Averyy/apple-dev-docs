# PortalComponent.ClippingMode

**Framework**: RealityKit  
**Kind**: enum

Specifies the mode of clipping for a portal.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
enum ClippingMode
```

#### Overview

This type can be passed into [`clippingMode`](portalcomponent/clippingmode-swift.property.md) to configure the portal component’s clipping feature.

With [`PortalComponent.ClippingMode.disabled`](portalcomponent/clippingmode-swift.enum/disabled.md), contents in portal world are not clipped

With [`PortalComponent.ClippingMode.plane(_:)`](portalcomponent/clippingmode-swift.enum/plane(_:).md), contents within portal are clipped by the edge of the plane.

## Topics

### Operators
- [static func == (PortalComponent.ClippingMode, PortalComponent.ClippingMode) -> Bool](portalcomponent/clippingmode-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [PortalComponent.ClippingMode.disabled](portalcomponent/clippingmode-swift.enum/disabled.md)
  Disables clipping of the contents within the portal.
- [PortalComponent.ClippingMode.plane(_:)](portalcomponent/clippingmode-swift.enum/plane(_:).md)
  Clips the contents within the portal by the edge of the plane.
### Default Implementations
- [Equatable Implementations](portalcomponent/clippingmode-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/clippingmode-swift.enum)*