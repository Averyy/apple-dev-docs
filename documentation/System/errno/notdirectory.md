# notDirectory

**Framework**: System  
**Kind**: property

Not a directory.

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
static var notDirectory: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

A component of the specified pathname exists, but it wasn’t a directory, when a directory was expected.

The corresponding C error is `ENOTDIR`.

## See Also

- [static var attributeNotFound: Errno](errno/attributenotfound.md)
  Attribute not found.
- [static var badFileDescriptor: Errno](errno/badfiledescriptor.md)
  Bad file descriptor.
- [static var fileExists: Errno](errno/fileexists.md)
  File exists.
- [static var fileTooLarge: Errno](errno/filetoolarge.md)
  The file is too large.
- [static var improperLink: Errno](errno/improperlink.md)
  Improper link.
- [static var isDirectory: Errno](errno/isdirectory.md)
  Is a directory.
- [static var noLocks: Errno](errno/nolocks.md)
  No locks available.
- [static var noSuchFileOrDirectory: Errno](errno/nosuchfileordirectory.md)
  No such file or directory.
- [static var permissionDenied: Errno](errno/permissiondenied.md)
  Permission denied.
- [static var textFileBusy: Errno](errno/textfilebusy.md)
  Text file busy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/notdirectory)*