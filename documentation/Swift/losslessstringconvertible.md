# LosslessStringConvertible

**Framework**: Swift  
**Kind**: protocol

A type that can be represented as a string in a lossless, unambiguous way.

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
protocol LosslessStringConvertible : CustomStringConvertible
```

#### Overview

For example, the integer value 1050 can be represented in its entirety as the string “1050”.

The description property of a conforming type must be a value-preserving representation of the original value. As such, it should be possible to re-create an instance from its string representation.

## Topics

### Initializers
- [init?(String)](losslessstringconvertible/init(_:).md)
  Instantiates an instance of the conforming type from a string representation.

## Relationships

### Inherits From
- [CustomStringConvertible](customstringconvertible.md)
### Inherited By
- [FixedWidthInteger](fixedwidthinteger.md)
- [StringProtocol](stringprotocol.md)
### Conforming Types
- [Bool](bool.md)
- [Character](character.md)
- [Double](double.md)
- [Float](float.md)
- [Float16](float16.md)
- [Float80](float80.md)
- [Int](int.md)
- [Int128](int128.md)
- [Int16](int16.md)
- [Int32](int32.md)
- [Int64](int64.md)
- [Int8](int8.md)
- [String](string.md)
- [Substring](substring.md)
- [UInt](uint.md)
- [UInt128](uint128.md)
- [UInt16](uint16.md)
- [UInt32](uint32.md)
- [UInt64](uint64.md)
- [UInt8](uint8.md)
- [Unicode.Scalar](unicode/scalar.md)

## See Also

- [protocol CustomStringConvertible](customstringconvertible.md)
  A type with a customized textual representation.
- [protocol CustomDebugStringConvertible](customdebugstringconvertible.md)
  A type with a customized textual representation suitable for debugging purposes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/losslessstringconvertible)*