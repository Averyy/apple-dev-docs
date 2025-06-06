# SignedInteger

**Framework**: Swift  
**Kind**: protocol

An integer type that can represent both positive and negative values.

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
protocol SignedInteger : BinaryInteger, SignedNumeric
```

## Topics

### Instance Methods
- [func dividingFullWidth((high: Self, low: Self.Magnitude)) -> (quotient: Self, remainder: Self)](signedinteger/dividingfullwidth(_:).md)
### Type Properties
- [static var max: Self](signedinteger/max.md)
  The maximum representable integer in this type.
- [static var min: Self](signedinteger/min.md)
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
- [SignedNumeric](signednumeric.md)
- [Strideable](strideable.md)
### Conforming Types
- [Int](int.md)
- [Int128](int128.md)
- [Int16](int16.md)
- [Int32](int32.md)
- [Int64](int64.md)
- [Int8](int8.md)

## See Also

- [protocol BinaryInteger](binaryinteger.md)
  An integer type with a binary representation.
- [protocol FixedWidthInteger](fixedwidthinteger.md)
  An integer type that uses a fixed size for every instance.
- [protocol UnsignedInteger](unsignedinteger.md)
  An integer type that can represent only nonnegative values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/signedinteger)*