# FileDescriptor.AccessMode

**Framework**: System  
**Kind**: struct  
**Role**: Structure

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
- [static var readOnly: FileDescriptor.AccessMode](./accessmode/readonly.md)
  Opens the file for reading only.
- [static var readWrite: FileDescriptor.AccessMode](./accessmode/readwrite.md)
  Opens the file for reading and writing.
- [static var writeOnly: FileDescriptor.AccessMode](./accessmode/writeonly.md)
  Opens the file for writing only.
### Debugging
- [var description: String](./accessmode/description.md)
  A textual representation of the access mode.
- [var debugDescription: String](./accessmode/debugdescription.md)
  A textual representation of the access mode, suitable for debugging
### Working with C APIs
- [init(rawValue: CInt)](./accessmode/init%28rawvalue%29.md)
  Creates a strongly-typed access mode from a raw C access mode.
- [var rawValue: CInt](./accessmode/rawvalue.md)
  The raw C access mode.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./accessmode/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](./accessmode/customstringconvertible-implementations.md)

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

### Opening a File
- [static func open(FilePath, FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions?, retryOnInterrupt: Bool) throws -> FileDescriptor](./open%28_,_,options,permissions,retryoninterrupt%29-4ql4b.md)
  Opens or creates a file for reading or writing.
- [static func open(UnsafePointer<CChar>, FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions?, retryOnInterrupt: Bool) throws -> FileDescriptor](./open%28_,_,options,permissions,retryoninterrupt%29-5t3xn.md)
  Opens or creates a file for reading or writing.
- [FileDescriptor.OpenOptions](./openoptions.md)
  Options that specify behavior for a newly-opened file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/accessmode)*