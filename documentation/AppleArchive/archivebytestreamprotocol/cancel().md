# cancel()

**Framework**: Apple Archive  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Cancels stream operations.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
func cancel()
```

#### Discussion

Note that after you’ve called [`cancel()`](./cancel%28%29.md), you must close the stream to release resources.

## See Also

### Using Archive Byte Streams
- [func seek(toOffset: Int64, relativeTo: FileDescriptor.SeekOrigin) throws -> Int64](./seek%28tooffset,relativeto%29.md)
  Updates the internal stream position to the specified offset relative to the specified origin.
- [func close() throws](./close%28%29.md)
  Closes the stream and releases associated resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestreamprotocol/cancel())*