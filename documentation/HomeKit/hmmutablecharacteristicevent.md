# HMMutableCharacteristicEvent

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

A mutable event that is evaluated based on the value of a characteristic.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class HMMutableCharacteristicEvent<TriggerValueType> where TriggerValueType : NSCopying
```

```objc
@interface HMMutableCharacteristicEvent : HMCharacteristicEvent
```

## Topics

### Configuring the event
- [var characteristic: HMCharacteristic](./hmmutablecharacteristicevent/characteristic.md)
  The characteristic associated with the event.
- [var triggerValue: TriggerValueType?](./hmmutablecharacteristicevent/triggervalue.md)
  The value of the characteristic that triggers the event.

## Relationships

### Inherits From
- [HMCharacteristicEvent](./hmcharacteristicevent.md)
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
- [class HMCharacteristicEvent](./hmcharacteristicevent.md)
  An event that is evaluated based on the value of a characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmmutablecharacteristicevent)*