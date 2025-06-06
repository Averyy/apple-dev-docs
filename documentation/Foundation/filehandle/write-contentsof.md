# write(contentsOf:)

**Framework**: Foundation  
**Kind**: method

Writes the specified data synchronously to the file handle.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 13.4+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
func write<T>(contentsOf data: T) throws where T : DataProtocol
```

#### Discussion

If the handle represents a file, writing takes place at the file pointer’s current position. After it writes the data, the method advances the file pointer by the number of bytes written. This method throws an error if the file descriptor is closed or isn’t valid, if the handle represents an unconnected pipe or socket endpoint, if there isn’t any free space on the file system, or if any other writing error occurs.

## Parameters

- `data`: The data to write to the file handle.

## See Also

- [var availableData: Data](filehandle/availabledata.md)
  The data currently available in the receiver.
- [func read(upToCount: Int) throws -> Data?](filehandle/read(uptocount:).md)
  Reads data synchronously up to the specified number of bytes.
- [func readToEnd() throws -> Data?](filehandle/readtoend.md)
  Reads the available data synchronously up to the end of file or maximum number of bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/write(contentsof:))*