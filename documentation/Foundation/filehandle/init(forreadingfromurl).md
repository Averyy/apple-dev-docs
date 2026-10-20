# init(forReadingFromURL:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Returns a file handle initialized for reading the file, device, or named socket at the specified URL.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(forReadingFromURL url: URL) throws
```

#### Return Value

The initialized file handle object or `nil` if no file exists at `url`.

#### Discussion

The file pointer is set to the beginning of the file. You cannot write data to the returned file handle object. Use the [`readDataToEndOfFile()`](./readdatatoendoffile%28%29.md) or [`readData(ofLength:)`](./readdata%28oflength%29.md) methods to read data from it.

When using this method to create a file handle object, the file handle owns its associated file descriptor and is responsible for closing it.

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: The URL of the file, device, or named socket to access.

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
- [convenience init?(forReadingAtPath: String)](./init%28forreadingatpath%29.md)
  Returns a file handle initialized for reading the file, device, or named socket at the specified path.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/init(forreadingfromurl:))*