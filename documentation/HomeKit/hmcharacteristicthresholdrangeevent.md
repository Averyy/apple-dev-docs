# HMCharacteristicThresholdRangeEvent

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

An event that triggers when the value of a characteristic is within a specified range.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class HMCharacteristicThresholdRangeEvent
```

```objc
@interface HMCharacteristicThresholdRangeEvent : HMEvent
```

## Topics

### Creating a characteristic threshold range event
- [init(characteristic: HMCharacteristic, thresholdRange: HMNumberRange)](./hmcharacteristicthresholdrangeevent/init%28characteristic,thresholdrange%29.md)
  Creates a characteristic threshold range event for the specified characteristic and number range.
### Inspecting a characteristic threshold event
- [var characteristic: HMCharacteristic](./hmcharacteristicthresholdrangeevent/characteristic.md)
  The characteristic associated with the event.
- [var thresholdRange: HMNumberRange](./hmcharacteristicthresholdrangeevent/thresholdrange.md)
  The range of the characteristic value that triggers the event.

## Relationships

### Inherits From
- [HMEvent](./hmevent.md)
### Inherited By
- [HMMutableCharacteristicThresholdRangeEvent](./hmmutablecharacteristicthresholdrangeevent.md)
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
- [class HMMutableCharacteristicThresholdRangeEvent](./hmmutablecharacteristicthresholdrangeevent.md)
  A mutable event that triggers when the value of a characteristic is within a specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristicthresholdrangeevent)*