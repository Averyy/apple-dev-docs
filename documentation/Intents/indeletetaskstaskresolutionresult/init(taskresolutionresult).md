# init(taskResolutionResult:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates an object whose resolution involves successfully deleting a task.

**Availability**:
- iOS 13.0+ - Deprecated in 15.0
- iPadOS 13.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 6.0+ - Deprecated in 8.0

> **Deprecated**: INDeleteTasksTaskResolutionResult is deprecated. There is no replacement.

## Declaration

```swift
init(taskResolutionResult: INTaskResolutionResult)
```

```objc
- (instancetype) initWithTaskResolutionResult:(INTaskResolutionResult *) taskResolutionResult;
```

#### Return Value

A new [`INDeleteTasksTaskResolutionResult`](../indeletetaskstaskresolutionresult.md) object.

#### Discussion

Use this method to create a result object when you’re able to delete a task.

## Parameters

- `taskResolutionResult`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result
- [class func unsupported(forReason: INDeleteTasksTaskUnsupportedReason) -> Self](./unsupported%28forreason%29.md)
  Creates an object whose resolution requires the user to confirm the task before continuing.
- [enum INDeleteTasksTaskUnsupportedReason](../indeletetaskstaskunsupportedreason.md)
  Constants that indicate the reason the app can’t support the delete task request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indeletetaskstaskresolutionresult/init(taskresolutionresult:))*