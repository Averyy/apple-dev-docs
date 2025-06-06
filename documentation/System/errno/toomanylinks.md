# tooManyLinks

**Framework**: System  
**Kind**: property

Too many links.

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
static var tooManyLinks: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

The maximum number of hard links to a single file (32767) has been exceeded.

The corresponding C error is `EMLINK`.

## See Also

- [static var badFileTypeOrFormat: Errno](errno/badfiletypeorformat.md)
  Inappropriate file type or format.
- [static var directoryNotEmpty: Errno](errno/directorynotempty.md)
  Directory not empty.
- [static var diskQuotaExceeded: Errno](errno/diskquotaexceeded.md)
  Disk quota exceeded.
- [static var noSpace: Errno](errno/nospace.md)
  Device out of space.
- [static var readOnlyFileSystem: Errno](errno/readonlyfilesystem.md)
  Read-only file system.
- [static var tooManyOpenFilesInSystem: Errno](errno/toomanyopenfilesinsystem.md)
  The system has too many open files.
- [static var tooManyOpenFiles: Errno](errno/toomanyopenfiles.md)
  This process has too many open files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/toomanylinks)*