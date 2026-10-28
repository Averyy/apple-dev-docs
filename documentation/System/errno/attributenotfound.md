# attributeNotFound

**Framework**: System  
**Kind**: property  
**Role**: Type Property

Attribute not found.

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
static var attributeNotFound: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](../adopting-errno.md)

## Discussion

The specified extended attribute doesn’t exist.

The corresponding C error is `ENOATTR`.

## See Also

### File and Directory Errors
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
- [static var textFileBusy: Errno](./textfilebusy.md)
  Text file busy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/attributenotfound)*