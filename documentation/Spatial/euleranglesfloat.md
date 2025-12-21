# EulerAnglesFloat

**Framework**: Spatial  
**Kind**: struct

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct EulerAnglesFloat
```

#### Overview

A structure that represents Euler angles, in radians, and ordering.

## Topics

### Initializers
- [init()](euleranglesfloat/init.md)
- [init(angles: simd_float3, order: __SPEulerAngleOrder)](euleranglesfloat/init(angles:order:).md)
- [init(x: Angle2DFloat, y: Angle2DFloat, z: Angle2DFloat, order: EulerAngles.Order)](euleranglesfloat/init(x:y:z:order:).md)
  Returns a new Euler angles structure from three angle structures.
### Instance Properties
- [var angles: simd_float3](euleranglesfloat/angles.md)
  A three-element vector that contains the angles, in radians.
- [var order: __SPEulerAngleOrder](euleranglesfloat/order.md)
  A constant that specify the Euler angle order.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/euleranglesfloat)*