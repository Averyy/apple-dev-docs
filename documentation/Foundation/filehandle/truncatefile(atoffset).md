# truncateFile(atOffset:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Truncates or extends the file represented by the file handle to a specified offset within the file and puts the file pointer at that position.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.0+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [`truncate(atOffset:)`](./truncate%28atoffset%29.md) to handle errors when truncating or extending the file.

## Declaration

```swift
func truncateFile(atOffset offset: UInt64)
```

```objc
- (void) truncateFileAtOffset:(unsigned long long) offset;
```

## Discussion

If the file is extended (if `offset` is beyond the current end of file), the added characters are null bytes.

> ❗ **Important**:  This method raises [`fileHandleOperationException`](../nsexceptionname/filehandleoperationexception.md) if called on a file handle representing a pipe or socket, if the file descriptor is closed, or if the operation failed.

## Parameters

- `offset`: The offset within the file that marks the new end of the file.

## See Also

### Deprecated
- [func readDataToEndOfFile() -> Data](./readdatatoendoffile%28%29.md)
  Reads the available data synchronously up to the end of file or maximum number of bytes.
- [func readData(ofLength: Int) -> Data](./readdata%28oflength%29.md)
  Reads data synchronously up to the specified number of bytes.
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
- [let NSFileHandleNotificationMonitorModes: String](../nsfilehandlenotificationmonitormodes.md)
  Currently unused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/truncatefile(atoffset:))*