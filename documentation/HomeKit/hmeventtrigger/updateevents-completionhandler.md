# updateEvents(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Updates the set of trigger events.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func updateEvents(_ events: [HMEvent]) async throws
```

## Parameters

- `events`: An array of events that replaces the events on the trigger.
- `completion`: The block takes the following parameter:

## See Also

- [var events: [HMEvent]](hmeventtrigger/events.md)
  The events that activate the trigger.
- [Location events](location-events.md)
  Events that represent the user’s movement among regions.
- [Time events](time-events.md)
  Events based on time, significant occurrences, and time durations.
- [Characteristic events](characteristic-events.md)
  Events based on the capabilities or characteristics of accessories.
- [Presence events](presence-events.md)
  Events based on the user’s presence in a home.
- [class HMEvent](hmevent.md)
  The abstract base class for a HomeKit event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtrigger/updateevents(_:completionhandler:))*