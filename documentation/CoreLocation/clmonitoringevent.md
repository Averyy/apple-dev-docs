# CLMonitoringEvent

**Framework**: Core Location  
**Kind**: class  
**Role**: Class

The object that the framework passes to the monitor’s callback handler upon receiving an event.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```objc
@interface CLMonitoringEvent : NSObject
```

#### Overview

Instances of `CLMonitoringEvent` contain detailed information about an event in the monitoring of a [`CLCondition`](./clcondition-swift.protocol.md) by a [`CLMonitor`](./clmonitor-2r51v.md).

## Topics

### Event states
- [accuracyLimited](./clmonitoringevent/accuracylimited.md)
  A Boolean value that indicates whether the app receives accuracy-limited location updates.
- [authorizationDenied](./clmonitoringevent/authorizationdenied.md)
  A Boolean value that indicates whether the app has local authorization.
- [authorizationDeniedGlobally](./clmonitoringevent/authorizationdeniedglobally.md)
  A Boolean value that indicates whether the app has system-wide authorization.
- [authorizationRequestInProgress](./clmonitoringevent/authorizationrequestinprogress.md)
- [authorizationRestricted](./clmonitoringevent/authorizationrestricted.md)
  A Boolean value that indicates whether the app can make authorization changes.
- [conditionLimitExceeded](./clmonitoringevent/conditionlimitexceeded.md)
  A Boolean value that indicates whether the app receives location updates based on other monitoring conditions.
- [conditionUnsupported](./clmonitoringevent/conditionunsupported.md)
  A Boolean value that indicates whether the app receives location updates based on the supported condition.
- [insufficientlyInUse](./clmonitoringevent/insufficientlyinuse.md)
  A Boolean value that indicates whether the app receives location updates because it’s insufficiently in use.
- [persistenceUnavailable](./clmonitoringevent/persistenceunavailable.md)
  A Boolean value that indicates whether it receives location updates based on successful persistence.
- [serviceSessionRequired](./clmonitoringevent/servicesessionrequired.md)
### Event properties
- [date](./clmonitoringevent/date.md)
  The date the event occurs.
- [identifier](./clmonitoringevent/identifier.md)
  A string that represents the identifier of a monitored condition.
- [refinement](./clmonitoringevent/refinement.md)
  An optional instance of a condition that represents the most specific condition to that this event can apply to.
- [state](./clmonitoringevent/state.md)
  The state of the condition at the time of the event.
- [CLMonitoringState](./clmonitoringstate.md)
  Values that represent the current state of a monitoring condition.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Location monitor events
- [CLMonitoringRecord](./clmonitoringrecord.md)
  An object that represents a condition and its associated information that a location monitor is monitoring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitoringevent)*