# nonBlocking

**Framework**: System  
**Kind**: property

Indicates that opening the file doesn’t wait for the file or device to become available.

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
static var nonBlocking: FileDescriptor.OpenOptions { get }
```

## Mentions

- [Adopting Swift File Options](adopting-file-options.md)

#### Discussion

If this option is specified, the system doesn’t wait for the device or file to be ready or available. If the doc:FileDescriptor/open(_:_:options:permissions:retryOnInterrupt:)-2266j call would result in the process being blocked for some reason, that method returns immediately. This flag also has the effect of making all subsequent input and output operations on the open file nonblocking.

The corresponding C constant is `O_NONBLOCK`.

## See Also

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
- [static var sharedLock: FileDescriptor.OpenOptions](filedescriptor/openoptions/sharedlock.md)
  Indicates that opening the file atomically obtains a shared lock on the file.
- [static var symlink: FileDescriptor.OpenOptions](filedescriptor/openoptions/symlink.md)
  Indicates that opening the file opens symbolic links instead of following them.
- [static var truncate: FileDescriptor.OpenOptions](filedescriptor/openoptions/truncate.md)
  Indicates that opening the file truncates the file if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/openoptions/nonblocking)*