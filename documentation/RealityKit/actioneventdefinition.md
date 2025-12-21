# ActionEventDefinition

**Framework**: RealityKit  
**Kind**: struct

Defines an action event interval, and any associated parameters.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct ActionEventDefinition<ActionType> where ActionType : EntityAction
```

#### Overview

Start, update, end, and skipped events are raised based on one or more event intervals defined by the action animation.

Also see: [`ActionEventType`](actioneventtype.md)

## Topics

### Initializers
- [init(startTime: TimeInterval, duration: TimeInterval, parameter: ActionEventDefinition<ActionType>.EventParameterType?)](actioneventdefinition/init(starttime:duration:parameter:).md)
  Constructs an event definition.
### Instance Properties
- [var duration: TimeInterval](actioneventdefinition/duration.md)
  The event interval’s duration.
- [var parameter: ActionEventDefinition<ActionType>.EventParameterType?](actioneventdefinition/parameter.md)
  Optional parameter data available to the event handler at the time of the event.
- [var startTime: TimeInterval](actioneventdefinition/starttime.md)
  The time at which the event interval starts.
### Type Aliases
- [ActionEventDefinition.EventParameterType](actioneventdefinition/eventparametertype.md)

## See Also

- [struct ActionEvent](actionevent.md)
  The structure returned to all action event handlers.
- [struct AnimationState](animationstate.md)
  The concretely typed animation state structure.
- [struct ActionEventType](actioneventtype.md)
  A set of events that an action responds to.
- [protocol AnimationStateProtocol](animationstateprotocol.md)
  The protocol representing the current animation state of an action animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actioneventdefinition)*