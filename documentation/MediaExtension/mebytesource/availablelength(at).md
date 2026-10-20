# availableLength(at:)

**Framework**: MediaExtension  
**Kind**: method  
**Role**: Instance Method

Gets the number of available bytes from the offset within the byte source.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func availableLength(at offset: Int64) -> Int64
```

```objc
- (int64_t) availableLengthAtOffset:(int64_t) offset;
```

#### Return Value

An integer that specifies the number of available bytes.

## Parameters

- `offset`: The offset in bytes from the beginning of the byte source.

## See Also

### Performing operations on a byte source
- [func byteSourceForRelatedFileName(String) throws -> MEByteSource](./bytesourceforrelatedfilename%28_%29.md)
  Creates a new byte source for a related file.
- [func read(length: Int, from: Int64, completionHandler: (Data?, (any Error)?) -> Void)](./read%28length,from,completionhandler%29.md)
  Reads bytes from a byte source into a data object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/mebytesource/availablelength(at:))*