# localParticipantState

**Framework**: Group Activities  
**Kind**: property

The current participant’s level of support for an activity that takes place in a shared simulation space.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
final var localParticipantState: SystemCoordinator.ParticipantState { get }
```

#### Discussion

This property tells you when the current participant supports inclusion in a shared simulation space. This property is `true` if the participant is using a device that supports spatial placement, configured their spatial Persona on that device, and enabled it for the current activity.

This property reflects only the state of the current participant. When this property is `true`, share additional information during activity updates to reflect changes the participant makes to the shared content. For example, if the participant rotates a 3D model, share the rotation amount so that your app can rotate the model on the devices of other participants. When your app receives such a change from another participant, incorporate those changes only if the value of this property is `true`. The goal of sharing information is to preserve the shared context of the scene, and to make it seem like people are experiencing the content together.

## See Also

- [var remoteParticipantStates: [Participant : SystemCoordinator.ParticipantState]](systemcoordinator/remoteparticipantstates.md)
- [var localParticipantStates: SystemCoordinator.ParticipantStates](systemcoordinator/localparticipantstates.md)
  An asynchronous sequence that reports changes to the local participant’s state.
- [SystemCoordinator.ParticipantStates](systemcoordinator/participantstates.md)
  An asynchronous sequence that reports the current person’s ability to participate in a shared context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/systemcoordinator/localparticipantstate)*