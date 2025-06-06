# UnsignedInteger

**Framework**: Swift  
**Kind**: protocol

An integer type that can represent only nonnegative values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol UnsignedInteger : BinaryInteger
```

## Topics

### Instance Methods
- [func dividingFullWidth((high: Self, low: Self.Magnitude)) -> (quotient: Self, remainder: Self)](unsignedinteger/dividingfullwidth(_:).md)
### Type Properties
- [static var max: Self](unsignedinteger/max.md)
  The maximum representable integer in this type.
- [static var min: Self](unsignedinteger/min.md)
  The minimum representable integer in this type.

## Relationships

### Inherits From
- [AdditiveArithmetic](additivearithmetic.md)
- [BinaryInteger](binaryinteger.md)
- [Comparable](comparable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [Equatable](equatable.md)
- [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md)
- [Hashable](hashable.md)
- [Numeric](numeric.md)
- [Strideable](strideable.md)
### Conforming Types
- [UInt](uint.md)
- [UInt128](uint128.md)
- [UInt16](uint16.md)
- [UInt32](uint32.md)
- [UInt64](uint64.md)
- [UInt8](uint8.md)

## See Also

- [protocol BinaryInteger](binaryinteger.md)
  An integer type with a binary representation.
- [protocol FixedWidthInteger](fixedwidthinteger.md)
  An integer type that uses a fixed size for every instance.
- [protocol SignedInteger](signedinteger.md)
  An integer type that can represent both positive and negative values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsignedinteger)*