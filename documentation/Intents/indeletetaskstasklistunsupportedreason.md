# INDeleteTasksTaskListUnsupportedReason

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the reason an app can’t support the delete task request.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0
- iPadOS 13.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 8.0

> **Deprecated**: INDeleteTasksTaskListUnsupportedReason is deprecated. There is no replacement.

## Declaration

```swift
enum INDeleteTasksTaskListUnsupportedReason
```

```c
enum INDeleteTasksTaskListUnsupportedReason : NSInteger;
```

## Topics

### Constants
- [INDeleteTasksTaskListUnsupportedReason.noTaskListFound](./indeletetaskstasklistunsupportedreason/notasklistfound.md)
  A resolution result that indicates no task list was found.
### Initializers
- [init?(rawValue: Int)](./indeletetaskstasklistunsupportedreason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating a Resolution Result
- [init(taskListResolutionResult: INTaskListResolutionResult)](./indeletetaskstasklistresolutionresult/init%28tasklistresolutionresult%29.md)
  Creates an object whose resolution involves successfully deleting a task from a task list.
- [class func unsupported(forReason: INDeleteTasksTaskListUnsupportedReason) -> Self](./indeletetaskstasklistresolutionresult/unsupported%28forreason%29.md)
  Creates an object whose resolution requires the user to confirm the task list before continuing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indeletetaskstasklistunsupportedreason)*