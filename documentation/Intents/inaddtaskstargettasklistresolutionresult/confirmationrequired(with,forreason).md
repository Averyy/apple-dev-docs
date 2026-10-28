# confirmationRequired(with:forReason:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires the user to confirm the reason for creating a new task list before proceeding.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```swift
class func confirmationRequired(with taskListToConfirm: INTaskList?, forReason reason: INAddTasksTargetTaskListConfirmationReason) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithTaskListToConfirm:(INTaskList *) taskListToConfirm forReason:(INAddTasksTargetTaskListConfirmationReason) reason;
```

## Return Value

A new [`INAddTasksTargetTaskListResolutionResult`](../inaddtaskstargettasklistresolutionresult.md) object.

## Discussion

Use this method when you can’t resolve the parameter to a similar but not equal temporal event type than the one specified in the intent. Don’t use this method to resolve task list types your app doesn’t support.

## Parameters

- `taskListToConfirm`: The task list to confirm.
- `reason`: The reason for confirming the task list.

## See Also

### Creating a Resolution Result
- [init(taskListResolutionResult: INTaskListResolutionResult)](./init%28tasklistresolutionresult%29.md)
  Creates an object whose resolution involves successfully matching the specified task list.
- [enum INAddTasksTargetTaskListConfirmationReason](../inaddtaskstargettasklistconfirmationreason.md)
  Constants that indicate the reason for confirming a task list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtaskstargettasklistresolutionresult/confirmationrequired(with:forreason:))*