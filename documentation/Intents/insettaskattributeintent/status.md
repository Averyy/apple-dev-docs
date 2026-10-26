# status

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The status to apply to the task.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSetTaskAttributeIntent is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
var status: INTaskStatus { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INTaskStatus status;
```

*macOS*

```objc
@property (atomic, assign, readonly) INTaskStatus status;
```

#### Discussion

If the value of this property is [`INTaskStatus.unknown`](../intaskstatus/unknown.md), do not attempt to change the status of the task.

## See Also

### Getting the Task Information
- [var priority: INTaskPriority](./priority.md)
  The priority for the task.
- [var taskTitle: INSpeakableString?](./tasktitle.md)
  The title for the task.
- [var targetTask: INTask?](./targettask.md)
  The task targetted for modification.
- [enum INTaskStatus](../intaskstatus.md)
  Constants indicating the completion state of a task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insettaskattributeintent/status)*