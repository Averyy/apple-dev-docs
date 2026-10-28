# write(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Writes the specified data synchronously to the file handle.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.0+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: To handle errors when writing data to the file handle, use [`write(contentsOf:)`](./write%28contentsof%29.md) in Swift and [`writeData:error:`](../nsfilehandle/writedata_error_.md) in Objective-C.

## Declaration

```swift
func write(_ data: Data)
```

```objc
- (void) writeData:(NSData *) data;
```

## Discussion

If the handle represents a file, writing takes place at the file pointer’s current position. After it writes the data, the method advances the file pointer by the number of bytes written.

> ❗ **Important**:  This method raises [`fileHandleOperationException`](../nsexceptionname/filehandleoperationexception.md) if the file descriptor is closed or isn’t valid, if the handle represents an unconnected pipe or socket endpoint, if there isn’t any free space on the file system, or if any other writing error occurs.

## Parameters

- `data`: The data to write to the file handle.

## See Also

### Related Documentation
- [var availableData: Data](./availabledata.md)
  The data currently available in the receiver.
### Deprecated
- [func readDataToEndOfFile() -> Data](./readdatatoendoffile%28%29.md)
  Reads the available data synchronously up to the end of file or maximum number of bytes.
- [func readData(ofLength: Int) -> Data](./readdata%28oflength%29.md)
  Reads data synchronously up to the specified number of bytes.
- [var offsetInFile: UInt64](./offsetinfile.md)
  The position of the file pointer within the file represented by the file handle.
- [func seekToEndOfFile() -> UInt64](./seektoendoffile%28%29.md)
  Places the file pointer at the end of the file referenced by the file handle and returns the new file offset.
- [func seek(toFileOffset: UInt64)](./seek%28tofileoffset%29.md)
  Moves the file pointer to the specified offset within the file represented by the receiver.
- [func closeFile()](./closefile%28%29.md)
  Disallows further access to the represented file or communications channel and signals end of file on communications channels that permit writing.
- [func synchronizeFile()](./synchronizefile%28%29.md)
  Causes all in-memory data and attributes of the file represented by the handle to write to permanent storage.
- [func truncateFile(atOffset: UInt64)](./truncatefile%28atoffset%29.md)
  Truncates or extends the file represented by the file handle to a specified offset within the file and puts the file pointer at that position.
- [let NSFileHandleNotificationMonitorModes: String](../nsfilehandlenotificationmonitormodes.md)
  Currently unused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/write(_:))*