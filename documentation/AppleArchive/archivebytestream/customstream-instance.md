# customStream(instance:)

**Framework**: Apple Archive  
**Kind**: method

Returns a new archive byte stream instance mapped to an object that conforms to the archive byte stream protocol.

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
static func customStream<C>(instance: C) -> ArchiveByteStream? where C : AnyObject, C : ArchiveByteStreamProtocol
```

#### Return Value

A new archive byte stream.

## Parameters

- `instance`: The object that the new archive stream wraps.

## See Also

- [static func withStream<C, E>(wrapping: C, (ArchiveByteStream) throws -> E) throws -> E](archivebytestream/withstream(wrapping:_:).md)
  Calls the given closure with an archive byte stream instance mapped to an object that conforms to the archive byte stream protocol.
- [static func sharedBufferPipe(capacity: Int) -> (output: ArchiveByteStream, input: ArchiveByteStream)?](archivebytestream/sharedbufferpipe(capacity:).md)
  Creates a pair of streams and links them by a shared buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivebytestream/customstream(instance:))*