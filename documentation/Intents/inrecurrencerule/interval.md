# interval

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The interval at which the recurrence rule is applied.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var interval: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger interval;
```

## Discussion

This property allows you to define recurrence rules that skip a particular instance. For example, a rule whose frequency is [`INRecurrenceFrequency.weekly`](../inrecurrencefrequency/weekly.md) and whose interval is `2` represents a recurrence that occurs every two weeks, instead of every week.

## See Also

### Getting the Rule Conditions
- [var frequency: INRecurrenceFrequency](./frequency.md)
  The time frame for which the rule applies.
- [enum INRecurrenceFrequency](../inrecurrencefrequency.md)
  The time frame for which the rule applies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrecurrencerule/interval)*