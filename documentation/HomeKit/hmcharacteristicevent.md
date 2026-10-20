# HMCharacteristicEvent

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HMCharacteristicEvent : HMEvent
```

## Topics

### Creating a characteristic event
- [init(characteristic: HMCharacteristic, triggerValue: TriggerValueType?)](./hmcharacteristicevent/init%28characteristic,triggervalue%29.md)
  Creates a new characteristic event which triggers when the specified characteristic reaches the specified value.
### Inspecting the event
- [var characteristic: HMCharacteristic](./hmcharacteristicevent/characteristic.md)
  The characteristic associated with the event.
- [var triggerValue: TriggerValueType?](./hmcharacteristicevent/triggervalue.md)
  The value of the characteristic that triggers the event.
### Configuring the event
- [func updateTriggerValue(TriggerValueType?, completionHandler: ((any Error)?) -> Void)](./hmcharacteristicevent/updatetriggervalue%28_,completionhandler%29.md)
  Changes the trigger value associated with this event.

## Relationships

### Inherits From
- [HMEvent](./hmevent.md)
### Inherited By
- [HMMutableCharacteristicEvent](./hmmutablecharacteristicevent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSMutableCopying](../Foundation/nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Characteristics
- [class HMMutableCharacteristicEvent](./hmmutablecharacteristicevent.md)
  A mutable event that is evaluated based on the value of a characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicevent)*