# readToEnd()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Reads the available data synchronously up to the end of file or maximum number of bytes.

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
func readToEnd() throws -> Data?
```

#### Return Value

The data available through the file handle up to the maximum size that can be represented by an [`NSData`](../nsdata.md) object or, if a communications channel, until an end-of-file indicator is returned.

#### Discussion

This method invokes [`readData(ofLength:)`](./readdata%28oflength%29.md) as part of its implementation.

## See Also

### Reading from a file handle synchronously
- [var availableData: Data](./availabledata.md)
  The data currently available in the receiver.
- [func read(upToCount: Int) throws -> Data?](./read%28uptocount%29.md)
  Reads data synchronously up to the specified number of bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/filehandle/readtoend())*