# priority

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The priority for the new task.

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

### Getting the Task Details
- [var targetTaskList: INTaskList?](./targettasklist.md)
  The task list to receive the new tasks.
- [var taskTitles: [INSpeakableString]?](./tasktitles.md)
  An array of strings containing the titles of the new tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtasksintent/priority)*