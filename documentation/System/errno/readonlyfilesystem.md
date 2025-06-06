# readOnlyFileSystem

**Framework**: System  
**Kind**: property

Read-only file system.

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
static var readOnlyFileSystem: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

You attempted to modify a file or directory on a file system that was read-only at the time.

The corresponding C error is `EROFS`.

## See Also

- [static var badFileTypeOrFormat: Errno](errno/badfiletypeorformat.md)
  Inappropriate file type or format.
- [static var directoryNotEmpty: Errno](errno/directorynotempty.md)
  Directory not empty.
- [static var diskQuotaExceeded: Errno](errno/diskquotaexceeded.md)
  Disk quota exceeded.
- [static var noSpace: Errno](errno/nospace.md)
  Device out of space.
- [static var tooManyLinks: Errno](errno/toomanylinks.md)
  Too many links.
- [static var tooManyOpenFilesInSystem: Errno](errno/toomanyopenfilesinsystem.md)
  The system has too many open files.
- [static var tooManyOpenFiles: Errno](errno/toomanyopenfiles.md)
  This process has too many open files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/readonlyfilesystem)*