# targetTask

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The task targetted for modification.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSetTaskAttributeIntent is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
@NSCopying
var targetTask: INTask? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INTask * targetTask;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INTask * targetTask;
```

## See Also

### Getting the Task Information
- [var priority: INTaskPriority](./priority.md)
  The priority for the task.
- [var taskTitle: INSpeakableString?](./tasktitle.md)
  The title for the task.
- [var status: INTaskStatus](./status.md)
  The status to apply to the task.
- [enum INTaskStatus](../intaskstatus.md)
  Constants indicating the completion state of a task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insettaskattributeintent/targettask)*