# ByteOrder

**Framework**: Swift  
**Kind**: enum  
**Role**: Enumeration

A byte ordering in memory.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@frozen
enum ByteOrder
```

## Topics

### Operators
- [static func == (ByteOrder, ByteOrder) -> Bool](./byteorder/eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ByteOrder.bigEndian](./byteorder/bigendian.md)
  Bytes are ordered with the most significant bits starting at the lowest memory address.
- [ByteOrder.littleEndian](./byteorder/littleendian.md)
  Bytes are ordered with the least significant bits starting at the lowest memory address.
### Instance Properties
- [var hashValue: Int](./byteorder/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](./byteorder/hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static var native: ByteOrder](./byteorder/native.md)
  The native byte ordering for the runtime target.
### Default Implementations
- [Equatable Implementations](./byteorder/equatable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](./bitwisecopyable.md)
- [Copyable](./copyable.md)
- [Equatable](./equatable.md)
- [Hashable](./hashable.md)
- [Sendable](./sendable.md)
- [SendableMetatype](./sendablemetatype.md)

## See Also

### Safe Access to Raw Bytes
- [typealias FullyInhabited](./fullyinhabited.md)
  A protocol for types whose memory can safely be written as or read from raw bytes.
- [protocol ConvertibleFromBytes](./convertiblefrombytes.md)
  A protocol for types whose memory can safely be populated from raw bytes, resulting in a valid instance.
- [protocol ConvertibleToBytes](./convertibletobytes.md)
  A protocol for types whose memory can safely be read as individual raw bytes.
- [func bitCast<T, U>(T, to: U.Type) -> U](./bitcast%28_,to%29.md)
  Returns the bits of the given instance, interpreted as having the specified type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/byteorder)*