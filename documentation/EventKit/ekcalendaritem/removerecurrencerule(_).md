# removeRecurrenceRule(_:)

**Framework**: EventKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) removeRecurrenceRule:(EKRecurrenceRule *) rule;
```

## Discussion

The implementation only supports a single recurrence rule.

## Parameters

- `rule`: The rule to be removed from [`recurrenceRules`](./recurrencerules.md).

## See Also

### Setting Recurrence Rules
- [var hasRecurrenceRules: Bool](./hasrecurrencerules.md)
  A Boolean value that indicates whether the calendar item has recurrence rules.
- [func addRecurrenceRule(EKRecurrenceRule)](./addrecurrencerule%28_%29.md)
  Adds a recurrence rule to the recurrence rule array.
- [var recurrenceRules: [EKRecurrenceRule]?](./recurrencerules.md)
  The recurrence rules for the calendar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendaritem/removerecurrencerule(_:))*