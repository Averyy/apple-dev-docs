# CMAcceleration

**Framework**: Core Motion  
**Kind**: struct

The type of a structure containing 3-axis acceleration values.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct CMAcceleration
```

#### Overview

A G is a unit of gravitation force equal to that exerted by the earth’s gravitational field (9.81 m s−2).

## Topics

### Initializers
- [init()](cmacceleration/init.md)
- [init(x: Double, y: Double, z: Double)](cmacceleration/init(x:y:z:).md)
### Getting the Acceleration Values
- [var x: Double](cmacceleration/x.md)
  X-axis acceleration in G’s (gravitational force).
- [var y: Double](cmacceleration/y.md)
  Y-axis acceleration in G’s (gravitational force).
- [var z: Double](cmacceleration/z.md)
  Z-axis acceleration in G’s (gravitational force).

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var acceleration: CMAcceleration](cmaccelerometerdata/acceleration.md)
  The acceleration measured by the accelerometer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmacceleration)*