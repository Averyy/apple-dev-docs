# FileDescriptor.OpenOptions

**Framework**: System  
**Kind**: struct

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
- [static var append: FileDescriptor.OpenOptions](filedescriptor/openoptions/append.md)
  Indicates that each write operation appends to the file.
- [static var closeOnExec: FileDescriptor.OpenOptions](filedescriptor/openoptions/closeonexec.md)
  Indicates that executing a program closes the file.
- [static var create: FileDescriptor.OpenOptions](filedescriptor/openoptions/create.md)
  Indicates that opening the file creates the file if it doesn’t exist.
- [static var eventOnly: FileDescriptor.OpenOptions](filedescriptor/openoptions/eventonly.md)
  Indicates that opening the file monitors a file for changes.
- [static var exclusiveCreate: FileDescriptor.OpenOptions](filedescriptor/openoptions/exclusivecreate.md)
  Indicates that opening the file creates the file, expecting that it doesn’t exist.
- [static var exclusiveLock: FileDescriptor.OpenOptions](filedescriptor/openoptions/exclusivelock.md)
  Indicates that opening the file atomically obtains an exclusive lock.
- [static var noFollow: FileDescriptor.OpenOptions](filedescriptor/openoptions/nofollow.md)
  Indicates that opening the file doesn’t follow symlinks.
- [static var nonBlocking: FileDescriptor.OpenOptions](filedescriptor/openoptions/nonblocking.md)
  Indicates that opening the file doesn’t wait for the file or device to become available.
- [static var sharedLock: FileDescriptor.OpenOptions](filedescriptor/openoptions/sharedlock.md)
  Indicates that opening the file atomically obtains a shared lock on the file.
- [static var symlink: FileDescriptor.OpenOptions](filedescriptor/openoptions/symlink.md)
  Indicates that opening the file opens symbolic links instead of following them.
- [static var truncate: FileDescriptor.OpenOptions](filedescriptor/openoptions/truncate.md)
  Indicates that opening the file truncates the file if it exists.
### Interacting with C APIs
- [init(rawValue: CInt)](filedescriptor/openoptions/init(rawvalue:).md)
  Create a strongly-typed options value from raw C options.
- [var rawValue: CInt](filedescriptor/openoptions/rawvalue.md)
  The raw C options.
### Debugging
- [var description: String](filedescriptor/openoptions/description.md)
  A textual representation of the open options.
- [var debugDescription: String](filedescriptor/openoptions/debugdescription.md)
  A textual representation of the open options, suitable for debugging.
### Type Properties
- [static var directory: FileDescriptor.OpenOptions](filedescriptor/openoptions/directory.md)
  Indicates that opening the file only succeeds if the file is a directory.
### Default Implementations
- [CustomDebugStringConvertible Implementations](filedescriptor/openoptions/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](filedescriptor/openoptions/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [static func open(FilePath, FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions?, retryOnInterrupt: Bool) throws -> FileDescriptor](filedescriptor/open(_:_:options:permissions:retryoninterrupt:)-4ql4b.md)
  Opens or creates a file for reading or writing.
- [static func open(UnsafePointer<CChar>, FileDescriptor.AccessMode, options: FileDescriptor.OpenOptions, permissions: FilePermissions?, retryOnInterrupt: Bool) throws -> FileDescriptor](filedescriptor/open(_:_:options:permissions:retryoninterrupt:)-5t3xn.md)
  Opens or creates a file for reading or writing.
- [FileDescriptor.AccessMode](filedescriptor/accessmode.md)
  The desired read and write access for a newly opened file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/openoptions)*