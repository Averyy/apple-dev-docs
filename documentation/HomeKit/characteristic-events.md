# Characteristic events

**Framework**: HomeKit

Events based on the capabilities or characteristics of accessories.

## Topics

### Characteristics
- [class HMCharacteristicEvent](hmcharacteristicevent.md)
  An event that is evaluated based on the value of a characteristic.
- [class HMMutableCharacteristicEvent](hmmutablecharacteristicevent.md)
  A mutable event that is evaluated based on the value of a characteristic.
### Characteristic ranges
- [class HMNumberRange](hmnumberrange.md)
  A set of numbers used to specify conditions for characteristic range threshold events.
- [class HMCharacteristicThresholdRangeEvent](hmcharacteristicthresholdrangeevent.md)
  An event that triggers when the value of a characteristic is within a specified range.
- [class HMMutableCharacteristicThresholdRangeEvent](hmmutablecharacteristicthresholdrangeevent.md)
  A mutable event that triggers when the value of a characteristic is within a specified range.

## See Also

- [var events: [HMEvent]](hmeventtrigger/events.md)
  The events that activate the trigger.
- [func updateEvents([HMEvent], completionHandler: ((any Error)?) -> Void)](hmeventtrigger/updateevents(_:completionhandler:).md)
  Updates the set of trigger events.
- [Location events](location-events.md)
  Events that represent the user’s movement among regions.
- [Time events](time-events.md)
  Events based on time, significant occurrences, and time durations.
- [Presence events](presence-events.md)
  Events based on the user’s presence in a home.
- [class HMEvent](hmevent.md)
  The abstract base class for a HomeKit event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/characteristic-events)*