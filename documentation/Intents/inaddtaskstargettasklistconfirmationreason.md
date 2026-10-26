# INAddTasksTargetTaskListConfirmationReason

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the reason for confirming a task list.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```swift
enum INAddTasksTargetTaskListConfirmationReason
```

```c
enum INAddTasksTargetTaskListConfirmationReason : NSInteger;
```

## Topics

### Constants
- [INAddTasksTargetTaskListConfirmationReason.listShouldBeCreated](./inaddtaskstargettasklistconfirmationreason/listshouldbecreated.md)
  A confirmation reason that indicates the app should create the task list.
### Initializers
- [init?(rawValue: Int)](./inaddtaskstargettasklistconfirmationreason/init%28rawvalue%29.md)

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
- [init(taskListResolutionResult: INTaskListResolutionResult)](./inaddtaskstargettasklistresolutionresult/init%28tasklistresolutionresult%29.md)
  Creates an object whose resolution involves successfully matching the specified task list.
- [class func confirmationRequired(with: INTaskList?, forReason: INAddTasksTargetTaskListConfirmationReason) -> Self](./inaddtaskstargettasklistresolutionresult/confirmationrequired%28with,forreason%29.md)
  Creates an object whose resolution requires the user to confirm the reason for creating a new task list before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtaskstargettasklistconfirmationreason)*