# close()

**Framework**: Apple Archive  
**Kind**: method  
**Required**: Yes

Closes the stream and releases associated resources.

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
func close() throws
```

#### Discussion

After calling [`close()`](archivebytestreamprotocol/close().md), expect that subsequent function calls on the stream to trigger a runtime error.

You must close all opened streams, otherwise deinitialization causes a runtime error.

## See Also

- [func seek(toOffset: Int64, relativeTo: FileDescriptor.SeekOrigin) throws -> Int64](archivebytestreamprotocol/seek(tooffset:relativeto:).md)
  Updates the internal stream position to the specified offset relative to the specified origin.
- [func cancel()](archivebytestreamprotocol/cancel.md)
  Cancels stream operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestreamprotocol/close())*