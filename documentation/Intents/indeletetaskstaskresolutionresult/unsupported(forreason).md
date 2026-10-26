# unsupported(forReason:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires the user to confirm the task before continuing.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0
- iPadOS 13.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 8.0

> **Deprecated**: INDeleteTasksTaskResolutionResult is deprecated. There is no replacement.

## Declaration

```swift
class func unsupported(forReason reason: INDeleteTasksTaskUnsupportedReason) -> Self
```

```objc
+ (instancetype) unsupportedForReason:(INDeleteTasksTaskUnsupportedReason) reason;
```

#### Return Value

A new [`INDeleteTasksTaskResolutionResult`](../indeletetaskstaskresolutionresult.md) object.

#### Discussion

Use this method to create a resolution result object when your app doesn’t support the intent parameter for the specified reason.

## See Also

### Creating a Resolution Result
- [init(taskResolutionResult: INTaskResolutionResult)](./init%28taskresolutionresult%29.md)
  Creates an object whose resolution involves successfully deleting a task.
- [enum INDeleteTasksTaskUnsupportedReason](../indeletetaskstaskunsupportedreason.md)
  Constants that indicate the reason the app can’t support the delete task request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indeletetaskstaskresolutionresult/unsupported(forreason:))*