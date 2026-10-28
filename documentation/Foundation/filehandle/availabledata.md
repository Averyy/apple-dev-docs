# availableData

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, readonly) NSData * availableData;
```

## Discussion

The data currently available through the receiver, up to the maximum size that can be represented by an [`NSData`](../nsdata.md) object.

If the receiver is a file, this method returns the data obtained by reading the file from the current file pointer to the end of the file. If the receiver is a communications channel, this method reads up to a buffer of data and returns it; if no data is available, the method blocks. Returns an empty data object if the end of file is reached. This method raises `NSFileHandleOperationException` if attempts to determine the file-handle type fail or if attempts to read from the file or channel fail.

## See Also

### Related Documentation
- [func readData(ofLength: Int) -> Data](./readdata%28oflength%29.md)
  Reads data synchronously up to the specified number of bytes.
- [func readDataToEndOfFile() -> Data](./readdatatoendoffile%28%29.md)
  Reads the available data synchronously up to the end of file or maximum number of bytes.
### Reading from a file handle synchronously
- [func readToEnd() throws -> Data?](./readtoend%28%29.md)
  Reads the available data synchronously up to the end of file or maximum number of bytes.
- [func read(upToCount: Int) throws -> Data?](./read%28uptocount%29.md)
  Reads data synchronously up to the specified number of bytes.
- [- readDataToEndOfFileAndReturnError:](../nsfilehandle/readdatatoendoffileandreturnerror_.md)
  Reads the available data synchronously up to the end of file or maximum number of bytes.
- [- readDataUpToLength:error:](../nsfilehandle/readdatauptolength_error_.md)
  Reads data synchronously up to the specified number of bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/availabledata)*