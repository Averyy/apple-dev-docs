# addRecurrenceRule(_:)

**Framework**: EventKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) addRecurrenceRule:(EKRecurrenceRule *) rule;
```

## Mentions

- [Creating a recurring event](../creating-a-recurring-event.md)
- [Creating events and reminders](../creating-events-and-reminders.md)

#### Discussion

The implementation only supports a single recurrence rule. Adding a recurrence rule replaces the single recurrence rule.

## Parameters

- `rule`: The rule to be added to [`recurrenceRules`](./recurrencerules.md).

## See Also

### Setting Recurrence Rules
- [var hasRecurrenceRules: Bool](./hasrecurrencerules.md)
  A Boolean value that indicates whether the calendar item has recurrence rules.
- [func removeRecurrenceRule(EKRecurrenceRule)](./removerecurrencerule%28_%29.md)
  Removes a recurrence rule from the recurrence rule array.
- [var recurrenceRules: [EKRecurrenceRule]?](./recurrencerules.md)
  The recurrence rules for the calendar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendaritem/addrecurrencerule(_:))*