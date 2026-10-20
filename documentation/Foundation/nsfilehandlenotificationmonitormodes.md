# NSFileHandleNotificationMonitorModes

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

Currently unused.

**Availability**:
- iOS 2.0+ - Deprecated in 5.0
- iPadOS 2.0+ - Deprecated in 5.0
- Mac Catalyst 2.0+ - Deprecated in 5.0
- tvOS 9.0+ - Deprecated in 9.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Not supported

## Declaration

```swift
let NSFileHandleNotificationMonitorModes: String
```

```c
extern NSString * const NSFileHandleNotificationMonitorModes;
```

## See Also

### Deprecated
- [func readDataToEndOfFile() -> Data](./filehandle/readdatatoendoffile%28%29.md)
  Reads the available data synchronously up to the end of file or maximum number of bytes.
- [func readData(ofLength: Int) -> Data](./filehandle/readdata%28oflength%29.md)
  Reads data synchronously up to the specified number of bytes.
- [func write(Data)](./filehandle/write%28_%29.md)
  Writes the specified data synchronously to the file handle.
- [var offsetInFile: UInt64](./filehandle/offsetinfile.md)
  The position of the file pointer within the file represented by the file handle.
- [func seekToEndOfFile() -> UInt64](./filehandle/seektoendoffile%28%29.md)
  Places the file pointer at the end of the file referenced by the file handle and returns the new file offset.
- [func seek(toFileOffset: UInt64)](./filehandle/seek%28tofileoffset%29.md)
  Moves the file pointer to the specified offset within the file represented by the receiver.
- [func closeFile()](./filehandle/closefile%28%29.md)
  Disallows further access to the represented file or communications channel and signals end of file on communications channels that permit writing.
- [func synchronizeFile()](./filehandle/synchronizefile%28%29.md)
  Causes all in-memory data and attributes of the file represented by the handle to write to permanent storage.
- [func truncateFile(atOffset: UInt64)](./filehandle/truncatefile%28atoffset%29.md)
  Truncates or extends the file represented by the file handle to a specified offset within the file and puts the file pointer at that position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsfilehandlenotificationmonitormodes)*