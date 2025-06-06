# read(upToCount:)

**Framework**: Foundation  
**Kind**: method

Reads data synchronously up to the specified number of bytes.

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
func read(upToCount count: Int) throws -> Data?
```

#### Return Value

The data available through the receiver up to a maximum of `length` bytes, or the maximum size that can be represented by an [`NSData`](nsdata.md) object, whichever is the smaller.

#### Discussion

If the handle represents a file, this method returns the data obtained by reading `length` bytes starting at the current file pointer. If `length` bytes aren’t available, this method returns the data from the current file pointer to the end of the file. If the handle is a communications channel, the method reads up to `length` bytes from the channel. Returns an empty [`NSData`](nsdata.md) object if the handle is at the file’s end or if the communications channel returns an end-of-file indicator.

This method throws an error if attempts to determine the file-handle type fail or if attempts to read from the file or channel fail.

## Parameters

- `count`: The number of bytes to read from the file handle.

## See Also

- [var availableData: Data](filehandle/availabledata.md)
  The data currently available in the receiver.
- [func readToEnd() throws -> Data?](filehandle/readtoend.md)
  Reads the available data synchronously up to the end of file or maximum number of bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/read(uptocount:))*