# customStream(instance:)

**Framework**: Apple Archive  
**Kind**: method

Returns a new archive stream instance mapped to an object that conforms to the archive stream protocol.

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
static func customStream<C>(instance: C) -> ArchiveStream? where C : AnyObject, C : ArchiveStreamProtocol
```

#### Return Value

A new archive stream.

## Parameters

- `instance`: The object that the new archive stream wraps.

## See Also

- [static func withStream<C, E>(wrapping: C, (ArchiveStream) throws -> E) throws -> E](archivestream/withstream(wrapping:_:).md)
  Calls the given closure with an archive stream instance mapped to an object that conforms to the archive stream protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivestream/customstream(instance:))*