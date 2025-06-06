# GroupSessionMessenger.Messages.Iterator

**Framework**: Group Activities  
**Kind**: struct

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
struct Iterator
```

## Topics

### Instance Methods
- [func next() async -> GroupSessionMessenger.Messages<Message>.Element?](groupsessionmessenger/messages/iterator/next.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
### Type Aliases
- [GroupSessionMessenger.Messages.Iterator.Element](groupsessionmessenger/messages/iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](groupsessionmessenger/messages/iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func makeAsyncIterator() -> GroupSessionMessenger.Messages<Message>.Iterator](groupsessionmessenger/messages/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [GroupSessionMessenger.Messages.Element](groupsessionmessenger/messages/element.md)
  The type of element produced by this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionmessenger/messages/iterator)*