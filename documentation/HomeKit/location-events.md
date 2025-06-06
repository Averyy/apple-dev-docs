# Location events

**Framework**: HomeKit

Events that represent the user’s movement among regions.

## Topics

### Locations
- [class HMLocationEvent](hmlocationevent.md)
  An event that is evaluated based on entry to or exit from a region.
- [class HMMutableLocationEvent](hmmutablelocationevent.md)
  A mutable event that is evaluated based on entry to or exit from a region.

## See Also

- [var events: [HMEvent]](hmeventtrigger/events.md)
  The events that activate the trigger.
- [func updateEvents([HMEvent], completionHandler: ((any Error)?) -> Void)](hmeventtrigger/updateevents(_:completionhandler:).md)
  Updates the set of trigger events.
- [Time events](time-events.md)
  Events based on time, significant occurrences, and time durations.
- [Characteristic events](characteristic-events.md)
  Events based on the capabilities or characteristics of accessories.
- [Presence events](presence-events.md)
  Events based on the user’s presence in a home.
- [class HMEvent](hmevent.md)
  The abstract base class for a HomeKit event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/location-events)*