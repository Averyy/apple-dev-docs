# INRecurrenceRule

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An object that describes the pattern to use when repeating an event.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class INRecurrenceRule
```

```objc
@interface INRecurrenceRule : NSObject
```

## Overview

Use an [`INRecurrenceRule`](./inrecurrencerule.md) object to define a repeating pattern for date ranges. Typically, you use recurrence rules when defining date ranges that you associate with a trigger, such as an [`INTemporalEventTrigger`](./intemporaleventtrigger.md) object. Using a recurrence rule avoids the need to create a new trigger each time the old one fires.

## Topics

### Initializing a Recurrence Rule
- [convenience init(interval: Int, frequency: INRecurrenceFrequency)](./inrecurrencerule/init%28interval,frequency%29.md)
  Initializes the recurrence rule to the specified frequency and interval.
### Getting the Rule Conditions
- [var frequency: INRecurrenceFrequency](./inrecurrencerule/frequency.md)
  The time frame for which the rule applies.
- [enum INRecurrenceFrequency](./inrecurrencefrequency.md)
  The time frame for which the rule applies.
- [var interval: Int](./inrecurrencerule/interval.md)
  The interval at which the recurrence rule is applied.
### Initializers
- [init?(coder: NSCoder)](./inrecurrencerule/init%28coder%29.md)
- [init(interval: Int, frequency: INRecurrenceFrequency, weeklyRecurrenceDays: INDayOfWeekOptions)](./inrecurrencerule/init%28interval,frequency,weeklyrecurrencedays%29.md)
### Instance Properties
- [var weeklyRecurrenceDays: INDayOfWeekOptions](./inrecurrencerule/weeklyrecurrencedays.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Date
- [class INDateComponentsRange](./indatecomponentsrange.md)
  A span of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrecurrencerule)*