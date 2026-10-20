# PortalComponent.Plane

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A representation of a portal as an infinite plane.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct Plane
```

#### Overview

Enable the corresponding clipping and crossing features by passing this value in [`PortalComponent.ClippingMode.plane(_:)`](./clippingmode-swift.enum/plane%28_%29.md) or [`PortalComponent.CrossingMode.plane(_:)`](./crossingmode-swift.enum/plane%28_%29.md).

RealityKit defines the [`position`](./plane/position.md) and [`normal`](./plane/normal.md) properties in entity local space.

The following default values are available:

- [`positiveX`](./plane/positivex.md)
- [`negativeX`](./plane/negativex.md)
- [`positiveY`](./plane/positivey.md)
- [`negativeY`](./plane/negativey.md)
- [`positiveZ`](./plane/positivez.md)
- [`negativeZ`](./plane/negativez.md)

See [`PortalComponent`](../portalcomponent.md) for example usage.

## Topics

### Initializers
- [init(position: SIMD3<Float>, normal: SIMD3<Float>)](./plane/init%28position,normal%29.md)
  Creates a portal plane with position and normal.
### Instance Properties
- [var normal: SIMD3<Float>](./plane/normal.md)
  The normal of the portal plane, in entity local space.
- [var position: SIMD3<Float>](./plane/position.md)
  The position of the portal plane, in entity local space.
### Type Properties
- [static let negativeX: PortalComponent.Plane](./plane/negativex.md)
  A portal plane sitting at the origin facing the negative x direction.
- [static let negativeY: PortalComponent.Plane](./plane/negativey.md)
  A portal plane sitting at the origin facing the negative y direction.
- [static let negativeZ: PortalComponent.Plane](./plane/negativez.md)
  A portal plane sitting at the origin facing the negative z direction.
- [static let positiveX: PortalComponent.Plane](./plane/positivex.md)
  A portal plane sitting at the origin facing the positive x direction.
- [static let positiveY: PortalComponent.Plane](./plane/positivey.md)
  A portal plane sitting at the origin facing the positive y direction.
- [static let positiveZ: PortalComponent.Plane](./plane/positivez.md)
  A portal plane sitting at the origin facing the positive z direction.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/portalcomponent/plane)*