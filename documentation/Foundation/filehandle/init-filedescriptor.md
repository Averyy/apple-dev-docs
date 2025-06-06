# init(fileDescriptor:)

**Framework**: Foundation  
**Kind**: init

Creates and returns a file handle object associated with the specified file descriptor.

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
convenience init(fileDescriptor fd: Int32)
```

#### Return Value

A file handle initialized with `fileDescriptor`.

#### Discussion

The file descriptor you pass in to this method isn’t owned by the file handle object. Therefore, you’re responsible for closing the file descriptor at some point after disposing of the file handle object.

You can create a file handle for a socket by using the result of a `socket` call as `fileDescriptor`.

## Parameters

- `fd`: The POSIX file descriptor with which to initialize the file handle. This descriptor represents an open file or socket that you created previously. For example, when creating a file handle for a socket, you’d pass the value returned by the socket function.

## See Also

- [func closeFile()](filehandle/closefile.md)
  Disallows further access to the represented file or communications channel and signals end of file on communications channels that permit writing.
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
- [init?(coder: NSCoder)](filehandle/init(coder:).md)
  Returns a file handle initialized from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/init(filedescriptor:))*