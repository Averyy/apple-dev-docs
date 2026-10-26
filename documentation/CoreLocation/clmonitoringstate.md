# CLMonitoringState

**Framework**: Core Location  
**Kind**: enum  
**Role**: Enumeration

Values that represent the current state of a monitoring condition.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
enum CLMonitoringState : NSUInteger;
```

## Topics

### Condition states
- [CLMonitoringStateSatisfied](./clmonitoringstate/clmonitoringstatesatisfied.md)
  The condition is in a satisfied state.
- [CLMonitoringStateUnknown](./clmonitoringstate/clmonitoringstateunknown.md)
  The condition is in an unknown state.
- [CLMonitoringStateUnsatisfied](./clmonitoringstate/clmonitoringstateunsatisfied.md)
  The condition is in an unsatisfied state.
- [CLMonitoringStateUnmonitored](./clmonitoringstate/clmonitoringstateunmonitored.md)
  The condition is in an unmonitored state.

## See Also

### Event properties
- [date](./clmonitoringevent/date.md)
  The date the event occurs.
- [identifier](./clmonitoringevent/identifier.md)
  A string that represents the identifier of a monitored condition.
- [refinement](./clmonitoringevent/refinement.md)
  An optional instance of a condition that represents the most specific condition to that this event can apply to.
- [state](./clmonitoringevent/state.md)
  The state of the condition at the time of the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitoringstate)*