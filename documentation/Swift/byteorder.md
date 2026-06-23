# ByteOrder

**Framework**: Swift  
**Kind**: enum

A byte ordering in memory.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
@frozen
enum ByteOrder
```

## Topics

### Operators
- [static func == (ByteOrder, ByteOrder) -> Bool](byteorder/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ByteOrder.bigEndian](byteorder/bigendian.md)
  Bytes are ordered with the most significant bits starting at the lowest memory address.
- [ByteOrder.littleEndian](byteorder/littleendian.md)
  Bytes are ordered with the least significant bits starting at the lowest memory address.
### Instance Properties
- [var hashValue: Int](byteorder/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](byteorder/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static var native: ByteOrder](byteorder/native.md)
  The native byte ordering for the runtime target.
### Default Implementations
- [Equatable Implementations](byteorder/equatable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [Copyable](copyable.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/byteorder)*