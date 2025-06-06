# EKReminderPriority

**Framework**: EventKit  
**Kind**: enum

The priority of the reminder.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum EKReminderPriority
```

## Topics

### Constants
- [EKReminderPriority.none](ekreminderpriority/none.md)
  The reminder has no priority set.
- [EKReminderPriority.high](ekreminderpriority/high.md)
  The reminder is high priority.
- [EKReminderPriority.medium](ekreminderpriority/medium.md)
  The reminder is medium priority.
- [EKReminderPriority.low](ekreminderpriority/low.md)
  The reminder is low priority.
### Initializers
- [init?(rawValue: UInt)](ekreminderpriority/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var priority: Int](ekreminder/priority.md)
  The reminder’s priority.
- [var startDateComponents: DateComponents?](ekreminder/startdatecomponents.md)
  The start date of the task.
- [var dueDateComponents: DateComponents?](ekreminder/duedatecomponents.md)
  The date by which the reminder should be completed.
- [var isCompleted: Bool](ekreminder/iscompleted.md)
  A Boolean value determining whether or not the reminder is marked completed.
- [var completionDate: Date?](ekreminder/completiondate.md)
  The date on which the reminder was completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekreminderpriority)*