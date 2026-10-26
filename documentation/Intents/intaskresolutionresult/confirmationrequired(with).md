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

> **Deprecated**: INTaskResolutionResult is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class func confirmationRequired(with taskToConfirm: INTask?) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithTaskToConfirm:(INTask *) taskToConfirm;
```

#### Return Value

A new [`INTaskResolutionResult`](../intaskresolutionresult.md) object.

#### Discussion

Use this method when you locate a single task but cannot determine with enough certainty that it is the one intended by the user. For example, you might ask for confirmation when the task’s title text does not match precisely. Provide an [`INTask`](../intask.md) object with as much information about the task as you have available.

## Parameters

- `taskToConfirm`: The object that resolves the request but must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INTask) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func disambiguation(with: [INTask]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intaskresolutionresult/confirmationrequired(with:))*