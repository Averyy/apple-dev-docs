# FileDescriptor.SeekOrigin

**Framework**: System  
**Kind**: struct

Options for specifying what a file descriptor’s offset is relative to.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@frozen
struct SeekOrigin
```

## Topics

### Creating a Seek Origin
- [static var current: FileDescriptor.SeekOrigin](filedescriptor/seekorigin/current.md)
  Indicates that the offset should be set to the specified number of bytes after the current location.
- [static var end: FileDescriptor.SeekOrigin](filedescriptor/seekorigin/end.md)
  Indicates that the offset should be set to the size of the file plus the specified number of bytes.
- [static var nextHole: FileDescriptor.SeekOrigin](filedescriptor/seekorigin/nexthole.md)
  Indicates that the offset should be set to the next hole after the specified number of bytes.
- [static var nextData: FileDescriptor.SeekOrigin](filedescriptor/seekorigin/nextdata.md)
  Indicates that the offset should be set to the start of the next file region that isn’t a hole and is greater than or equal to the supplied offset.
- [static var start: FileDescriptor.SeekOrigin](filedescriptor/seekorigin/start.md)
  Indicates that the offset should be set to the specified value.
### Debugging
- [var description: String](filedescriptor/seekorigin/description.md)
  A textual representation of the seek origin.
- [var debugDescription: String](filedescriptor/seekorigin/debugdescription.md)
  A textual representation of the seek origin, suitable for debugging.
### Working with C APIs
- [init(rawValue: CInt)](filedescriptor/seekorigin/init(rawvalue:).md)
  Create a strongly-typed seek origin from a raw C value.
- [var rawValue: CInt](filedescriptor/seekorigin/rawvalue-swift.property.md)
  The raw C value.
- [FileDescriptor.SeekOrigin.RawValue](filedescriptor/seekorigin/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Comparing Seek Origins
- [static func != (Self, Self) -> Bool](filedescriptor/seekorigin/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [func hash(into: inout Hasher)](filedescriptor/seekorigin/hash(into:).md)
- [var hashValue: Int](filedescriptor/seekorigin/hashvalue.md)
### Encoding Seek Origins
- [func encode(to: any Encoder) throws](filedescriptor/seekorigin/encode(to:).md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int32`.
- [init(from: any Decoder) throws](filedescriptor/seekorigin/init(from:).md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int32`.
### Default Implementations
- [CustomDebugStringConvertible Implementations](filedescriptor/seekorigin/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](filedescriptor/seekorigin/customstringconvertible-implementations.md)
- [Equatable Implementations](filedescriptor/seekorigin/equatable-implementations.md)
- [RawRepresentable Implementations](filedescriptor/seekorigin/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func seek(offset: Int64, from: FileDescriptor.SeekOrigin) throws -> Int64](filedescriptor/seek(offset:from:).md)
  Repositions the offset for the given file descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/seekorigin)*