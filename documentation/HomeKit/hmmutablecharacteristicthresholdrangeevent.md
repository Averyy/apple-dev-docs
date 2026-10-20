# HMMutableCharacteristicThresholdRangeEvent

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

A mutable event that triggers when the value of a characteristic is within a specified range.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class HMMutableCharacteristicThresholdRangeEvent
```

```objc
@interface HMMutableCharacteristicThresholdRangeEvent : HMCharacteristicThresholdRangeEvent
```

## Topics

### Configuring a characteristic threshold event
- [var characteristic: HMCharacteristic](./hmmutablecharacteristicthresholdrangeevent/characteristic.md)
  The characteristic associated with the event.
- [var thresholdRange: HMNumberRange](./hmmutablecharacteristicthresholdrangeevent/thresholdrange.md)
  The range of the characteristic value that triggers the event.

## Relationships

### Inherits From
- [HMCharacteristicThresholdRangeEvent](./hmcharacteristicthresholdrangeevent.md)
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

### Characteristic ranges
- [class HMNumberRange](./hmnumberrange.md)
  A set of numbers used to specify conditions for characteristic range threshold events.
- [class HMCharacteristicThresholdRangeEvent](./hmcharacteristicthresholdrangeevent.md)
  An event that triggers when the value of a characteristic is within a specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmmutablecharacteristicthresholdrangeevent)*