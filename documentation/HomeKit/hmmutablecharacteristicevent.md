# HMMutableCharacteristicEvent

**Framework**: HomeKit  
**Kind**: class

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

## Topics

### Configuring the event
- [var characteristic: HMCharacteristic](hmmutablecharacteristicevent/characteristic.md)
  The characteristic associated with the event.
- [var triggerValue: TriggerValueType?](hmmutablecharacteristicevent/triggervalue.md)
  The value of the characteristic that triggers the event.

## Relationships

### Inherits From
- [HMCharacteristicEvent](hmcharacteristicevent.md)
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

- [class HMCharacteristicEvent](hmcharacteristicevent.md)
  An event that is evaluated based on the value of a characteristic.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmmutablecharacteristicevent)*