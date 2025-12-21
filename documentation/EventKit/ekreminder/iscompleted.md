# isCompleted

**Framework**: EventKit  
**Kind**: property

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

#### Discussion

Setting this property to [`true`](https://developer.apple.com/documentation/Swift/true) will set [`completionDate`](ekreminder/completiondate.md) to the current date; setting this property to [`false`](https://developer.apple.com/documentation/Swift/false) will set `completionDate` to `nil`.

##### Special Considerations

If the reminder was completed using a different client, you may encounter the case where this property is [`true`](https://developer.apple.com/documentation/Swift/true), but `completionDate` is `nil`.

## See Also

- [enum EKReminderPriority](ekreminderpriority.md)
  The priority of the reminder.
- [var priority: Int](ekreminder/priority.md)
  The reminder’s priority.
- [var startDateComponents: DateComponents?](ekreminder/startdatecomponents.md)
  The start date of the task.
- [var dueDateComponents: DateComponents?](ekreminder/duedatecomponents.md)
  The date by which the reminder should be completed.
- [var completionDate: Date?](ekreminder/completiondate.md)
  The date on which the reminder was completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekreminder/iscompleted)*