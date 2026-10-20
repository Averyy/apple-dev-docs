# remoteParticipantStates

**Framework**: Group Activities  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- visionOS 26.0+

## Declaration

```swift
final var remoteParticipantStates: [Participant : SystemCoordinator.ParticipantState] { get }
```

## Mentions

- [Configure your visionOS app for sharing with people nearby](../configure-your-app-for-sharing-with-people-nearby.md)

## See Also

### Getting the participant state
- [var localParticipantState: SystemCoordinator.ParticipantState](./localparticipantstate.md)
  The current participant’s level of support for an activity that takes place in a shared simulation space.
- [var localParticipantStates: SystemCoordinator.ParticipantStates](./localparticipantstates.md)
  An asynchronous sequence that reports changes to the local participant’s state.
- [SystemCoordinator.ParticipantStates](./participantstates.md)
  An asynchronous sequence that reports the current person’s ability to participate in a shared context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/systemcoordinator/remoteparticipantstates)*