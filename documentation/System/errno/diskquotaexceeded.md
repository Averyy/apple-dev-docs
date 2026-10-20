# diskQuotaExceeded

**Framework**: System  
**Kind**: property  
**Role**: Type Property

Disk quota exceeded.

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
static var diskQuotaExceeded: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](../adopting-errno.md)

#### Discussion

A write to an ordinary file, the creation of a directory or symbolic link, or the creation of a directory entry failed because the user’s quota of disk blocks was exhausted, or the allocation of an inode for a newly created file failed because the user’s quota of inodes was exhausted.

The corresponding C error is `EDQUOT`.

## See Also

### File System Errors
- [static var badFileTypeOrFormat: Errno](./badfiletypeorformat.md)
  Inappropriate file type or format.
- [static var directoryNotEmpty: Errno](./directorynotempty.md)
  Directory not empty.
- [static var noSpace: Errno](./nospace.md)
  Device out of space.
- [static var readOnlyFileSystem: Errno](./readonlyfilesystem.md)
  Read-only file system.
- [static var tooManyLinks: Errno](./toomanylinks.md)
  Too many links.
- [static var tooManyOpenFilesInSystem: Errno](./toomanyopenfilesinsystem.md)
  The system has too many open files.
- [static var tooManyOpenFiles: Errno](./toomanyopenfiles.md)
  This process has too many open files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/diskquotaexceeded)*