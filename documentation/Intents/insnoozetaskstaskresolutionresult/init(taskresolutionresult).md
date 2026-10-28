# init(taskResolutionResult:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates an object whose resolution involves successfully snoozing a task.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```swift
init(taskResolutionResult: INTaskResolutionResult)
```

```objc
- (instancetype) initWithTaskResolutionResult:(INTaskResolutionResult *) taskResolutionResult;
```

## Return Value

A new [`INSnoozeTasksTaskResolutionResult`](../insnoozetaskstaskresolutionresult.md) object.

## Discussion

Use this method to create a result object when you’re able to snooze a task.

## Parameters

- `taskResolutionResult`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result
- [class func unsupported(forReason: INSnoozeTasksTaskUnsupportedReason) -> Self](./unsupported%28forreason%29.md)
  Creates an object whose resolution requires the user to confirm the task to be snoozed before continuing.
- [enum INSnoozeTasksTaskUnsupportedReason](../insnoozetaskstaskunsupportedreason.md)
  Constants that indicates the reason the app can’t support the snooze task request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insnoozetaskstaskresolutionresult/init(taskresolutionresult:))*