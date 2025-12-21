# FileDescriptor.AccessMode

**Framework**: System  
**Kind**: struct

The desired read and write access for a newly opened file.

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
struct AccessMode
```

## Topics

### Creating an Access Mode
- [static var readOnly: FileDescriptor.AccessMode](filedescriptor/accessmode/readonly.md)
  Opens the file for reading only.
- [static var readWrite: FileDescriptor.AccessMode](filedescriptor/accessmode/readwrite.md)
  Opens the file for reading and writing.
- [static var writeOnly: FileDescriptor.AccessMode](filedescriptor/accessmode/writeonly.md)
  Opens the file for writing only.
### Debugging
- [var description: String](filedescriptor/accessmode/description.md)
  A textual representation of the access mode.
- [var debugDescription: String](filedescriptor/accessmode/debugdescription.md)
  A textual representation of the access mode, suitable for debugging
### Working with C APIs
- [init(rawValue: CInt)](filedescriptor/accessmode/init(rawvalue:).md)
  Creates a strongly-typed access mode from a raw C access mode.
- [var rawValue: CInt](filedescriptor/accessmode/rawvalue.md)
  The raw C access mode.
### Default Implementations
- [CustomDebugStringConvertible Implementations](filedescriptor/accessmode/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](filedescriptor/accessmode/customstringconvertible-implementations.md)

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

- [static func open(FilePath, FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions?, retryOnInterrupt: Bool) throws -> FileDescriptor](filedescriptor/open(_:_:options:permissions:retryoninterrupt:)-4ql4b.md)
  Opens or creates a file for reading or writing.
- [static func open(UnsafePointer<CChar>, FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions?, retryOnInterrupt: Bool) throws -> FileDescriptor](filedescriptor/open(_:_:options:permissions:retryoninterrupt:)-5t3xn.md)
  Opens or creates a file for reading or writing.
- [FileDescriptor.OpenOptions](filedescriptor/openoptions.md)
  Options that specify behavior for a newly-opened file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/accessmode)*