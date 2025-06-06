# Angle2D

**Framework**: Spatial  
**Kind**: struct

A geometric angle with a value you access in either radians or degrees.

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
struct Angle2D
```

## Topics

### Creating an angle structure
- [init()](angle2d/init.md)
  Creates an angle.
- [init(Angle)](angle2d/init(_:).md)
  Creates an angle from a SwiftUI angle.
- [init(radians: Double)](angle2d/init(radians:)-3zcwo.md)
  Creates an angle with the specified double-precision radians.
- [init(radians: Double)](angle2d/init(radians:)-6s7o6.md)
  Creates an angle with the specified double-precision radians.
- [init<T>(radians: T)](angle2d/init(radians:)-74ym2.md)
  Creates an angle with the specified floating-point radians.
- [init<T>(degrees: T)](angle2d/init(degrees:)-2obd.md)
  Creates an angle with the specified floating-point degrees.
- [init(degrees: Double)](angle2d/init(degrees:)-7y9lb.md)
  Creates an angle with the specified double-precision degrees.
- [static func degrees(Double) -> Angle2D](angle2d/degrees(_:).md)
  Returns a new angle structure with the specified double-precision degrees.
- [static func radians(Double) -> Angle2D](angle2d/radians(_:).md)
  Returns a new angle structure with the specified double-precision radians.
### Inspecting an angle’s properties
- [var degrees: Double](angle2d/degrees.md)
  The angle in degrees.
- [var radians: Double](angle2d/radians.md)
  The angle in radians.
### Geometry functions
- [func cos(Angle2D) -> Double](cos(_:).md)
  Returns the cosine of the specified angle.
- [func cosh(Angle2D) -> Double](cosh(_:).md)
  Returns the hyperbolic cosine of the specified angle.
- [func sin(Angle2D) -> Double](sin(_:).md)
  Returns the sine of the specified angle.
- [func sinh(Angle2D) -> Double](sinh(_:).md)
  Returns the hyperbolic sine of the specified angle.
- [func tan(Angle2D) -> Double](tan(_:).md)
  Returns the tangent of the specified angle.
- [func tanh(Angle2D) -> Double](tanh(_:).md)
  Returns the hyperbolic tangent of the specified angle.
- [static func acos(Double) -> Angle2D](angle2d/acos(_:).md)
  Returns the inverse cosine of the specified value.
- [static func acosh(Double) -> Angle2D](angle2d/acosh(_:).md)
  Returns the inverse hyperbolic cosine of the specified value.
- [static func asin(Double) -> Angle2D](angle2d/asin(_:).md)
  Returns the inverse sine of the specified value.
- [static func asinh(Double) -> Angle2D](angle2d/asinh(_:).md)
  Returns the inverse hyperbolic sine of the specified value.
- [static func atan(Double) -> Angle2D](angle2d/atan(_:).md)
  Returns the inverse hyperbolic tangent of the specified value.
- [static func atan2(y: Double, x: Double) -> Angle2D](angle2d/atan2(y:x:).md)
  Returns the two-argument arctangent of the specified values.
- [static func atanh(Double) -> Angle2D](angle2d/atanh(_:).md)
  Returns the inverse hyperbolic tangent of the specified value.
- [var normalized: Angle2D](angle2d/normalized.md)
  Returns the specified angle normalized between –180° and 180.0°.
### Comparing values
- [static func == (Angle2D, Angle2D) -> Bool](angle2d/==(_:_:).md)
  Returns a Boolean value that indicates whether two angles are equal.
### Encoding and decoding an angle structure
- [init(from: any Decoder) throws](angle2d/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](angle2d/encode(to:).md)
  Encodes this value into the given encoder.
### Applying arithmetic operations
- [static func + (Angle2D) -> Angle2D](angle2d/+(_:).md)
  Returns the given angle unchanged.
- [static func + (Angle2D, Angle2D) -> Angle2D](angle2d/+(_:_:).md)
  Adds two angles and produces their sum.
- [static func += (inout Angle2D, Angle2D)](angle2d/+=(_:_:).md)
  Adds two angles and stores the result in the left-hand-side variable.
- [static func - (Angle2D) -> Angle2D](angle2d/-(_:).md)
  Returns the additive inverse of the given angle.
- [static func - (Angle2D, Angle2D) -> Angle2D](angle2d/-(_:_:).md)
  Subtracts one angle from another and produces their difference.
- [static func -= (inout Angle2D, Angle2D)](angle2d/-=(_:_:).md)
  Subtracts the second angle from the first and stores the difference in the left-hand-side variable.
### Default Implementations
- [AdditiveArithmetic Implementations](angle2d/additivearithmetic-implementations.md)
- [CustomReflectable Implementations](angle2d/customreflectable-implementations.md)
- [Decodable Implementations](angle2d/decodable-implementations.md)
- [Encodable Implementations](angle2d/encodable-implementations.md)
- [Equatable Implementations](angle2d/equatable-implementations.md)
- [Hashable Implementations](angle2d/hashable-implementations.md)

## Relationships

### Conforms To
- [AdditiveArithmetic](../Swift/AdditiveArithmetic.md)
- [Animatable](../SwiftUI/Animatable.md)
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/angle2d)*