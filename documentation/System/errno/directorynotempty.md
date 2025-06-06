# directoryNotEmpty

**Framework**: System  
**Kind**: property

Directory not empty.

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
static var directoryNotEmpty: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

A directory with entries other than `.` and `..` was supplied to a `remove(2)` directory or `rename(2)` call.

The corresponding C error is `ENOTEMPTY`.

## See Also

- [static var badFileTypeOrFormat: Errno](errno/badfiletypeorformat.md)
  Inappropriate file type or format.
- [static var diskQuotaExceeded: Errno](errno/diskquotaexceeded.md)
  Disk quota exceeded.
- [static var noSpace: Errno](errno/nospace.md)
  Device out of space.
- [static var readOnlyFileSystem: Errno](errno/readonlyfilesystem.md)
  Read-only file system.
- [static var tooManyLinks: Errno](errno/toomanylinks.md)
  Too many links.
- [static var tooManyOpenFilesInSystem: Errno](errno/toomanyopenfilesinsystem.md)
  The system has too many open files.
- [static var tooManyOpenFiles: Errno](errno/toomanyopenfiles.md)
  This process has too many open files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/directorynotempty)*