# ActionEvent

**Framework**: RealityKit  
**Kind**: struct

The structure returned to all action event handlers.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
struct ActionEvent<ActionType> where ActionType : EntityAction
```

#### Overview

Actions perform their function within one or more custom event handlers associated with an action type.

The event structure contains useful information for an action to perform its function when an action event is raised.

## Topics

### Instance Properties
- [let action: ActionType](actionevent/action.md)
  The action parameter data that remains constant across one or more events intervals defined for the action animation.
- [var animationState: (any AnimationStateProtocol)?](actionevent/animationstate.md)
  The animation state for the action.
- [let duration: TimeInterval](actionevent/duration.md)
  The duration of the the event.
- [let parameter: ActionType.EventParameterType?](actionevent/parameter.md)
  The event parameter data that can vary for each event.
- [let playbackController: AnimationPlaybackController](actionevent/playbackcontroller.md)
  The animation playback controller that manages the animation executing the action.
- [let reversed: Bool](actionevent/reversed.md)
  A Boolean value that indicates reverse playback when true.
- [let startTime: TimeInterval](actionevent/starttime.md)
  The start time of the current event.
- [let targetEntity: Entity?](actionevent/targetentity.md)
  The entity the bind target references.

## See Also

- [struct AnimationState](animationstate.md)
  The concretely typed animation state structure.
- [struct ActionEventType](actioneventtype.md)
  A set of events that an action responds to.
- [struct ActionEventDefinition](actioneventdefinition.md)
  Defines an action event interval, and any associated parameters.
- [protocol AnimationStateProtocol](animationstateprotocol.md)
  The protocol representing the current animation state of an action animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actionevent)*