# frequency

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The time frame for which the rule applies.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var frequency: INRecurrenceFrequency { get }
```

```objc
@property (nonatomic, readonly) INRecurrenceFrequency frequency;
```

## Discussion

This property represents the time frame over which a date or time recurs. For example, applying a recurrence rule with the frequency of [`INRecurrenceFrequency.daily`](../inrecurrencefrequency/daily.md) to date components containing the hour of 7:00 would let you create a trigger that applies at 7:00 each day.

Use the [`interval`](./interval.md) property to create gaps in the repetition of the specified date.

## See Also

### Getting the Rule Conditions
- [enum INRecurrenceFrequency](../inrecurrencefrequency.md)
  The time frame for which the rule applies.
- [var interval: Int](./interval.md)
  The interval at which the recurrence rule is applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrecurrencerule/frequency)*