# supportsGroupImmersiveSpace

**Framework**: Group Activities  
**Kind**: property

A Boolean value that indicates whether your app supports a shared context when an immersive space is open.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var supportsGroupImmersiveSpace: Bool
```

#### Discussion

If your app presents an immersive space, set this property to `true` if you want the system to display spatial Personas when that space is open. The default value of this property is `false`.

An immersive space places a person in their own private experience. To prevent the disruption of that experience, the system disables spatial Personas by default when any immersive space is open. Setting this property to `true` tells the system that it can once again display spatial Personas when an immersive space is open.

When displaying spatial Personas in an immersive space, the system establishes a shared coordinate space among the participants. Specifically, the system moves the origin of the coordinate space to a shared location, which it derives from the template in the [`spatialTemplatePreference`](systemcoordinator/configuration-swift.struct/spatialtemplatepreference.md) property. Any content you place in the immersive space subsequently appears in the correct relative location from each participant’s perspective.

To place content in front of a specific participant, observe updates to [`remoteParticipantStates`](systemcoordinator/remoteparticipantstates.md) to retrieve a mapping between each remote participant and their current state. Access the seat and pose properties of `SystemCoordinator.ParticipantState` to determine where remote participants are positioned in the shared space and place content in front of them.

```swift
Task {
    let observedRemoteParticipantStates = Observations {
        return systemCoordinator.remoteParticipantStates
    }
    for await observedRemoteParticipantState in observedRemoteParticipantStates {
        for (participant, state) in observedRemoteParticipantState {
            // Access seat and pose for each participant and handle changes.
            updateRemoteParticipantPosition(participant, participantState.pose)
        }
    }
}
```

For more information and examples, see [`Building a guessing game for visionOS`](building-a-guessing-game-for-visionos.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/systemcoordinator/configuration-swift.struct/supportsgroupimmersivespace)*