# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves the successful matching of the specified parameter.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INTaskStatusResolutionResult is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class func success(with resolvedTaskStatus: INTaskStatus) -> Self
```

```objc
+ (instancetype) successWithResolvedTaskStatus:(INTaskStatus) resolvedTaskStatus;
```

#### Return Value

A new [`INTaskStatusResolutionResult`](../intaskstatusresolutionresult.md) object.

#### Discussion

Use this method to create a result object when you support searching for tasks with the specified status or applying the status to a task.

## Parameters

- `resolvedTaskStatus`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INTaskStatus) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires confirmation from the user before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intaskstatusresolutionresult/success(with:))*