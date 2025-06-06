# init(coder:)

**Framework**: Foundation  
**Kind**: init

Returns a file handle initialized from data in an unarchiver.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(coder: NSCoder)
```

## See Also

- [convenience init(fileDescriptor: Int32)](filehandle/init(filedescriptor:).md)
  Creates and returns a file handle object associated with the specified file descriptor.
- [init(fileDescriptor: Int32, closeOnDealloc: Bool)](filehandle/init(filedescriptor:closeondealloc:).md)
  Creates and returns a file handle object associated with the specified file descriptor and deallocation policy.
- [convenience init?(forReadingAtPath: String)](filehandle/init(forreadingatpath:).md)
  Returns a file handle initialized for reading the file, device, or named socket at the specified path.
- [convenience init(forReadingFromURL: URL) throws](filehandle/init(forreadingfromurl:).md)
  Returns a file handle initialized for reading the file, device, or named socket at the specified URL.
- [convenience init?(forWritingAtPath: String)](filehandle/init(forwritingatpath:).md)
  Returns a file handle initialized for writing to the file, device, or named socket at the specified path.
- [convenience init(forWritingToURL: URL) throws](filehandle/init(forwritingtourl:).md)
  Returns a file handle initialized for writing to the file, device, or named socket at the specified URL.
- [convenience init?(forUpdatingAtPath: String)](filehandle/init(forupdatingatpath:).md)
  Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified path.
- [convenience init(forUpdatingURL: URL) throws](filehandle/init(forupdatingurl:).md)
  Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/init(coder:))*