# PortalComponent.Plane

**Framework**: RealityKit  
**Kind**: struct

A representation of a portal as an infinite plane.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct Plane
```

#### Overview

Enable the corresponding clipping and crossing features by passing this value in [`PortalComponent.ClippingMode.plane(_:)`](portalcomponent/clippingmode-swift.enum/plane(_:).md) or [`PortalComponent.CrossingMode.plane(_:)`](portalcomponent/crossingmode-swift.enum/plane(_:).md).

RealityKit defines the [`position`](portalcomponent/plane/position.md) and [`normal`](portalcomponent/plane/normal.md) properties in entity local space.

The following default values are available:

- [`positiveX`](portalcomponent/plane/positivex.md)
- [`negativeX`](portalcomponent/plane/negativex.md)
- [`positiveY`](portalcomponent/plane/positivey.md)
- [`negativeY`](portalcomponent/plane/negativey.md)
- [`positiveZ`](portalcomponent/plane/positivez.md)
- [`negativeZ`](portalcomponent/plane/negativez.md)

See [`PortalComponent`](portalcomponent.md) for example usage.

## Topics

### Operators
- [static func == (PortalComponent.Plane, PortalComponent.Plane) -> Bool](portalcomponent/plane/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(position: SIMD3<Float>, normal: SIMD3<Float>)](portalcomponent/plane/init(position:normal:).md)
  Creates a portal plane with position and normal.
### Instance Properties
- [var normal: SIMD3<Float>](portalcomponent/plane/normal.md)
  The normal of the portal plane, in entity local space.
- [var position: SIMD3<Float>](portalcomponent/plane/position.md)
  The position of the portal plane, in entity local space.
### Type Properties
- [static let negativeX: PortalComponent.Plane](portalcomponent/plane/negativex.md)
  A portal plane sitting at the origin facing the negative x direction.
- [static let negativeY: PortalComponent.Plane](portalcomponent/plane/negativey.md)
  A portal plane sitting at the origin facing the negative y direction.
- [static let negativeZ: PortalComponent.Plane](portalcomponent/plane/negativez.md)
  A portal plane sitting at the origin facing the negative z direction.
- [static let positiveX: PortalComponent.Plane](portalcomponent/plane/positivex.md)
  A portal plane sitting at the origin facing the positive x direction.
- [static let positiveY: PortalComponent.Plane](portalcomponent/plane/positivey.md)
  A portal plane sitting at the origin facing the positive y direction.
- [static let positiveZ: PortalComponent.Plane](portalcomponent/plane/positivez.md)
  A portal plane sitting at the origin facing the positive z direction.
### Default Implementations
- [Equatable Implementations](portalcomponent/plane/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/plane)*