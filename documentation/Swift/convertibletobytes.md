# ConvertibleToBytes

**Framework**: Swift  
**Kind**: protocol

A protocol for types whose memory can safely be read as individual raw bytes.

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
protocol ConvertibleToBytes
```

#### Overview

A type can conform to ConvertibleToBytes if its memory representation includes no padding. The sum of the size of its stored properties must be equal to its stride.

A type that conforms to ConvertibleToBytes must have:

- one or more stored properties,
- all of its stored properties have a type which conforms to `ConvertibleToBytes`,
- its stored properties are stored contiguously in memory, with no padding,
- none of its values disregards a subset of its bytes, making most enums ineligible.

## Relationships

### Conforming Types
- [Bool](bool.md)
- [ClosedRange](closedrange.md)
- [CollectionOfOne](collectionofone.md)
- [Double](double.md)
- [Duration](duration.md)
- [Float](float.md)
- [Float16](float16.md)
- [InlineArray](inlinearray.md)
- [Int](int.md)
- [Int128](int128.md)
- [Int16](int16.md)
- [Int32](int32.md)
- [Int64](int64.md)
- [Int8](int8.md)
- [ObjectIdentifier](objectidentifier.md)
- [OpaquePointer](opaquepointer.md)
- [PartialRangeFrom](partialrangefrom.md)
- [PartialRangeFrom.Iterator](partialrangefrom/iterator.md)
- [PartialRangeThrough](partialrangethrough.md)
- [PartialRangeUpTo](partialrangeupto.md)
- [Range](range.md)
- [UInt](uint.md)
- [UInt128](uint128.md)
- [UInt16](uint16.md)
- [UInt32](uint32.md)
- [UInt64](uint64.md)
- [UInt8](uint8.md)
- [UnsafeBufferPointer](unsafebufferpointer.md)
- [UnsafeMutableBufferPointer](unsafemutablebufferpointer.md)
- [UnsafeMutablePointer](unsafemutablepointer.md)
- [UnsafeMutableRawBufferPointer](unsafemutablerawbufferpointer.md)
- [UnsafeMutableRawPointer](unsafemutablerawpointer.md)
- [UnsafePointer](unsafepointer.md)
- [UnsafeRawBufferPointer](unsaferawbufferpointer.md)
- [UnsafeRawPointer](unsaferawpointer.md)

## See Also

- [typealias FullyInhabited](fullyinhabited.md)
  A protocol for types whose memory can safely be written as or read from raw bytes.
- [protocol ConvertibleFromBytes](convertiblefrombytes.md)
  A protocol for types whose memory can safely be populated from raw bytes, resulting in a valid instance.
- [enum ByteOrder](byteorder.md)
  A byte ordering in memory.
- [func bitCast<T, U>(T, to: U.Type) -> U](bitcast(_:to:).md)
  Returns the bits of the given instance, interpreted as having the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/convertibletobytes)*