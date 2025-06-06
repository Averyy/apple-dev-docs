# recurrenceRules

**Framework**: EventKit  
**Kind**: property

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

#### Discussion

The implementation only supports a single recurrence rule.

## See Also

- [var hasRecurrenceRules: Bool](ekcalendaritem/hasrecurrencerules.md)
  A Boolean value that indicates whether the calendar item has recurrence rules.
- [func addRecurrenceRule(EKRecurrenceRule)](ekcalendaritem/addrecurrencerule(_:).md)
  Adds a recurrence rule to the recurrence rule array.
- [func removeRecurrenceRule(EKRecurrenceRule)](ekcalendaritem/removerecurrencerule(_:).md)
  Removes a recurrence rule from the recurrence rule array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendaritem/recurrencerules)*