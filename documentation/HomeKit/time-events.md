# Time events

**Framework**: HomeKit

Events based on time, significant occurrences, and time durations.

## Topics

### Dates and times
- [class HMCalendarEvent](hmcalendarevent.md)
  An event that fires at a specified time.
- [class HMMutableCalendarEvent](hmmutablecalendarevent.md)
  A mutable event that fires at a specified time.
- [class HMTimeEvent](hmtimeevent.md)
  An abstract superclass for time-based events.
### Significant events
- [struct HMSignificantEvent](hmsignificantevent.md)
  An event that represents significant time-based events, including sunrise and sunset.
- [class HMSignificantTimeEvent](hmsignificanttimeevent.md)
  An event that fires at a time offset from a significant time-based event.
- [class HMMutableSignificantTimeEvent](hmmutablesignificanttimeevent.md)
  A mutable event that fires at the specified temporal offset to a significant event.
### Durations
- [class HMDurationEvent](hmdurationevent.md)
  An event that ends after the specified time duration.
- [class HMMutableDurationEvent](hmmutabledurationevent.md)
  A mutable event that fires after the specified time duration.

## See Also

- [var events: [HMEvent]](hmeventtrigger/events.md)
  The events that activate the trigger.
- [func updateEvents([HMEvent], completionHandler: ((any Error)?) -> Void)](hmeventtrigger/updateevents(_:completionhandler:).md)
  Updates the set of trigger events.
- [Location events](location-events.md)
  Events that represent the user’s movement among regions.
- [Characteristic events](characteristic-events.md)
  Events based on the capabilities or characteristics of accessories.
- [Presence events](presence-events.md)
  Events based on the user’s presence in a home.
- [class HMEvent](hmevent.md)
  The abstract base class for a HomeKit event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/time-events)*