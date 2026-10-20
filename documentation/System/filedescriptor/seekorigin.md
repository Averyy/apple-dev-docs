# FileDescriptor.SeekOrigin

**Framework**: System  
**Kind**: struct  
**Role**: Structure

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
- [static var current: FileDescriptor.SeekOrigin](./seekorigin/current.md)
  Indicates that the offset should be set to the specified number of bytes after the current location.
- [static var end: FileDescriptor.SeekOrigin](./seekorigin/end.md)
  Indicates that the offset should be set to the size of the file plus the specified number of bytes.
- [static var nextHole: FileDescriptor.SeekOrigin](./seekorigin/nexthole.md)
  Indicates that the offset should be set to the next hole after the specified number of bytes.
- [static var nextData: FileDescriptor.SeekOrigin](./seekorigin/nextdata.md)
  Indicates that the offset should be set to the start of the next file region that isn’t a hole and is greater than or equal to the supplied offset.
- [static var start: FileDescriptor.SeekOrigin](./seekorigin/start.md)
  Indicates that the offset should be set to the specified value.
### Debugging
- [var description: String](./seekorigin/description.md)
  A textual representation of the seek origin.
- [var debugDescription: String](./seekorigin/debugdescription.md)
  A textual representation of the seek origin, suitable for debugging.
### Working with C APIs
- [init(rawValue: CInt)](./seekorigin/init%28rawvalue%29.md)
  Create a strongly-typed seek origin from a raw C value.
- [var rawValue: CInt](./seekorigin/rawvalue.md)
  The raw C value.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./seekorigin/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](./seekorigin/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Changing a File’s Offset
- [func seek(offset: Int64, from: FileDescriptor.SeekOrigin) throws -> Int64](./seek%28offset,from%29.md)
  Repositions the offset for the given file descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/seekorigin)*