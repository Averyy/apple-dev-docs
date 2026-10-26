# targetTaskList

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The task list to receive the new tasks.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INAddTasksIntent is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
@NSCopying
var targetTaskList: INTaskList? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INTaskList * targetTaskList;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INTaskList * targetTaskList;
```

## See Also

### Getting the Task Details
- [var taskTitles: [INSpeakableString]?](./tasktitles.md)
  An array of strings containing the titles of the new tasks.
- [var priority: INTaskPriority](./priority.md)
  The priority for the new task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtasksintent/targettasklist)*