# SystemCoordinator.ParticipantStates

**Framework**: Group Activities  
**Kind**: struct  
**Role**: Structure

An asynchronous sequence that reports the current person’s ability to participate in a shared context.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct ParticipantStates
```

## Topics

### Creating an iterator
- [func makeAsyncIterator() -> SystemCoordinator.ParticipantStates.Iterator](./participantstates/makeasynciterator%28%29.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.
- [SystemCoordinator.ParticipantStates.Iterator](./participantstates/iterator.md)
- [SystemCoordinator.ParticipantStates.Element](./participantstates/element.md)
  The type of element produced by this asynchronous sequence.

## Relationships

### Conforms To
- [AsyncSequence](../../Swift/asyncsequence.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the participant state
- [var remoteParticipantStates: [Participant : SystemCoordinator.ParticipantState]](./remoteparticipantstates.md)
- [var localParticipantState: SystemCoordinator.ParticipantState](./localparticipantstate.md)
  The current participant’s level of support for an activity that takes place in a shared simulation space.
- [var localParticipantStates: SystemCoordinator.ParticipantStates](./localparticipantstates.md)
  An asynchronous sequence that reports changes to the local participant’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/systemcoordinator/participantstates)*