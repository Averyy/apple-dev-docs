# isCompleted

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value determining whether or not the reminder is marked completed.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isCompleted: Bool { get set }
```

```objc
@property (nonatomic, getter=isCompleted) BOOL completed;
```

#### Discussion

Setting this property to [`true`](../../Swift/true.md) will set [`completionDate`](./completiondate.md) to the current date; setting this property to [`false`](../../Swift/false.md) will set `completionDate` to `nil`.

##### Special Considerations

If the reminder was completed using a different client, you may encounter the case where this property is [`true`](../../Swift/true.md), but `completionDate` is `nil`.

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
- [var completionDate: Date?](./completiondate.md)
  The date on which the reminder was completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekreminder/iscompleted)*