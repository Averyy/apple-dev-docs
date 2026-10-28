# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires confirmation from the user before proceeding.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INTaskListResolutionResult is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class func confirmationRequired(with taskListToConfirm: INTaskList?) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithTaskListToConfirm:(INTaskList *) taskListToConfirm;
```

## Return Value

A new [`INTaskListResolutionResult`](../intasklistresolutionresult.md) object.

## Discussion

Use this method when you locate a single task list but cannot determine with enough certainty that it is the one intended by the user. For example, you might ask for confirmation when the task list title does not match precisely. Provide an [`INTaskList`](../intasklist.md) object with as much information about the task list as you have available.

## Parameters

- `taskListToConfirm`: The object that resolves the request but must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INTaskList) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func disambiguation(with: [INTaskList]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intasklistresolutionresult/confirmationrequired(with:))*