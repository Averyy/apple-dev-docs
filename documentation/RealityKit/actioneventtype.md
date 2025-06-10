# ActionEventType

**Framework**: RealityKit  
**Kind**: struct

A set of events that an action responds to.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
struct ActionEventType
```

#### Overview

Actions can respond to specific events with one or more custom event handlers that you associate with each event type.

RealityKit calls the event handlers when the animation time enters, exits, or continues within a time interval for an [`ActionEventDefinition`](actioneventdefinition.md).

A time interval for an event begins at its starting time and spans up to, but doesn’t include, the event’s starting time plus its duration.

## Topics

### Event types
- [static var started: ActionEventType](actioneventtype/started.md)
  An event that takes place when a new action event begins.
- [static var ended: ActionEventType](actioneventtype/ended.md)
  An event that takes place when the action event exits its time interval.
- [static var paused: ActionEventType](actioneventtype/paused.md)
  An event that takes place when the animation pauses.
- [static var resumed: ActionEventType](actioneventtype/resumed.md)
  An event that takes place when the animation resumes after a pause.
- [static var updated: ActionEventType](actioneventtype/updated.md)
  An event that takes place after an action event starts and is within its time interval.
- [static var skipped: ActionEventType](actioneventtype/skipped.md)
  An event that takes place when the system misses an action event’s time interval.
- [static var terminated: ActionEventType](actioneventtype/terminated.md)
  An event that takes place when the animation ends.
### Protocol support
- [init(rawValue: UInt)](actioneventtype/init(rawvalue:).md)
  Creates an action event type from a raw value.
- [let rawValue: UInt](actioneventtype/rawvalue.md)
  The backing storage for action event types.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [struct ActionEvent](actionevent.md)
  The structure returned to all action event handlers.
- [struct AnimationState](animationstate.md)
  The concretely typed animation state structure.
- [struct ActionEventDefinition](actioneventdefinition.md)
  Defines an action event interval, and any associated parameters.
- [protocol AnimationStateProtocol](animationstateprotocol.md)
  The protocol representing the current animation state of an action animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/actioneventtype)*