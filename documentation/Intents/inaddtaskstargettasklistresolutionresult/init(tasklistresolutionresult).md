# init(taskListResolutionResult:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates an object whose resolution involves successfully matching the specified task list.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```swift
init(taskListResolutionResult: INTaskListResolutionResult)
```

```objc
- (instancetype) initWithTaskListResolutionResult:(INTaskListResolutionResult *) taskListResolutionResult;
```

## Return Value

A new [`INTaskListResolutionResult`](../intasklistresolutionresult.md) object.

## Discussion

Use this method to create a result object when you’re able to add a task to the specified task list.

## Parameters

- `taskListResolutionResult`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result
- [class func confirmationRequired(with: INTaskList?, forReason: INAddTasksTargetTaskListConfirmationReason) -> Self](./confirmationrequired%28with,forreason%29.md)
  Creates an object whose resolution requires the user to confirm the reason for creating a new task list before proceeding.
- [enum INAddTasksTargetTaskListConfirmationReason](../inaddtaskstargettasklistconfirmationreason.md)
  Constants that indicate the reason for confirming a task list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtaskstargettasklistresolutionresult/init(tasklistresolutionresult:))*