# recurrenceRules

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The recurrence rules for the calendar item.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var recurrenceRules: [EKRecurrenceRule]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<EKRecurrenceRule *> * recurrenceRules;
```

## Discussion

The implementation only supports a single recurrence rule.

## See Also

### Setting Recurrence Rules
- [var hasRecurrenceRules: Bool](./hasrecurrencerules.md)
  A Boolean value that indicates whether the calendar item has recurrence rules.
- [func addRecurrenceRule(EKRecurrenceRule)](./addrecurrencerule%28_%29.md)
  Adds a recurrence rule to the recurrence rule array.
- [func removeRecurrenceRule(EKRecurrenceRule)](./removerecurrencerule%28_%29.md)
  Removes a recurrence rule from the recurrence rule array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendaritem/recurrencerules)*