# CLMonitor.Event

**Framework**: Core Location  
**Kind**: struct  
**Role**: Structure

An event object that the framework passes to the events sequence in the monitor.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
struct Event
```

#### Overview

The framework delivers these events to an asynchronous sequence in the monitor that your app processes.

## Topics

### Event states
- [var accuracyLimited: Bool](./event/accuracylimited.md)
  A Boolean value that indicates whether the app receives accuracy-limited location updates.
- [var authorizationDenied: Bool](./event/authorizationdenied.md)
  A Boolean value that indicates whether the app has local authorization.
- [var authorizationDeniedGlobally: Bool](./event/authorizationdeniedglobally.md)
  A Boolean value that indicates whether the app has system-wide authorization.
- [var authorizationRequestInProgress: Bool](./event/authorizationrequestinprogress.md)
- [var authorizationRestricted: Bool](./event/authorizationrestricted.md)
  A Boolean value that indicates whether the app can make authorization changes.
- [var conditionLimitExceeded: Bool](./event/conditionlimitexceeded.md)
  A Boolean value that indicates whether the app receives location updates based on other monitoring conditions.
- [var conditionUnsupported: Bool](./event/conditionunsupported.md)
  A Boolean value that indicates whether the app receives location updates based on the supported condition.
- [var insufficientlyInUse: Bool](./event/insufficientlyinuse.md)
  A Boolean value that indicates whether the app receives location updates because it’s insufficiently in use.
- [var persistenceUnavailable: Bool](./event/persistenceunavailable.md)
  A Boolean value that indicates whether it receives location updates based on successful persistence.
- [var serviceSessionRequired: Bool](./event/servicesessionrequired.md)
### Event characteristics
- [var date: Date](./event/date.md)
  A date indicating the time of the event.
- [var identifier: String](./event/identifier.md)
  A string that identifies the event.
- [let refinement: (any CLCondition)?](./event/refinement.md)
  An optional instance of a condition that represents the most specific condition that this event can apply to.
- [var state: CLMonitor.Event.State](./event/state-swift.property.md)
  The event’s state.
### Type aliases
- [CLMonitor.Event.State](./event/state-swift.typealias.md)
  The type that represents the state of the monitoring event.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Monitor events
- [CLMonitor.Record](./record.md)
  A structure that represents a condition and its associated event information that the framework is monitoring.
- [CLMonitor.Events](./events-swift.struct.md)
  A type that represents an asynchronous sequence of events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/event)*