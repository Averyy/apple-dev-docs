# append

**Framework**: System  
**Kind**: property  
**Role**: Type Property

Indicates that each write operation appends to the file.

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
static var append: FileDescriptor.OpenOptions { get }
```

## Mentions

- [Adopting Swift File Options](../../adopting-file-options.md)

#### Discussion

If this option is specified, each time you write to the file, the new data is written at the end of the file, after all existing file data.

The corresponding C constant is `O_APPEND`.

## See Also

### Specifying Options
- [static var closeOnExec: FileDescriptor.OpenOptions](./closeonexec.md)
  Indicates that executing a program closes the file.
- [static var create: FileDescriptor.OpenOptions](./create.md)
  Indicates that opening the file creates the file if it doesn’t exist.
- [static var eventOnly: FileDescriptor.OpenOptions](./eventonly.md)
  Indicates that opening the file monitors a file for changes.
- [static var exclusiveCreate: FileDescriptor.OpenOptions](./exclusivecreate.md)
  Indicates that opening the file creates the file, expecting that it doesn’t exist.
- [static var exclusiveLock: FileDescriptor.OpenOptions](./exclusivelock.md)
  Indicates that opening the file atomically obtains an exclusive lock.
- [static var noFollow: FileDescriptor.OpenOptions](./nofollow.md)
  Indicates that opening the file doesn’t follow symlinks.
- [static var nonBlocking: FileDescriptor.OpenOptions](./nonblocking.md)
  Indicates that opening the file doesn’t wait for the file or device to become available.
- [static var sharedLock: FileDescriptor.OpenOptions](./sharedlock.md)
  Indicates that opening the file atomically obtains a shared lock on the file.
- [static var symlink: FileDescriptor.OpenOptions](./symlink.md)
  Indicates that opening the file opens symbolic links instead of following them.
- [static var truncate: FileDescriptor.OpenOptions](./truncate.md)
  Indicates that opening the file truncates the file if it exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/openoptions/append)*