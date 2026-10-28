# exclusiveCreate

**Framework**: System  
**Kind**: property  
**Role**: Type Property

Indicates that opening the file creates the file, expecting that it doesn’t exist.

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
static var exclusiveCreate: FileDescriptor.OpenOptions { get }
```

## Mentions

- [Adopting Swift File Options](../../adopting-file-options.md)

## Discussion

If this option and [`create`](./create.md) are both specified and the file exists, doc:FileDescriptor/open(_:_:options:permissions:retryOnInterrupt:)-2266j returns an error instead of creating the file. You can use this, for example, to implement a simple exclusive-access locking mechanism.

If this option and [`create`](./create.md) are both specified and the last component of the file’s path is a symbolic link, doc:FileDescriptor/open(_:_:options:permissions:retryOnInterrupt:)-2266j fails even if the symbolic link points to a nonexistent name.

The corresponding C constant is `O_EXCL`.

## See Also

### Specifying Options
- [static var append: FileDescriptor.OpenOptions](./append.md)
  Indicates that each write operation appends to the file.
- [static var closeOnExec: FileDescriptor.OpenOptions](./closeonexec.md)
  Indicates that executing a program closes the file.
- [static var create: FileDescriptor.OpenOptions](./create.md)
  Indicates that opening the file creates the file if it doesn’t exist.
- [static var eventOnly: FileDescriptor.OpenOptions](./eventonly.md)
  Indicates that opening the file monitors a file for changes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/openoptions/exclusivecreate)*