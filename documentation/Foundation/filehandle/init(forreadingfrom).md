# init(forReadingFrom:)

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
convenience init(forReadingFrom url: URL) throws
```

```objc
+ (instancetype) fileHandleForReadingFromURL:(NSURL *) url error:(NSError **) error;
```

#### Return Value

The initialized file handle object or `nil` if no file exists at `url`.

#### Discussion

The file pointer is set to the beginning of the file. You cannot write data to the returned file handle object. Use the [`readDataToEndOfFile()`](./readdatatoendoffile%28%29.md) or [`readData(ofLength:)`](./readdata%28oflength%29.md) methods to read data from it.

When using this method to create a file handle object, the file handle owns its associated file descriptor and is responsible for closing it.

## Parameters

- `url`: The URL of the file, device, or named socket to access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/init(forreadingfrom:))*