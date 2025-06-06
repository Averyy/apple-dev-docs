# CFReadStreamClose(_:)

**Framework**: Core Foundation  
**Kind**: func

Closes a readable stream.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFReadStreamClose(_ stream: CFReadStream!)
```

#### Discussion

This function terminates the flow of bytes and releases any system resources required by the stream. The stream is removed from any run loops in which it was scheduled. Once closed, the stream cannot be reopened.

## Parameters

- `stream`: The stream to close.

## See Also

- [func CFReadStreamOpen(CFReadStream!) -> Bool](cfreadstreamopen(_:).md)
  Opens a stream for reading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfreadstreamclose(_:))*