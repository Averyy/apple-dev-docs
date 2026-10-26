# priority

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The priority for the task.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```swift
var priority: INTaskPriority { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, assign, readonly) INTaskPriority priority;
```

*macOS*

```objc
@property (atomic, assign, readonly) INTaskPriority priority;
```

## See Also

### Getting the Task Information
- [var taskTitle: INSpeakableString?](./tasktitle.md)
  The title for the task.
- [var targetTask: INTask?](./targettask.md)
  The task targetted for modification.
- [var status: INTaskStatus](./status.md)
  The status to apply to the task.
- [enum INTaskStatus](../intaskstatus.md)
  Constants indicating the completion state of a task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insettaskattributeintent/priority)*