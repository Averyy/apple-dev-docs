# SystemCoordinator.ParticipantStates.Iterator

**Framework**: Group Activities  
**Kind**: struct

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct Iterator
```

## Topics

### Instance Methods
- [func next() async -> SystemCoordinator.ParticipantStates.Element?](systemcoordinator/participantstates/iterator/next.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.
### Type Aliases
- [SystemCoordinator.ParticipantStates.Iterator.Element](systemcoordinator/participantstates/iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](systemcoordinator/participantstates/iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func makeAsyncIterator() -> SystemCoordinator.ParticipantStates.Iterator](systemcoordinator/participantstates/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [SystemCoordinator.ParticipantStates.Element](systemcoordinator/participantstates/element.md)
  The type of element produced by this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/systemcoordinator/participantstates/iterator)*