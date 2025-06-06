# cancel()

**Framework**: Apple Archive  
**Kind**: method  
**Required**: Yes

Cancels stream operations.

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
func cancel()
```

#### Discussion

Note that after you’ve called [`cancel()`](archivebytestreamprotocol/cancel().md), you must close the stream to release resources.

## See Also

- [func seek(toOffset: Int64, relativeTo: FileDescriptor.SeekOrigin) throws -> Int64](archivebytestreamprotocol/seek(tooffset:relativeto:).md)
  Updates the internal stream position to the specified offset relative to the specified origin.
- [func close() throws](archivebytestreamprotocol/close.md)
  Closes the stream and releases associated resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestreamprotocol/cancel())*