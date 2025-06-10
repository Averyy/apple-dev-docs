# HMMutableCharacteristicThresholdRangeEvent

**Framework**: HomeKit  
**Kind**: class

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

## Topics

### Configuring a characteristic threshold event
- [var characteristic: HMCharacteristic](hmmutablecharacteristicthresholdrangeevent/characteristic.md)
  The characteristic associated with the event.
- [var thresholdRange: HMNumberRange](hmmutablecharacteristicthresholdrangeevent/thresholdrange.md)
  The range of the characteristic value that triggers the event.

## Relationships

### Inherits From
- [HMCharacteristicThresholdRangeEvent](hmcharacteristicthresholdrangeevent.md)
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
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class HMNumberRange](hmnumberrange.md)
  A set of numbers used to specify conditions for characteristic range threshold events.
- [class HMCharacteristicThresholdRangeEvent](hmcharacteristicthresholdrangeevent.md)
  An event that triggers when the value of a characteristic is within a specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmmutablecharacteristicthresholdrangeevent)*