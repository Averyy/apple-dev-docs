# availableData

**Framework**: Foundation  
**Kind**: property

The data currently available in the receiver.

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
var availableData: Data { get }
```

#### Discussion

The data currently available through the receiver, up to the maximum size that can be represented by an [`NSData`](nsdata.md) object.

If the receiver is a file, this method returns the data obtained by reading the file from the current file pointer to the end of the file. If the receiver is a communications channel, this method reads up to a buffer of data and returns it; if no data is available, the method blocks. Returns an empty data object if the end of file is reached. This method raises `NSFileHandleOperationException` if attempts to determine the file-handle type fail or if attempts to read from the file or channel fail.

## See Also

- [func readData(ofLength: Int) -> Data](filehandle/readdata(oflength:).md)
  Reads data synchronously up to the specified number of bytes.
- [func readDataToEndOfFile() -> Data](filehandle/readdatatoendoffile.md)
  Reads the available data synchronously up to the end of file or maximum number of bytes.
- [func readToEnd() throws -> Data?](filehandle/readtoend.md)
  Reads the available data synchronously up to the end of file or maximum number of bytes.
- [func read(upToCount: Int) throws -> Data?](filehandle/read(uptocount:).md)
  Reads data synchronously up to the specified number of bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/availabledata)*