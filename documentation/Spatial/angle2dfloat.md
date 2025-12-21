# Angle2DFloat

**Framework**: Spatial  
**Kind**: struct

A single-precision geometric angle whose value you access in either radians or degrees.

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
struct Angle2DFloat
```

## Topics

### Operators
- [static func + (Angle2DFloat) -> Angle2DFloat](angle2dfloat/+(_:).md)
  Returns the given angle unchanged.
- [static func - (Angle2DFloat) -> Angle2DFloat](angle2dfloat/-(_:).md)
  Returns the additive inverse of the specified angle.
### Initializers
- [init()](angle2dfloat/init.md)
- [init(Angle2D)](angle2dfloat/init(_:).md)
  Returns a single-precision angle from a double-precision angle.
- [init<T>(degrees: T)](angle2dfloat/init(degrees:)-2mulz.md)
  Returns a new angle from floating-point degrees.
- [init(degrees: Float)](angle2dfloat/init(degrees:)-56b20.md)
- [init(radians: Float)](angle2dfloat/init(radians:)-4uwyj.md)
- [init<T>(radians: T)](angle2dfloat/init(radians:)-9r8ja.md)
  Returns a new angle from floating-point radians.
- [init(radians: Float)](angle2dfloat/init(radians:)-9ri4z.md)
### Instance Properties
- [var degrees: Float](angle2dfloat/degrees.md)
- [var normalized: Angle2DFloat](angle2dfloat/normalized.md)
  Returns the specified angle normalized to `(-π, π]` radians (`(-180°, 180.0°]`).
- [var radians: Float](angle2dfloat/radians.md)
  The angle in radians.
### Type Methods
- [static func acos(Float) -> Angle2DFloat](angle2dfloat/acos(_:).md)
- [static func acosh(Float) -> Angle2DFloat](angle2dfloat/acosh(_:).md)
- [static func asin(Float) -> Angle2DFloat](angle2dfloat/asin(_:).md)
- [static func asinh(Float) -> Angle2DFloat](angle2dfloat/asinh(_:).md)
- [static func atan(Float) -> Angle2DFloat](angle2dfloat/atan(_:).md)
- [static func atan2(y: Float, x: Float) -> Angle2DFloat](angle2dfloat/atan2(y:x:).md)
- [static func atanh(Float) -> Angle2DFloat](angle2dfloat/atanh(_:).md)
- [static func degrees(Float) -> Angle2DFloat](angle2dfloat/degrees(_:).md)
- [static func radians(Float) -> Angle2DFloat](angle2dfloat/radians(_:).md)
### Default Implementations
- [AdditiveArithmetic Implementations](angle2dfloat/additivearithmetic-implementations.md)
- [Comparable Implementations](angle2dfloat/comparable-implementations.md)
- [CustomReflectable Implementations](angle2dfloat/customreflectable-implementations.md)
- [Decodable Implementations](angle2dfloat/decodable-implementations.md)
- [Encodable Implementations](angle2dfloat/encodable-implementations.md)
- [Equatable Implementations](angle2dfloat/equatable-implementations.md)
- [Hashable Implementations](angle2dfloat/hashable-implementations.md)

## Relationships

### Conforms To
- [AdditiveArithmetic](../Swift/AdditiveArithmetic.md)
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct Angle2D](angle2d.md)
  A geometric angle with a value you access in either radians or degrees.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/angle2dfloat)*