# tooManyLinks

**Framework**: System  
**Kind**: property  
**Role**: Type Property

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

- [Adopting Swift Error Constants](../adopting-errno.md)

## Discussion

The maximum number of hard links to a single file (32767) has been exceeded.

The corresponding C error is `EMLINK`.

## See Also

### File System Errors
- [static var badFileTypeOrFormat: Errno](./badfiletypeorformat.md)
  Inappropriate file type or format.
- [static var directoryNotEmpty: Errno](./directorynotempty.md)
  Directory not empty.
- [static var diskQuotaExceeded: Errno](./diskquotaexceeded.md)
  Disk quota exceeded.
- [static var noSpace: Errno](./nospace.md)
  Device out of space.
- [static var readOnlyFileSystem: Errno](./readonlyfilesystem.md)
  Read-only file system.
- [static var tooManyOpenFilesInSystem: Errno](./toomanyopenfilesinsystem.md)
  The system has too many open files.
- [static var tooManyOpenFiles: Errno](./toomanyopenfiles.md)
  This process has too many open files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/toomanylinks)*