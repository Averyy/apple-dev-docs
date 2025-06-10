# localParticipantStates

**Framework**: Group Activities  
**Kind**: property

An asynchronous sequence that reports changes to the local participant’s state.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
final var localParticipantStates: SystemCoordinator.ParticipantStates { get }
```

## Mentions

- [Adding spatial Persona support to an activity](adding-spatial-persona-support-to-an-activity.md)
- [Configure your visionOS app for sharing with people nearby](configure-your-app-for-sharing-with-people-nearby.md)

#### Discussion

Use this property to detect when the current person starts or stops displaying their spatial Persona. The following example shows how to set up a task to monitor the sequence and respond to changes:

```swift
Task.detached {
    for await localParticipantState in systemCoordinator.localParticipantStates {
         if localParticipantState.isSpatial {
              // Handle changes to the state.
         }
    }
}
```

## See Also

- [var remoteParticipantStates: [Participant : SystemCoordinator.ParticipantState]](systemcoordinator/remoteparticipantstates.md)
- [var localParticipantState: SystemCoordinator.ParticipantState](systemcoordinator/localparticipantstate.md)
  The current participant’s level of support for an activity that takes place in a shared simulation space.
- [SystemCoordinator.ParticipantStates](systemcoordinator/participantstates.md)
  An asynchronous sequence that reports the current person’s ability to participate in a shared context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/systemcoordinator/localparticipantstates)*