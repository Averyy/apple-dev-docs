# init(forUpdatingAtPath:)

**Framework**: Foundation  
**Kind**: init

Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified path.

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
convenience init?(forUpdatingAtPath path: String)
```

#### Return Value

The initialized file handle object or `nil` if no file exists at `path`.

#### Discussion

The file pointer is set to the beginning of the file. The returned object responds to both   `read...` messages and [`write(_:)`](filehandle/write(_:).md).

When using this method to create a file handle object, the file handle owns its associated file descriptor and is responsible for closing it.

## Parameters

- `path`: The path to the file, device, or named socket to access.

## See Also

- [var availableData: Data](filehandle/availabledata.md)
  The data currently available in the receiver.
- [func readData(ofLength: Int) -> Data](filehandle/readdata(oflength:).md)
  Reads data synchronously up to the specified number of bytes.
- [func readDataToEndOfFile() -> Data](filehandle/readdatatoendoffile.md)
  Reads the available data synchronously up to the end of file or maximum number of bytes.
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
- [convenience init(forUpdatingURL: URL) throws](filehandle/init(forupdatingurl:).md)
  Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified URL.
- [init?(coder: NSCoder)](filehandle/init(coder:).md)
  Returns a file handle initialized from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/init(forupdatingatpath:))*