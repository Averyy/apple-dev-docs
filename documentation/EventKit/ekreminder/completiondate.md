# completionDate

**Framework**: EventKit  
**Kind**: property

The date on which the reminder was completed.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var completionDate: Date? { get set }
```

## Mentions

- [Creating events and reminders](creating-events-and-reminders.md)

#### Discussion

Setting this property to a date will set [`isCompleted`](ekreminder/iscompleted.md) to [`true`](https://developer.apple.com/documentation/Swift/true); setting this property to `nil` will set `completed` to [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [enum EKReminderPriority](ekreminderpriority.md)
  The priority of the reminder.
- [var priority: Int](ekreminder/priority.md)
  The reminder’s priority.
- [var startDateComponents: DateComponents?](ekreminder/startdatecomponents.md)
  The start date of the task.
- [var dueDateComponents: DateComponents?](ekreminder/duedatecomponents.md)
  The date by which the reminder should be completed.
- [var isCompleted: Bool](ekreminder/iscompleted.md)
  A Boolean value determining whether or not the reminder is marked completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekreminder/completiondate)*