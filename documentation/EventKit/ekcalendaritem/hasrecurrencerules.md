# hasRecurrenceRules

**Framework**: EventKit  
**Kind**: property

A Boolean value that indicates whether the calendar item has recurrence rules.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var hasRecurrenceRules: Bool { get }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), the calendar item has recurrence rules; otherwise it does not.

##### Special Considerations

The implementation only supports a single recurrence rule. Adding a recurrence rule replaces the single recurrence rule.

## See Also

- [func addRecurrenceRule(EKRecurrenceRule)](ekcalendaritem/addrecurrencerule(_:).md)
  Adds a recurrence rule to the recurrence rule array.
- [func removeRecurrenceRule(EKRecurrenceRule)](ekcalendaritem/removerecurrencerule(_:).md)
  Removes a recurrence rule from the recurrence rule array.
- [var recurrenceRules: [EKRecurrenceRule]?](ekcalendaritem/recurrencerules.md)
  The recurrence rules for the calendar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendaritem/hasrecurrencerules)*