# tooManyOpenFiles

**Framework**: System  
**Kind**: property  
**Role**: Type Property

This process has too many open files.

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
static var tooManyOpenFiles: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](../adopting-errno.md)

## Discussion

To check the current limit, call the `getdtablesize` function.

The corresponding C error is `EMFILE`.

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
- [static var tooManyLinks: Errno](./toomanylinks.md)
  Too many links.
- [static var tooManyOpenFilesInSystem: Errno](./toomanyopenfilesinsystem.md)
  The system has too many open files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/toomanyopenfiles)*