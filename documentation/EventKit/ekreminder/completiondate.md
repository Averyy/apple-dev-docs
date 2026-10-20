# completionDate

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, nullable) NSDate * completionDate;
```

## Mentions

- [Creating events and reminders](../creating-events-and-reminders.md)

#### Discussion

Setting this property to a date will set [`isCompleted`](./iscompleted.md) to [`true`](../../Swift/true.md); setting this property to `nil` will set `completed` to [`false`](../../Swift/false.md).

## See Also

### Accessing Reminder Properties
- [enum EKReminderPriority](../ekreminderpriority.md)
  The priority of the reminder.
- [var priority: Int](./priority.md)
  The reminder’s priority.
- [var startDateComponents: DateComponents?](./startdatecomponents.md)
  The start date of the task.
- [var dueDateComponents: DateComponents?](./duedatecomponents.md)
  The date by which the reminder should be completed.
- [var isCompleted: Bool](./iscompleted.md)
  A Boolean value determining whether or not the reminder is marked completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekreminder/completiondate)*