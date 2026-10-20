# close()

**Framework**: Apple Archive  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Closes the stream and releases associated resources.

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
func close() throws
```

#### Discussion

After calling [`close()`](./close%28%29.md), expect that subsequent function calls on the stream to trigger a runtime error.

You must close all opened streams, otherwise deinitialization causes a runtime error.

## See Also

### Using Archive Byte Streams
- [func seek(toOffset: Int64, relativeTo: FileDescriptor.SeekOrigin) throws -> Int64](./seek%28tooffset,relativeto%29.md)
  Updates the internal stream position to the specified offset relative to the specified origin.
- [func cancel()](./cancel%28%29.md)
  Cancels stream operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestreamprotocol/close())*