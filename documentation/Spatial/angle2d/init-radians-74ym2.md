# init(radians:)

**Framework**: Spatial  
**Kind**: init

Creates an angle with the specified floating-point radians.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
init<T>(radians: T) where T : BinaryFloatingPoint
```

## Parameters

- `radians`: A floating-point value that specifies the angle in radians.

## See Also

- [init()](angle2d/init.md)
  Creates an angle.
- [init(Angle)](angle2d/init(_:).md)
  Creates an angle from a SwiftUI angle.
- [init(radians: Double)](angle2d/init(radians:)-3zcwo.md)
  Creates an angle with the specified double-precision radians.
- [init(radians: Double)](angle2d/init(radians:)-6s7o6.md)
  Creates an angle with the specified double-precision radians.
- [init<T>(degrees: T)](angle2d/init(degrees:)-2obd.md)
  Creates an angle with the specified floating-point degrees.
- [init(degrees: Double)](angle2d/init(degrees:)-7y9lb.md)
  Creates an angle with the specified double-precision degrees.
- [static func degrees(Double) -> Angle2D](angle2d/degrees(_:).md)
  Returns a new angle structure with the specified double-precision degrees.
- [static func radians(Double) -> Angle2D](angle2d/radians(_:).md)
  Returns a new angle structure with the specified double-precision radians.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/angle2d/init(radians:)-74ym2)*