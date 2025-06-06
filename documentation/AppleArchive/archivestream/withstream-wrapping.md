# withStream(wrapping:_:)

**Framework**: Apple Archive  
**Kind**: method

Calls the given closure with an archive stream instance mapped to an object that conforms to the archive stream protocol.

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
static func withStream<C, E>(wrapping instance: C, _ body: (ArchiveStream) throws -> E) throws -> E where C : AnyObject, C : ArchiveStreamProtocol
```

#### Return Value

The result of the closure.

## Parameters

- `instance`: The object that the new archive stream wraps.
- `body`: A closure with the archive stream passed as a parameter.

## See Also

- [static func customStream<C>(instance: C) -> ArchiveStream?](archivestream/customstream(instance:).md)
  Returns a new archive stream instance mapped to an object that conforms to the archive stream protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archivestream/withstream(wrapping:_:))*