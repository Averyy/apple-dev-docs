# init(forReadingAtPath:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns a file handle initialized for reading the file, device, or named socket at the specified path.

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
convenience init?(forReadingAtPath path: String)
```

```objc
+ (instancetype) fileHandleForReadingAtPath:(NSString *) path;
```

## Return Value

The initialized file handle object or `nil` if no file exists at `path`.

## Discussion

The system sets the file pointer to the beginning of the file. You can’t write data to the returned file handle object. Use the [`readDataToEndOfFile()`](./readdatatoendoffile%28%29.md) or [`readData(ofLength:)`](./readdata%28oflength%29.md) methods to read data from it.

When using this method to create a file handle object, the file handle owns its associated file descriptor and is responsible for closing it.

## Parameters

- `path`: The path to the file, device, or named socket to access.

## See Also

### Related Documentation
- [var availableData: Data](./availabledata.md)
  The data currently available in the receiver.
- [func readData(ofLength: Int) -> Data](./readdata%28oflength%29.md)
  Reads data synchronously up to the specified number of bytes.
- [func readDataToEndOfFile() -> Data](./readdatatoendoffile%28%29.md)
  Reads the available data synchronously up to the end of file or maximum number of bytes.
### Creating a file handle
- [convenience init(fileDescriptor: Int32)](./init%28filedescriptor%29.md)
  Creates and returns a file handle object associated with the specified file descriptor.
- [init(fileDescriptor: Int32, closeOnDealloc: Bool)](./init%28filedescriptor,closeondealloc%29.md)
  Creates and returns a file handle object associated with the specified file descriptor and deallocation policy.
- [convenience init(forReadingFromURL: URL) throws](./init%28forreadingfromurl%29.md)
  Returns a file handle initialized for reading the file, device, or named socket at the specified URL.
- [convenience init?(forWritingAtPath: String)](./init%28forwritingatpath%29.md)
  Returns a file handle initialized for writing to the file, device, or named socket at the specified path.
- [convenience init(forWritingToURL: URL) throws](./init%28forwritingtourl%29.md)
  Returns a file handle initialized for writing to the file, device, or named socket at the specified URL.
- [convenience init?(forUpdatingAtPath: String)](./init%28forupdatingatpath%29.md)
  Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified path.
- [convenience init(forUpdatingURL: URL) throws](./init%28forupdatingurl%29.md)
  Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified URL.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Returns a file handle initialized from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/init(forreadingatpath:))*