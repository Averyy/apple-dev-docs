# priority

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The reminder’s priority.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var priority: Int { get set }
```

```objc
@property (nonatomic) NSUInteger priority;
```

## See Also

### Accessing Reminder Properties
- [enum EKReminderPriority](../ekreminderpriority.md)
  The priority of the reminder.
- [var startDateComponents: DateComponents?](./startdatecomponents.md)
  The start date of the task.
- [var dueDateComponents: DateComponents?](./duedatecomponents.md)
  The date by which the reminder should be completed.
- [var isCompleted: Bool](./iscompleted.md)
  A Boolean value determining whether or not the reminder is marked completed.
- [var completionDate: Date?](./completiondate.md)
  The date on which the reminder was completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekreminder/priority)*