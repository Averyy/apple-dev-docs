# write(_:)

**Framework**: Foundation  
**Kind**: method

Writes the specified data synchronously to the file handle.

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
func write(_ data: Data)
```

#### Discussion

If the handle represents a file, writing takes place at the file pointer’s current position. After it writes the data, the method advances the file pointer by the number of bytes written.

> ❗ **Important**:  This method raises [`fileHandleOperationException`](nsexceptionname/filehandleoperationexception.md) if the file descriptor is closed or isn’t valid, if the handle represents an unconnected pipe or socket endpoint, if there isn’t any free space on the file system, or if any other writing error occurs.

 This method raises [`fileHandleOperationException`](nsexceptionname/filehandleoperationexception.md) if the file descriptor is closed or isn’t valid, if the handle represents an unconnected pipe or socket endpoint, if there isn’t any free space on the file system, or if any other writing error occurs.

## Parameters

- `data`: The data to write to the file handle.

## See Also

- [var availableData: Data](filehandle/availabledata.md)
  The data currently available in the receiver.
- [func readDataToEndOfFile() -> Data](filehandle/readdatatoendoffile.md)
  Reads the available data synchronously up to the end of file or maximum number of bytes.
- [func readData(ofLength: Int) -> Data](filehandle/readdata(oflength:).md)
  Reads data synchronously up to the specified number of bytes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/write(_:))*