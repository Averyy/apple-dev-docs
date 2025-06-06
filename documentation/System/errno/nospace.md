# noSpace

**Framework**: System  
**Kind**: property

Device out of space.

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
static var noSpace: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

A write to an ordinary file, the creation of a directory or symbolic link, or the creation of a directory entry failed because there aren’t any available disk blocks on the file system, or the allocation of an inode for a newly created file failed because there aren’t any inodes available on the file system.

The corresponding C error is `ENOSPC`.

## See Also

- [static var badFileTypeOrFormat: Errno](errno/badfiletypeorformat.md)
  Inappropriate file type or format.
- [static var directoryNotEmpty: Errno](errno/directorynotempty.md)
  Directory not empty.
- [static var diskQuotaExceeded: Errno](errno/diskquotaexceeded.md)
  Disk quota exceeded.
- [static var readOnlyFileSystem: Errno](errno/readonlyfilesystem.md)
  Read-only file system.
- [static var tooManyLinks: Errno](errno/toomanylinks.md)
  Too many links.
- [static var tooManyOpenFilesInSystem: Errno](errno/toomanyopenfilesinsystem.md)
  The system has too many open files.
- [static var tooManyOpenFiles: Errno](errno/toomanyopenfiles.md)
  This process has too many open files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/nospace)*