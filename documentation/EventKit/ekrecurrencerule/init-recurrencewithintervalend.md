# init(recurrenceWith:interval:end:)

**Framework**: EventKit  
**Kind**: init

Initializes and returns a simple recurrence rule with a given frequency, interval, and end.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(recurrenceWith type: EKRecurrenceFrequency, interval: Int, end: EKRecurrenceEnd?)
```

## Mentions

- [Creating a recurring event](creating-a-recurring-event.md)

#### Return Value

The initialized recurrence rule, or `nil` if invalid values are provided.

## Parameters

- `type`: The frequency of the recurrence rule. Can be daily, weekly, monthly, or yearly.
- `interval`: The interval between instances of this recurrence. For example, a weekly recurrence rule with an interval of   occurs every other week. Must be greater than  .
- `end`: The end of the recurrence rule.

## See Also

- [Calendar and Reminders Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/EventKitProgGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009765)
- [enum EKSpan](ekspan.md)
  An object that indicates whether modifications should apply to a single event or all future events of a recurring event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekrecurrencerule/init(recurrencewith:interval:end:))*