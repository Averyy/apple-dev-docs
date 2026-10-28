# textFileBusy

**Framework**: System  
**Kind**: property  
**Role**: Type Property

Text file busy.

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
static var textFileBusy: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](../adopting-errno.md)

## Discussion

The new process was a pure procedure (shared text) file, which was already open for writing by another process, or while the pure procedure file was being executed, an open call requested write access.

The corresponding C error is `ETXTBSY`.

## See Also

### File and Directory Errors
- [static var attributeNotFound: Errno](./attributenotfound.md)
  Attribute not found.
- [static var badFileDescriptor: Errno](./badfiledescriptor.md)
  Bad file descriptor.
- [static var fileExists: Errno](./fileexists.md)
  File exists.
- [static var fileTooLarge: Errno](./filetoolarge.md)
  The file is too large.
- [static var improperLink: Errno](./improperlink.md)
  Improper link.
- [static var isDirectory: Errno](./isdirectory.md)
  Is a directory.
- [static var noLocks: Errno](./nolocks.md)
  No locks available.
- [static var noSuchFileOrDirectory: Errno](./nosuchfileordirectory.md)
  No such file or directory.
- [static var notDirectory: Errno](./notdirectory.md)
  Not a directory.
- [static var permissionDenied: Errno](./permissiondenied.md)
  Permission denied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/textfilebusy)*