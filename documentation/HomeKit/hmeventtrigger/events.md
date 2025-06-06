# events

**Framework**: HomeKit  
**Kind**: property

The events that activate the trigger.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var events: [HMEvent] { get }
```

## See Also

- [func updateEvents([HMEvent], completionHandler: ((any Error)?) -> Void)](hmeventtrigger/updateevents(_:completionhandler:).md)
  Updates the set of trigger events.
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

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmeventtrigger/events)*