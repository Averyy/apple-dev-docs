# HMEvent

**Framework**: HomeKit  
**Kind**: class

The abstract base class for a HomeKit event.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HMEvent
```

## Topics

### Getting information about the event
- [var uniqueIdentifier: UUID](hmevent/uniqueidentifier.md)
  A unique identifier for the event.
- [class func isSupported(for: HMHome) -> Bool](hmevent/issupported(for:).md)
  A Boolean value indicating whether the event can be added to an event trigger on the specified home.
### Initializers
- [init()](hmevent/init.md)
### Type Methods
- [class func new() -> Self](hmevent/new.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [HMCharacteristicEvent](hmcharacteristicevent.md)
- [HMCharacteristicThresholdRangeEvent](hmcharacteristicthresholdrangeevent.md)
- [HMLocationEvent](hmlocationevent.md)
- [HMPresenceEvent](hmpresenceevent.md)
- [HMTimeEvent](hmtimeevent.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

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
- [Presence events](presence-events.md)
  Events based on the user’s presence in a home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmevent)*