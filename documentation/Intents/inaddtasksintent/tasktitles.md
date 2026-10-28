# taskTitles

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An array of strings containing the titles of the new tasks.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INAddTasksIntent is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
var taskTitles: [INSpeakableString]? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<INSpeakableString *> * taskTitles;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSArray<INSpeakableString *> * taskTitles;
```

## Discussion

Create a new task for each string in the array. Use the string contents as the title of the task.

## See Also

### Getting the Task Details
- [var targetTaskList: INTaskList?](./targettasklist.md)
  The task list to receive the new tasks.
- [var priority: INTaskPriority](./priority.md)
  The priority for the new task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtasksintent/tasktitles)*