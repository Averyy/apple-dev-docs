# unsupported(forReason:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires the user to confirm the task list before continuing.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0
- iPadOS 13.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 8.0

> **Deprecated**: INDeleteTasksTaskListResolutionResult is deprecated. There is no replacement.

## Declaration

```swift
class func unsupported(forReason reason: INDeleteTasksTaskListUnsupportedReason) -> Self
```

```objc
+ (instancetype) unsupportedForReason:(INDeleteTasksTaskListUnsupportedReason) reason;
```

## Return Value

A new [`INDeleteTasksTaskListResolutionResult`](../indeletetaskstasklistresolutionresult.md) object.

## Discussion

Use this method to create a resolution result object when your app doesn’t support the intent parameter for the specified reason.

## Parameters

- `reason`: The reason that deletion isn’t supported.

## See Also

### Creating a Resolution Result
- [init(taskListResolutionResult: INTaskListResolutionResult)](./init%28tasklistresolutionresult%29.md)
  Creates an object whose resolution involves successfully deleting a task from a task list.
- [enum INDeleteTasksTaskListUnsupportedReason](../indeletetaskstasklistunsupportedreason.md)
  Constants that indicate the reason an app can’t support the delete task request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indeletetaskstasklistresolutionresult/unsupported(forreason:))*