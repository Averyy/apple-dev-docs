# FileDescriptor.OpenOptions

**Framework**: System  
**Kind**: struct  
**Role**: Structure

Options that specify behavior for a newly-opened file.

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
struct OpenOptions
```

## Topics

### Specifying Options
- [static var append: FileDescriptor.OpenOptions](./openoptions/append.md)
  Indicates that each write operation appends to the file.
- [static var closeOnExec: FileDescriptor.OpenOptions](./openoptions/closeonexec.md)
  Indicates that executing a program closes the file.
- [static var create: FileDescriptor.OpenOptions](./openoptions/create.md)
  Indicates that opening the file creates the file if it doesn’t exist.
- [static var eventOnly: FileDescriptor.OpenOptions](./openoptions/eventonly.md)
  Indicates that opening the file monitors a file for changes.
- [static var exclusiveCreate: FileDescriptor.OpenOptions](./openoptions/exclusivecreate.md)
  Indicates that opening the file creates the file, expecting that it doesn’t exist.
- [static var exclusiveLock: FileDescriptor.OpenOptions](./openoptions/exclusivelock.md)
  Indicates that opening the file atomically obtains an exclusive lock.
- [static var noFollow: FileDescriptor.OpenOptions](./openoptions/nofollow.md)
  Indicates that opening the file doesn’t follow symlinks.
- [static var nonBlocking: FileDescriptor.OpenOptions](./openoptions/nonblocking.md)
  Indicates that opening the file doesn’t wait for the file or device to become available.
- [static var sharedLock: FileDescriptor.OpenOptions](./openoptions/sharedlock.md)
  Indicates that opening the file atomically obtains a shared lock on the file.
- [static var symlink: FileDescriptor.OpenOptions](./openoptions/symlink.md)
  Indicates that opening the file opens symbolic links instead of following them.
- [static var truncate: FileDescriptor.OpenOptions](./openoptions/truncate.md)
  Indicates that opening the file truncates the file if it exists.
### Interacting with C APIs
- [init(rawValue: CInt)](./openoptions/init%28rawvalue%29.md)
  Create a strongly-typed options value from raw C options.
- [var rawValue: CInt](./openoptions/rawvalue.md)
  The raw C options.
### Debugging
- [var description: String](./openoptions/description.md)
  A textual representation of the open options.
- [var debugDescription: String](./openoptions/debugdescription.md)
  A textual representation of the open options, suitable for debugging.
### Type Properties
- [static var directory: FileDescriptor.OpenOptions](./openoptions/directory.md)
  Indicates that opening the file only succeeds if the file is a directory.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./openoptions/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](./openoptions/customstringconvertible-implementations.md)

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
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [Hashable](../../Swift/hashable.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Opening a File
- [static func open(FilePath, FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions?, retryOnInterrupt: Bool) throws -> FileDescriptor](./open%28_,_,options,permissions,retryoninterrupt%29-4ql4b.md)
  Opens or creates a file for reading or writing.
- [static func open(UnsafePointer<CChar>, FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions?, retryOnInterrupt: Bool) throws -> FileDescriptor](./open%28_,_,options,permissions,retryoninterrupt%29-5t3xn.md)
  Opens or creates a file for reading or writing.
- [FileDescriptor.AccessMode](./accessmode.md)
  The desired read and write access for a newly opened file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/openoptions)*