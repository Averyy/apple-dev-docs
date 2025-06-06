# GroupSessionJournal.Attachments.Iterator

**Framework**: Group Activities  
**Kind**: struct

The asynchronous iterator that produces a sequence of attachments.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct Iterator
```

## Topics

### Instance Methods
- [func next() async -> GroupSessionJournal.Attachments.Element?](groupsessionjournal/attachments-swift.struct/iterator/next.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
### Type Aliases
- [GroupSessionJournal.Attachments.Iterator.Element](groupsessionjournal/attachments-swift.struct/iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](groupsessionjournal/attachments-swift.struct/iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func makeAsyncIterator() -> GroupSessionJournal.Attachments.Iterator](groupsessionjournal/attachments-swift.struct/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [GroupSessionJournal.Attachments.Element](groupsessionjournal/attachments-swift.struct/element.md)
  The type of element this asynchronous sequence produces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionjournal/attachments-swift.struct/iterator)*