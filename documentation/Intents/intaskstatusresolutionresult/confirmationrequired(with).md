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

> **Deprecated**: INTaskStatusResolutionResult is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class func confirmationRequired(with taskStatusToConfirm: INTaskStatus) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithTaskStatusToConfirm:(INTaskStatus) taskStatusToConfirm;
```

## Return Value

A new [`INTaskStatusResolutionResult`](../intaskstatusresolutionresult.md) object.

## Discussion

Use this method when you cannot handle the intent using the specified task status but can handle it using a different status and want to confirm with the user before proceeding.

## Parameters

- `taskStatusToConfirm`: The value that resolves the request but must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INTaskStatus) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intaskstatusresolutionresult/confirmationrequired(with:))*