# CMAcceleration

**Framework**: Core Motion  
**Kind**: struct  
**Role**: Structure

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

```c
typedef struct { ... } CMAcceleration;
```

## Overview

A G is a unit of gravitation force equal to that exerted by the earth’s gravitational field (9.81 m s−2).

## Topics

### Initializers
- [init()](./cmacceleration/init%28%29.md)
- [init(x: Double, y: Double, z: Double)](./cmacceleration/init%28x,y,z%29.md)
### Getting the Acceleration Values
- [var x: Double](./cmacceleration/x.md)
  X-axis acceleration in G’s (gravitational force).
- [var y: Double](./cmacceleration/y.md)
  Y-axis acceleration in G’s (gravitational force).
- [var z: Double](./cmacceleration/z.md)
  Z-axis acceleration in G’s (gravitational force).

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Accessing Accelerometer Data
- [var acceleration: CMAcceleration](./cmaccelerometerdata/acceleration.md)
  The acceleration measured by the accelerometer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmacceleration)*