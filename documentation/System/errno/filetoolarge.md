# fileTooLarge

**Framework**: System  
**Kind**: property

The file is too large.

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
static var fileTooLarge: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](adopting-errno.md)

#### Discussion

The file exceeds the maximum size allowed by the file system. For example, the maximum size on UFS is about 2.1 gigabytes, and about 9,223 petabytes on HFS-Plus and Apple File System.

The corresponding C error is `EFBIG`.

## See Also

- [static var attributeNotFound: Errno](errno/attributenotfound.md)
  Attribute not found.
- [static var badFileDescriptor: Errno](errno/badfiledescriptor.md)
  Bad file descriptor.
- [static var fileExists: Errno](errno/fileexists.md)
  File exists.
- [static var improperLink: Errno](errno/improperlink.md)
  Improper link.
- [static var isDirectory: Errno](errno/isdirectory.md)
  Is a directory.
- [static var noLocks: Errno](errno/nolocks.md)
  No locks available.
- [static var noSuchFileOrDirectory: Errno](errno/nosuchfileordirectory.md)
  No such file or directory.
- [static var notDirectory: Errno](errno/notdirectory.md)
  Not a directory.
- [static var permissionDenied: Errno](errno/permissiondenied.md)
  Permission denied.
- [static var textFileBusy: Errno](errno/textfilebusy.md)
  Text file busy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/filetoolarge)*