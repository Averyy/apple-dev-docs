# modifiedTaskList

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The task list that you modified.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INAddTasksIntentResponse is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
@NSCopying
var modifiedTaskList: INTaskList? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INTaskList * modifiedTaskList;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INTaskList * modifiedTaskList;
```

#### Discussion

Set this property to the [`INTaskList`](../intasklist.md) object containing the newly created tasks.

## See Also

### Providing the Task Information
- [var addedTasks: [INTask]?](./addedtasks.md)
  The tasks that you added to the task list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtasksintentresponse/modifiedtasklist)*