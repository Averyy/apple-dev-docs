# CLMonitor

**Framework**: Core Location  
**Kind**: class

An object that monitors the conditions you add to it.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
actor CLMonitor
```

## Mentions

- [Handling location updates in the background](handling-location-updates-in-the-background.md)

#### Overview

Use `CLMonitor` to monitor for and observe events such as the entry to a specific geographic area or proximity to a beacon with characteristics that you specify.

This service is unavailable in a compatible iPad or iPhone app running in visionOS.

## Topics

### Creating a monitor
- [init(String) async](clmonitor-2r51v/init(_:).md)
  Creates a location monitor with the name you specify.
### Adding and removing conditions
- [func add(any CLCondition, identifier: String)](clmonitor-2r51v/add(_:identifier:).md)
  Adds the given condition for monitoring.
- [func add(any CLCondition, identifier: String, assuming: CLMonitor.Event.State)](clmonitor-2r51v/add(_:identifier:assuming:).md)
  Adds the monitoring condition with the identifier and initial state you specify.
- [func record(for: String) -> CLMonitor.Record?](clmonitor-2r51v/record(for:).md)
  A record that contains a condition and the most recent event your app receives.
- [func remove(String)](clmonitor-2r51v/remove(_:).md)
  Removes the condition and its enclosed record associated with the identifier you provide.
### Accessing the location monitor’s identifiers
- [var identifiers: [String]](clmonitor-2r51v/identifiers.md)
  An array that contains the identifiers of the conditions the framework is monitoring.
### Accessing the monitor’s events
- [let events: CLMonitor.Events](clmonitor-2r51v/events-swift.property.md)
  An asynchronous sequence of events that represent the conditions the monitor object observes.
### Monitor conditions
- [CLMonitor.BeaconIdentityCondition](clmonitor-2r51v/beaconidentitycondition.md)
  A condition that describes the characteristics of a beacon.
- [CLMonitor.CircularGeographicCondition](clmonitor-2r51v/circulargeographiccondition.md)
  A condition that describes a circular geographic area that a center point and radius define.
### Monitor events
- [CLMonitor.Event](clmonitor-2r51v/event.md)
  An event object that the framework passes to the events sequence in the monitor.
- [CLMonitor.Record](clmonitor-2r51v/record.md)
  A structure that represents a condition and its associated event information that the framework is monitoring.
- [CLMonitor.Events](clmonitor-2r51v/events-swift.struct.md)
  A type that represents an asynchronous sequence of events.

## Relationships

### Conforms To
- [Actor](../Swift/Actor.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitor-2r51v)*