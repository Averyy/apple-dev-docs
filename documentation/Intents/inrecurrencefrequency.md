# INRecurrenceFrequency

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

The time frame for which the rule applies.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
enum INRecurrenceFrequency
```

```c
enum INRecurrenceFrequency : NSInteger;
```

## Topics

### Enumeration Cases
- [INRecurrenceFrequency.unknown](./inrecurrencefrequency/unknown.md)
  An unknown repetition frequency.
- [INRecurrenceFrequency.minute](./inrecurrencefrequency/minute.md)
  A time range that repeats every minute.
- [INRecurrenceFrequency.hourly](./inrecurrencefrequency/hourly.md)
  A time range that repeats on an hourly basis.
- [INRecurrenceFrequency.daily](./inrecurrencefrequency/daily.md)
  A time range that repeats on a daily basis.
- [INRecurrenceFrequency.weekly](./inrecurrencefrequency/weekly.md)
  A date range that repeats on a weekly basis.
- [INRecurrenceFrequency.monthly](./inrecurrencefrequency/monthly.md)
  A date range that repeats on a monthly basis.
- [INRecurrenceFrequency.yearly](./inrecurrencefrequency/yearly.md)
  A date range that repeats on a yearly basis.
### Initializers
- [init?(rawValue: Int)](./inrecurrencefrequency/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Rule Conditions
- [var frequency: INRecurrenceFrequency](./inrecurrencerule/frequency.md)
  The time frame for which the rule applies.
- [var interval: Int](./inrecurrencerule/interval.md)
  The interval at which the recurrence rule is applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrecurrencefrequency)*