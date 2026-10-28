# readData(ofLength:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Reads data synchronously up to the specified number of bytes.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.0+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: To handle errors when reading data from the file handle, use [`read(upToCount:)`](./read%28uptocount%29.md) in Swift and [`readDataUpToLength:error:`](../nsfilehandle/readdatauptolength_error_.md) in Objective-C.

## Declaration

```swift
func readData(ofLength length: Int) -> Data
```

```objc
- (NSData *) readDataOfLength:(NSUInteger) length;
```

## Return Value

The data available through the receiver up to a maximum of `length` bytes, or the maximum size that can be represented by an [`NSData`](../nsdata.md) object, whichever is the smaller.

## Discussion

If the handle represents a file, this method returns the data obtained by reading `length` bytes starting at the current file pointer. If `length` bytes aren’t available, this method returns the data from the current file pointer to the end of the file. If the handle represents a communications channel, the method reads up to `length` bytes from the channel. Returns an empty `NSData` object if the handle is at the file’s end or if the communications channel returns an end-of-file indicator.

> ❗ **Important**:  This method raises [`fileHandleOperationException`](../nsexceptionname/filehandleoperationexception.md) if attempts to determine the file-handle type fail or if attempts to read from the file or channel fail.

## Parameters

- `length`: The number of bytes to read from the file handle.

## See Also

### Related Documentation
- [var availableData: Data](./availabledata.md)
  The data currently available in the receiver.
### Deprecated
- [func readDataToEndOfFile() -> Data](./readdatatoendoffile%28%29.md)
  Reads the available data synchronously up to the end of file or maximum number of bytes.
- [func write(Data)](./write%28_%29.md)
  Writes the specified data synchronously to the file handle.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/readdata(oflength:))*