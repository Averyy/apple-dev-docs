# hasRecurrenceRules

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) BOOL hasRecurrenceRules;
```

#### Discussion

If [`true`](../../Swift/true.md), the calendar item has recurrence rules; otherwise it does not.

##### Special Considerations

The implementation only supports a single recurrence rule. Adding a recurrence rule replaces the single recurrence rule.

## See Also

### Setting Recurrence Rules
- [func addRecurrenceRule(EKRecurrenceRule)](./addrecurrencerule%28_%29.md)
  Adds a recurrence rule to the recurrence rule array.
- [func removeRecurrenceRule(EKRecurrenceRule)](./removerecurrencerule%28_%29.md)
  Removes a recurrence rule from the recurrence rule array.
- [var recurrenceRules: [EKRecurrenceRule]?](./recurrencerules.md)
  The recurrence rules for the calendar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekcalendaritem/hasrecurrencerules)*