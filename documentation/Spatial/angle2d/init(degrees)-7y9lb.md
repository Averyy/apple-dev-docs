# init(degrees:)

**Framework**: Spatial  
**Kind**: init  
**Role**: Initializer

Creates an angle with the specified double-precision degrees.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(degrees: Double)
```

```c
static SPAngle SPAngleMakeWithDegrees(double degrees);
```

## Parameters

- `degrees`: A double-precision value that specifies the angle in degrees.

## See Also

### Creating an angle structure
- [init()](./init%28%29.md)
  Creates an angle.
- [init(radians: Double)](./init%28radians%29-3zcwo.md)
  Creates an angle with the specified double-precision radians.
- [init(radians: Double)](./init%28radians%29-6s7o6.md)
  Creates an angle with the specified double-precision radians.
- [init<T>(radians: T)](./init%28radians%29-74ym2.md)
  Creates an angle with the specified floating-point radians.
- [init<T>(degrees: T)](./init%28degrees%29-2obd.md)
  Creates an angle with the specified floating-point degrees.
- [static func degrees(Double) -> Angle2D](./degrees%28_%29.md)
  Returns a new angle structure with the specified double-precision degrees.
- [static func radians(Double) -> Angle2D](./radians%28_%29.md)
  Returns a new angle structure with the specified double-precision radians.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/angle2d/init(degrees:)-7y9lb)*