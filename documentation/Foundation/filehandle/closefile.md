# closeFile()

**Framework**: Foundation  
**Kind**: method

Disallows further access to the represented file or communications channel and signals end of file on communications channels that permit writing.

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
func closeFile()
```

#### Discussion

If the file handle object owns its file descriptor, it automatically closes that descriptor when it is deallocated. If you initialized the file handle object using the [`init(fileDescriptor:)`](filehandle/init(filedescriptor:).md) method, or you initialized it using the [`init(fileDescriptor:closeOnDealloc:)`](filehandle/init(filedescriptor:closeondealloc:).md) and passed [`false`](https://developer.apple.com/documentation/Swift/false) for the `flag` parameter, you can use this method to close the file descriptor; otherwise, you must close the file descriptor yourself.

After calling this method, you may still use the file handle object but must not attempt to read or write data or use the object to operate on the file descriptor. Attempts to read or write a closed file descriptor raise an exception.

## See Also

- [func readDataToEndOfFile() -> Data](filehandle/readdatatoendoffile.md)
  Reads the available data synchronously up to the end of file or maximum number of bytes.
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
- [func synchronizeFile()](filehandle/synchronizefile.md)
  Causes all in-memory data and attributes of the file represented by the handle to write to permanent storage.
- [func truncateFile(atOffset: UInt64)](filehandle/truncatefile(atoffset:).md)
  Truncates or extends the file represented by the file handle to a specified offset within the file and puts the file pointer at that position.
- [let NSFileHandleNotificationMonitorModes: String](nsfilehandlenotificationmonitormodes.md)
  Currently unused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/closefile())*