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

> **Deprecated**: INLocationSearchTypeResolutionResult is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class func confirmationRequired(with locationSearchTypeToConfirm: INLocationSearchType) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithLocationSearchTypeToConfirm:(INLocationSearchType) locationSearchTypeToConfirm;
```

#### Return Value

A new [`INLocationSearchTypeResolutionResult`](../inlocationsearchtyperesolutionresult.md) object.

#### Discussion

Use this method when you cannot resolve the parameter to the specified type and want the user to confirm the use of a different type. Do not use this method to resolve location types if you do not support searching by location.

## Parameters

- `locationSearchTypeToConfirm`: The value that resolves the request but must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INLocationSearchType) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlocationsearchtyperesolutionresult/confirmationrequired(with:))*