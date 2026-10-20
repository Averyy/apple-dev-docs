# Angle2D

**Framework**: Spatial  
**Kind**: struct  
**Role**: Structure

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

```c
typedef struct { ... } SPAngle;
```

## Topics

### Creating an angle structure
- [init()](./angle2d/init%28%29.md)
  Creates an angle.
- [init(radians: Double)](./angle2d/init%28radians%29-3zcwo.md)
  Creates an angle with the specified double-precision radians.
- [init(radians: Double)](./angle2d/init%28radians%29-6s7o6.md)
  Creates an angle with the specified double-precision radians.
- [init<T>(radians: T)](./angle2d/init%28radians%29-74ym2.md)
  Creates an angle with the specified floating-point radians.
- [init<T>(degrees: T)](./angle2d/init%28degrees%29-2obd.md)
  Creates an angle with the specified floating-point degrees.
- [init(degrees: Double)](./angle2d/init%28degrees%29-7y9lb.md)
  Creates an angle with the specified double-precision degrees.
- [static func degrees(Double) -> Angle2D](./angle2d/degrees%28_%29.md)
  Returns a new angle structure with the specified double-precision degrees.
- [static func radians(Double) -> Angle2D](./angle2d/radians%28_%29.md)
  Returns a new angle structure with the specified double-precision radians.
### Inspecting an angle’s properties
- [var degrees: Double](./angle2d/degrees.md)
  The angle in degrees.
- [var radians: Double](./angle2d/radians.md)
  The angle in radians.
### Geometry functions
- [static func acos(Double) -> Angle2D](./angle2d/acos%28_%29.md)
  Returns the inverse cosine of the specified value.
- [static func acosh(Double) -> Angle2D](./angle2d/acosh%28_%29.md)
  Returns the inverse hyperbolic cosine of the specified value.
- [static func asin(Double) -> Angle2D](./angle2d/asin%28_%29.md)
  Returns the inverse sine of the specified value.
- [static func asinh(Double) -> Angle2D](./angle2d/asinh%28_%29.md)
  Returns the inverse hyperbolic sine of the specified value.
- [static func atan(Double) -> Angle2D](./angle2d/atan%28_%29.md)
  Returns the inverse hyperbolic tangent of the specified value.
- [static func atan2(y: Double, x: Double) -> Angle2D](./angle2d/atan2%28y,x%29.md)
  Returns the two-argument arctangent of the specified values.
- [static func atanh(Double) -> Angle2D](./angle2d/atanh%28_%29.md)
  Returns the inverse hyperbolic tangent of the specified value.
- [var normalized: Angle2D](./angle2d/normalized.md)
  Returns the specified angle normalized between –180° and 180.0°.
### Comparing values
- [static func == (Angle2D, Angle2D) -> Bool](./angle2d/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two angles are equal.
### Encoding and decoding an angle structure
- [init(from: any Decoder) throws](./angle2d/init%28from%29.md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](./angle2d/encode%28to%29.md)
  Encodes this value into the given encoder.
### Applying arithmetic operations
- [static func + (Angle2D) -> Angle2D](./angle2d/plus%28_%29.md)
  Returns the given angle unchanged.
- [static func + (Angle2D, Angle2D) -> Angle2D](./angle2d/plus%28_,_%29.md)
  Adds two angles and produces their sum.
- [static func += (inout Angle2D, Angle2D)](./angle2d/pluseq%28_,_%29.md)
  Adds two angles and stores the result in the left-hand-side variable.
- [static func - (Angle2D) -> Angle2D](./angle2d/minus%28_%29.md)
  Returns the additive inverse of the given angle.
- [static func - (Angle2D, Angle2D) -> Angle2D](./angle2d/minus%28_,_%29.md)
  Subtracts one angle from another and produces their difference.
- [static func -= (inout Angle2D, Angle2D)](./angle2d/minuseq%28_,_%29.md)
  Subtracts the second angle from the first and stores the difference in the left-hand-side variable.
### Initializers
- [init(Angle)](./angle2d/init%28_%29-44cs8.md)
- [init(Angle2DFloat)](./angle2d/init%28_%29-7nf6j.md)
  Returns a double-precision angle from a single-precision angle.
### Default Implementations
- [AdditiveArithmetic Implementations](./angle2d/additivearithmetic-implementations.md)
- [Comparable Implementations](./angle2d/comparable-implementations.md)
- [CustomReflectable Implementations](./angle2d/customreflectable-implementations.md)
- [Decodable Implementations](./angle2d/decodable-implementations.md)
- [Encodable Implementations](./angle2d/encodable-implementations.md)
- [Equatable Implementations](./angle2d/equatable-implementations.md)
- [Hashable Implementations](./angle2d/hashable-implementations.md)

## Relationships

### Conforms To
- [AdditiveArithmetic](../Swift/additivearithmetic.md)
- [Animatable](../SwiftUI/animatable.md)
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Comparable](../Swift/comparable.md)
- [Copyable](../Swift/copyable.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### 2D primitives
- [struct Angle2DFloat](./angle2dfloat.md)
  A single-precision geometric angle whose value you access in either radians or degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/angle2d)*