# seek(toOffset:relativeTo:)

**Framework**: Apple Archive  
**Kind**: method  
**Required**: Yes

Updates the internal stream position to the specified offset relative to the specified origin.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
func seek(toOffset offset: Int64, relativeTo origin: FileDescriptor.SeekOrigin) throws -> Int64
```

#### Return Value

The new internal stream position that is relative to the beginning of the stream.

## Parameters

- `offset`: The offset relative to the reference position from which to seek.
- `origin`: The reference position from which to seek.

## See Also

- [func cancel()](archivebytestreamprotocol/cancel.md)
  Cancels stream operations.
- [func close() throws](archivebytestreamprotocol/close.md)
  Closes the stream and releases associated resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestreamprotocol/seek(tooffset:relativeto:))*