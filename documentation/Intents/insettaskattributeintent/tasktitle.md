# taskTitle

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The title for the task.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```swift
@NSCopying
var taskTitle: INSpeakableString? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INSpeakableString * taskTitle;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INSpeakableString * taskTitle;
```

## See Also

### Getting the Task Information
- [var priority: INTaskPriority](./priority.md)
  The priority for the task.
- [var targetTask: INTask?](./targettask.md)
  The task targetted for modification.
- [var status: INTaskStatus](./status.md)
  The status to apply to the task.
- [enum INTaskStatus](../intaskstatus.md)
  Constants indicating the completion state of a task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insettaskattributeintent/tasktitle)*