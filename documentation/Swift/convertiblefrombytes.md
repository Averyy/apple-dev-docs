# ConvertibleFromBytes

**Framework**: Swift  
**Kind**: protocol

A protocol for types whose memory can safely be populated from raw bytes, resulting in a valid instance.

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
protocol ConvertibleFromBytes : BitwiseCopyable
```

#### Overview

A type can conform to ConvertibleFromBytes if every bit pattern for every byte of its stored properties is valid. Note that this allows conformances for types with internal or trailing padding. A conformer to ConvertibleFromBytes must not have semantic constraints on the values of its stored properties. All its stored properties must themselves conform to ConvertibleFromBytes.

## Relationships

### Inherits From
- [BitwiseCopyable](bitwisecopyable.md)
### Conforming Types
- [CollectionOfOne](collectionofone.md)
- [Double](double.md)
- [Duration](duration.md)
- [Float](float.md)
- [Float16](float16.md)
- [Float80](float80.md)
- [InlineArray](inlinearray.md)
- [Int](int.md)
- [Int128](int128.md)
- [Int16](int16.md)
- [Int32](int32.md)
- [Int64](int64.md)
- [Int8](int8.md)
- [PartialRangeFrom](partialrangefrom.md)
- [PartialRangeFrom.Iterator](partialrangefrom/iterator.md)
- [PartialRangeThrough](partialrangethrough.md)
- [PartialRangeUpTo](partialrangeupto.md)
- [SIMD16](simd16.md)
- [SIMD2](simd2.md)
- [SIMD3](simd3.md)
- [SIMD32](simd32.md)
- [SIMD4](simd4.md)
- [SIMD64](simd64.md)
- [SIMD8](simd8.md)
- [UInt](uint.md)
- [UInt128](uint128.md)
- [UInt16](uint16.md)
- [UInt32](uint32.md)
- [UInt64](uint64.md)
- [UInt8](uint8.md)

## See Also

- [typealias FullyInhabited](fullyinhabited.md)
  A protocol for types whose memory can safely be written as or read from raw bytes.
- [protocol ConvertibleToBytes](convertibletobytes.md)
  A protocol for types whose memory can safely be read as individual raw bytes.
- [enum ByteOrder](byteorder.md)
  A byte ordering in memory.
- [func bitCast<T, U>(T, to: U.Type) -> U](bitcast(_:to:).md)
  Returns the bits of the given instance, interpreted as having the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/convertiblefrombytes)*