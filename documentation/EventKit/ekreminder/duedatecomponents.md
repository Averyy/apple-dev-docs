# dueDateComponents

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The date by which the reminder should be completed.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var dueDateComponents: DateComponents? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSDateComponents * dueDateComponents;
```

## Mentions

- [Creating events and reminders](../creating-events-and-reminders.md)

#### Discussion

The use of date components allows the due date and its time zone to be represented in a single property. A `nil` time zone represents a floating date. Setting a date component without an hour, minute and second component will set the reminder to be an all-day reminder. If this property is set, the calendar must be set to `NSGregorianCalendar`; otherwise an exception is raised.

This components’s `timeZone` property is independent of time zone properties on [`startDateComponents`](./startdatecomponents.md) and its super [`EKCalendarItem`](../ekcalendaritem.md) object. By default, the due date is set to the system time zone.

##### Special Considerations

On iOS, Event Kit requires that a start date is set if the due date is set, however this is not a requirement in macOS.

## See Also

### Accessing Reminder Properties
- [enum EKReminderPriority](../ekreminderpriority.md)
  The priority of the reminder.
- [var priority: Int](./priority.md)
  The reminder’s priority.
- [var startDateComponents: DateComponents?](./startdatecomponents.md)
  The start date of the task.
- [var isCompleted: Bool](./iscompleted.md)
  A Boolean value determining whether or not the reminder is marked completed.
- [var completionDate: Date?](./completiondate.md)
  The date on which the reminder was completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekreminder/duedatecomponents)*