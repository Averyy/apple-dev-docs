# HMNumberRange

**Framework**: HomeKit  
**Kind**: class

A set of numbers used to specify conditions for characteristic range threshold events.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class HMNumberRange
```

## Topics

### Creating a number range
- [convenience init(minValue: NSNumber, maxValue: NSNumber)](hmnumberrange/init(minvalue:maxvalue:).md)
  Creates a new number range.
- [convenience init(minValue: NSNumber)](hmnumberrange/init(minvalue:).md)
  Creates an one-sided number range with a minimum value.
- [convenience init(maxValue: NSNumber)](hmnumberrange/init(maxvalue:).md)
  Creates a one-sided number range with a maximum value.
### Inspecting a number range
- [var minValue: NSNumber?](hmnumberrange/minvalue.md)
  The minimum value of the range.
- [var maxValue: NSNumber?](hmnumberrange/maxvalue.md)
  The maximum value of the range.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class HMCharacteristicThresholdRangeEvent](hmcharacteristicthresholdrangeevent.md)
  An event that triggers when the value of a characteristic is within a specified range.
- [class HMMutableCharacteristicThresholdRangeEvent](hmmutablecharacteristicthresholdrangeevent.md)
  A mutable event that triggers when the value of a characteristic is within a specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmnumberrange)*