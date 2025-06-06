# withStream(wrapping:_:)

**Framework**: Apple Archive  
**Kind**: method

Calls the given closure with an archive byte stream instance mapped to an object that conforms to the archive byte stream protocol.

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
static func withStream<C, E>(wrapping instance: C, _ body: (ArchiveByteStream) throws -> E) throws -> E where C : AnyObject, C : ArchiveByteStreamProtocol
```

#### Return Value

The result of the closure.

## Parameters

- `instance`: The object that the new archive stream wraps.
- `body`: A closure with the archive byte stream passed as a parameter.

## See Also

- [static func customStream<C>(instance: C) -> ArchiveByteStream?](archivebytestream/customstream(instance:).md)
  Returns a new archive byte stream instance mapped to an object that conforms to the archive byte stream protocol.
- [static func sharedBufferPipe(capacity: Int) -> (output: ArchiveByteStream, input: ArchiveByteStream)?](archivebytestream/sharedbufferpipe(capacity:).md)
  Creates a pair of streams and links them by a shared buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestream/withstream(wrapping:_:))*