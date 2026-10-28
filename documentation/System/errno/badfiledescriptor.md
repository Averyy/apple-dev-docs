# badFileDescriptor

**Framework**: System  
**Kind**: property  
**Role**: Type Property

Bad file descriptor.

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
static var badFileDescriptor: Errno { get }
```

## Mentions

- [Adopting Swift Error Constants](../adopting-errno.md)

## Discussion

A file descriptor argument was out of range, referred to no open file, or a read (write) request was made to a file that was only open for writing (reading).

The corresponding C error is `EBADF`.

## See Also

### File and Directory Errors
- [static var attributeNotFound: Errno](./attributenotfound.md)
  Attribute not found.
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

*[View on Apple Developer](https://developer.apple.com/documentation/system/errno/badfiledescriptor)*