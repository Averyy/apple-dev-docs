# addedTasks

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The tasks that you added to the task list.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INAddTasksIntentResponse is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
var addedTasks: [INTask]? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSArray<INTask *> * addedTasks;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSArray<INTask *> * addedTasks;
```

#### Discussion

Set this property to an array of [`INTask`](../intask.md) objects, each of which represents a single task that you added.

## See Also

### Providing the Task Information
- [var modifiedTaskList: INTaskList?](./modifiedtasklist.md)
  The task list that you modified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtasksintentresponse/addedtasks)*