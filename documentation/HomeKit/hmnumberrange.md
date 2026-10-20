# HMNumberRange

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HMNumberRange : NSObject
```

## Topics

### Creating a number range
- [convenience init(minValue: NSNumber, maxValue: NSNumber)](./hmnumberrange/init%28minvalue,maxvalue%29.md)
  Creates a new number range.
- [convenience init(minValue: NSNumber)](./hmnumberrange/init%28minvalue%29.md)
  Creates an one-sided number range with a minimum value.
- [convenience init(maxValue: NSNumber)](./hmnumberrange/init%28maxvalue%29.md)
  Creates a one-sided number range with a maximum value.
### Inspecting a number range
- [var minValue: NSNumber?](./hmnumberrange/minvalue.md)
  The minimum value of the range.
- [var maxValue: NSNumber?](./hmnumberrange/maxvalue.md)
  The maximum value of the range.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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

### Characteristic ranges
- [class HMCharacteristicThresholdRangeEvent](./hmcharacteristicthresholdrangeevent.md)
  An event that triggers when the value of a characteristic is within a specified range.
- [class HMMutableCharacteristicThresholdRangeEvent](./hmmutablecharacteristicthresholdrangeevent.md)
  A mutable event that triggers when the value of a characteristic is within a specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmnumberrange)*