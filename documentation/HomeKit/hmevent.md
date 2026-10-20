# HMEvent

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HMEvent : NSObject
```

## Topics

### Getting information about the event
- [var uniqueIdentifier: UUID](./hmevent/uniqueidentifier.md)
  A unique identifier for the event.
- [class func isSupported(for: HMHome) -> Bool](./hmevent/issupported%28for%29.md)
  A Boolean value indicating whether the event can be added to an event trigger on the specified home.
### Initializers
- [init()](./hmevent/init%28%29.md)
### Type Methods
- [class func new() -> Self](./hmevent/new%28%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [HMCharacteristicEvent](./hmcharacteristicevent.md)
- [HMCharacteristicThresholdRangeEvent](./hmcharacteristicthresholdrangeevent.md)
- [HMLocationEvent](./hmlocationevent.md)
- [HMPresenceEvent](./hmpresenceevent.md)
- [HMTimeEvent](./hmtimeevent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Setting trigger events
- [var events: [HMEvent]](./hmeventtrigger/events.md)
  The events that activate the trigger.
- [func updateEvents([HMEvent], completionHandler: ((any Error)?) -> Void)](./hmeventtrigger/updateevents%28_,completionhandler%29.md)
  Updates the set of trigger events.
- [Location events](./location-events.md)
  Events that represent the user’s movement among regions.
- [Time events](./time-events.md)
  Events based on time, significant occurrences, and time durations.
- [Characteristic events](./characteristic-events.md)
  Events based on the capabilities or characteristics of accessories.
- [Presence events](./presence-events.md)
  Events based on the user’s presence in a home.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmevent)*