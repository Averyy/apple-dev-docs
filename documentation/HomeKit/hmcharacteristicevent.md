# HMCharacteristicEvent

**Framework**: HomeKit  
**Kind**: class

An event that is evaluated based on the value of a characteristic.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class HMCharacteristicEvent<TriggerValueType> where TriggerValueType : NSCopying
```

## Topics

### Creating a characteristic event
- [init(characteristic: HMCharacteristic, triggerValue: TriggerValueType?)](hmcharacteristicevent/init(characteristic:triggervalue:).md)
  Creates a new characteristic event which triggers when the specified characteristic reaches the specified value.
### Inspecting the event
- [var characteristic: HMCharacteristic](hmcharacteristicevent/characteristic.md)
  The characteristic associated with the event.
- [var triggerValue: TriggerValueType?](hmcharacteristicevent/triggervalue.md)
  The value of the characteristic that triggers the event.
### Configuring the event
- [func updateTriggerValue(TriggerValueType?, completionHandler: ((any Error)?) -> Void)](hmcharacteristicevent/updatetriggervalue(_:completionhandler:).md)
  Changes the trigger value associated with this event.

## Relationships

### Inherits From
- [HMEvent](hmevent.md)
### Inherited By
- [HMMutableCharacteristicEvent](hmmutablecharacteristicevent.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class HMMutableCharacteristicEvent](hmmutablecharacteristicevent.md)
  A mutable event that is evaluated based on the value of a characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicevent)*