# addRecurrenceRule(_:)

**Framework**: EventKit  
**Kind**: method

Adds a recurrence rule to the recurrence rule array.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func addRecurrenceRule(_ rule: EKRecurrenceRule)
```

## Mentions

- [Creating a recurring event](creating-a-recurring-event.md)
- [Creating events and reminders](creating-events-and-reminders.md)

#### Discussion

The implementation only supports a single recurrence rule. Adding a recurrence rule replaces the single recurrence rule.

## Parameters

- `rule`: The rule to be added to  .

## See Also

- [var hasRecurrenceRules: Bool](ekcalendaritem/hasrecurrencerules.md)
  A Boolean value that indicates whether the calendar item has recurrence rules.
- [func removeRecurrenceRule(EKRecurrenceRule)](ekcalendaritem/removerecurrencerule(_:).md)
  Removes a recurrence rule from the recurrence rule array.
- [var recurrenceRules: [EKRecurrenceRule]?](ekcalendaritem/recurrencerules.md)
  The recurrence rules for the calendar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendaritem/addrecurrencerule(_:))*