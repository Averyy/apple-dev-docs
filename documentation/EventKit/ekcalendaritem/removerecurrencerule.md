# removeRecurrenceRule(_:)

**Framework**: EventKit  
**Kind**: method

Removes a recurrence rule from the recurrence rule array.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func removeRecurrenceRule(_ rule: EKRecurrenceRule)
```

#### Discussion

The implementation only supports a single recurrence rule.

## Parameters

- `rule`: The rule to be removed from  .

## See Also

- [var hasRecurrenceRules: Bool](ekcalendaritem/hasrecurrencerules.md)
  A Boolean value that indicates whether the calendar item has recurrence rules.
- [func addRecurrenceRule(EKRecurrenceRule)](ekcalendaritem/addrecurrencerule(_:).md)
  Adds a recurrence rule to the recurrence rule array.
- [var recurrenceRules: [EKRecurrenceRule]?](ekcalendaritem/recurrencerules.md)
  The recurrence rules for the calendar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendaritem/removerecurrencerule(_:))*