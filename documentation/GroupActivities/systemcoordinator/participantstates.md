# SystemCoordinator.ParticipantStates

**Framework**: Group Activities  
**Kind**: struct

An asynchronous sequence that reports the current person’s ability to participate in a shared context.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct ParticipantStates
```

## Topics

### Creating an iterator
- [func makeAsyncIterator() -> SystemCoordinator.ParticipantStates.Iterator](systemcoordinator/participantstates/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [SystemCoordinator.ParticipantStates.Iterator](systemcoordinator/participantstates/iterator.md)
- [SystemCoordinator.ParticipantStates.Element](systemcoordinator/participantstates/element.md)
  The type of element produced by this asynchronous sequence.
### Type Aliases
- [SystemCoordinator.ParticipantStates.AsyncIterator](systemcoordinator/participantstates/asynciterator.md)
  The type of asynchronous iterator that produces elements of this asynchronous sequence.
### Default Implementations
- [AsyncSequence Implementations](systemcoordinator/participantstates/asyncsequence-implementations.md)

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var remoteParticipantStates: [Participant : SystemCoordinator.ParticipantState]](systemcoordinator/remoteparticipantstates.md)
- [var localParticipantState: SystemCoordinator.ParticipantState](systemcoordinator/localparticipantstate.md)
  The current participant’s level of support for an activity that takes place in a shared simulation space.
- [var localParticipantStates: SystemCoordinator.ParticipantStates](systemcoordinator/localparticipantstates.md)
  An asynchronous sequence that reports changes to the local participant’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/systemcoordinator/participantstates)*