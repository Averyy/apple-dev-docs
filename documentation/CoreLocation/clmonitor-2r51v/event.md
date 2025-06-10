# CLMonitor.Event

**Framework**: Core Location  
**Kind**: struct

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
- [var accuracyLimited: Bool](clmonitor-2r51v/event/accuracylimited.md)
  A Boolean value that indicates whether the app receives accuracy-limited location updates.
- [var authorizationDenied: Bool](clmonitor-2r51v/event/authorizationdenied.md)
  A Boolean value that indicates whether the app has local authorization.
- [var authorizationDeniedGlobally: Bool](clmonitor-2r51v/event/authorizationdeniedglobally.md)
  A Boolean value that indicates whether the app has system-wide authorization.
- [var authorizationRequestInProgress: Bool](clmonitor-2r51v/event/authorizationrequestinprogress.md)
- [var authorizationRestricted: Bool](clmonitor-2r51v/event/authorizationrestricted.md)
  A Boolean value that indicates whether the app can make authorization changes.
- [var conditionLimitExceeded: Bool](clmonitor-2r51v/event/conditionlimitexceeded.md)
  A Boolean value that indicates whether the app receives location updates based on other monitoring conditions.
- [var conditionUnsupported: Bool](clmonitor-2r51v/event/conditionunsupported.md)
  A Boolean value that indicates whether the app receives location updates based on the supported condition.
- [var insufficientlyInUse: Bool](clmonitor-2r51v/event/insufficientlyinuse.md)
  A Boolean value that indicates whether the app receives location updates because it’s insufficiently in use.
- [var persistenceUnavailable: Bool](clmonitor-2r51v/event/persistenceunavailable.md)
  A Boolean value that indicates whether it receives location updates based on successful persistence.
- [var serviceSessionRequired: Bool](clmonitor-2r51v/event/servicesessionrequired.md)
### Event characteristics
- [var date: Date](clmonitor-2r51v/event/date.md)
  A date indicating the time of the event.
- [var identifier: String](clmonitor-2r51v/event/identifier.md)
  A string that identifies the event.
- [let refinement: (any CLCondition)?](clmonitor-2r51v/event/refinement.md)
  An optional instance of a condition that represents the most specific condition that this event can apply to.
- [var state: CLMonitor.Event.State](clmonitor-2r51v/event/state-swift.property.md)
  The event’s state.
### Type aliases
- [CLMonitor.Event.State](clmonitor-2r51v/event/state-swift.typealias.md)
  The type that represents the state of the monitoring event.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [CLMonitor.Record](clmonitor-2r51v/record.md)
  A structure that represents a condition and its associated event information that the framework is monitoring.
- [CLMonitor.Events](clmonitor-2r51v/events-swift.struct.md)
  A type that represents an asynchronous sequence of events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/event)*