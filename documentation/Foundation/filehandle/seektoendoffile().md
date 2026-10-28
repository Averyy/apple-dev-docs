# seekToEndOfFile()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Places the file pointer at the end of the file referenced by the file handle and returns the new file offset.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.0+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use To handle errors when seeking to the end of the file, use [`seekToEnd()`](./seektoend%28%29.md) in Swift and  [`seekToEndReturningOffset:error:`](../nsfilehandle/seektoendreturningoffset_error_.md) in Objective-C.

## Declaration

```swift
func seekToEndOfFile() -> UInt64
```

```objc
- (unsigned long long) seekToEndOfFile;
```

## Return Value

The file offset with the file pointer at the end of the file. This is therefore equal to the size of the file.

## Discussion

Raises [`fileHandleOperationException`](../nsexceptionname/filehandleoperationexception.md) if called on a file handle representing a pipe or socket, if the file descriptor is closed, or if any other error occurs while seeking.

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/seektoendoffile())*