# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves successfully matching the specified parameter.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

> **Deprecated**: INTaskPriorityResolutionResult is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class func success(with resolvedTaskPriority: INTaskPriority) -> Self
```

```objc
+ (instancetype) successWithResolvedTaskPriority:(INTaskPriority) resolvedTaskPriority;
```

#### Return Value

A new [`INTaskPriorityResolutionResult`](../intaskpriorityresolutionresult.md) object.

#### Discussion

Use this method to create a result object when you successfully identify the task priority to modify.

## Parameters

- `resolvedTaskPriority`: The object that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INTaskPriority) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires user confirmation before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intaskpriorityresolutionresult/success(with:))*