# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires user confirmation before proceeding.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

> **Deprecated**: INTaskPriorityResolutionResult is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class func confirmationRequired(with taskPriorityToConfirm: INTaskPriority) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithTaskPriorityToConfirm:(INTaskPriority) taskPriorityToConfirm;
```

## Return Value

A new [`INTaskPriorityResolutionResult`](../intaskpriorityresolutionresult.md) object.

## Discussion

Use this method when you have to make assumptions about the time information specified by the user.

## Parameters

- `taskPriorityToConfirm`: The object that resolves the request but must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INTaskPriority) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves successfully matching the specified parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intaskpriorityresolutionresult/confirmationrequired(with:))*