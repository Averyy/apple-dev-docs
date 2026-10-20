# SystemCoordinator.ParticipantStates.Iterator

**Framework**: Group Activities  
**Kind**: struct  
**Role**: Structure

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct Iterator
```

## Topics

### Instance Methods
- [func next() async -> SystemCoordinator.ParticipantStates.Element?](./iterator/next%28%29.md)
  Asynchronously advances to the next element and returns it, or ends the sequence if there is no next element.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../../../Swift/asynciteratorprotocol.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Creating an iterator
- [func makeAsyncIterator() -> SystemCoordinator.ParticipantStates.Iterator](./makeasynciterator%28%29.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [SystemCoordinator.ParticipantStates.Element](./element.md)
  The type of element produced by this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/systemcoordinator/participantstates/iterator)*