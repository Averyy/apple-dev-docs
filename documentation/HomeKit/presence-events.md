# Presence events

**Framework**: HomeKit

Events based on the user’s presence in a home.

## Topics

### User presence
- [class HMPresenceEvent](hmpresenceevent.md)
  An event that triggers based on the presence of users in the home.
- [class HMMutablePresenceEvent](hmmutablepresenceevent.md)
  A mutable event that triggers based on the presence of users in the home.
- [enum HMPresenceEventType](hmpresenceeventtype.md)
  The user presence type that triggers a presence event.
- [enum HMPresenceEventUserType](hmpresenceeventusertype.md)
  The group of users that triggers a presence event.

## See Also

- [var events: [HMEvent]](hmeventtrigger/events.md)
  The events that activate the trigger.
- [func updateEvents([HMEvent], completionHandler: ((any Error)?) -> Void)](hmeventtrigger/updateevents(_:completionhandler:).md)
  Updates the set of trigger events.
- [Location events](location-events.md)
  Events that represent the user’s movement among regions.
- [Time events](time-events.md)
  Events based on time, significant occurrences, and time durations.
- [Characteristic events](characteristic-events.md)
  Events based on the capabilities or characteristics of accessories.
- [class HMEvent](hmevent.md)
  The abstract base class for a HomeKit event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/presence-events)*