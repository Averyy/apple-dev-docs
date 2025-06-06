# readDataToEndOfFile()

**Framework**: Foundation  
**Kind**: method

Reads the available data synchronously up to the end of file or maximum number of bytes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func readDataToEndOfFile() -> Data
```

#### Return Value

The data available through the receiver up to maximum size that can be represented by an [`NSData`](nsdata.md) object or, if a communications channel, until an end-of-file indicator is returned.

#### Discussion

This method invokes [`readData(ofLength:)`](filehandle/readdata(oflength:).md) as part of its implementation.

> ❗ **Important**:  This method raises [`fileHandleOperationException`](nsexceptionname/filehandleoperationexception.md) if attempts to determine the file-handle type fail or if attempts to read from the file or channel fail.

 This method raises [`fileHandleOperationException`](nsexceptionname/filehandleoperationexception.md) if attempts to determine the file-handle type fail or if attempts to read from the file or channel fail.

## See Also

- [var availableData: Data](filehandle/availabledata.md)
  The data currently available in the receiver.
- [func readData(ofLength: Int) -> Data](filehandle/readdata(oflength:).md)
  Reads data synchronously up to the specified number of bytes.
- [func write(Data)](filehandle/write(_:).md)
  Writes the specified data synchronously to the file handle.
- [var offsetInFile: UInt64](filehandle/offsetinfile.md)
  The position of the file pointer within the file represented by the file handle.
- [func seekToEndOfFile() -> UInt64](filehandle/seektoendoffile.md)
  Places the file pointer at the end of the file referenced by the file handle and returns the new file offset.
- [func seek(toFileOffset: UInt64)](filehandle/seek(tofileoffset:).md)
  Moves the file pointer to the specified offset within the file represented by the receiver.
- [func closeFile()](filehandle/closefile.md)
  Disallows further access to the represented file or communications channel and signals end of file on communications channels that permit writing.
- [func synchronizeFile()](filehandle/synchronizefile.md)
  Causes all in-memory data and attributes of the file represented by the handle to write to permanent storage.
- [func truncateFile(atOffset: UInt64)](filehandle/truncatefile(atoffset:).md)
  Truncates or extends the file represented by the file handle to a specified offset within the file and puts the file pointer at that position.
- [let NSFileHandleNotificationMonitorModes: String](nsfilehandlenotificationmonitormodes.md)
  Currently unused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/readdatatoendoffile())*