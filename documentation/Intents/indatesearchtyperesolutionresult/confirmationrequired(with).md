# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires that the user must confirm the value before proceeding.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INDateSearchTypeResolutionResult is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class func confirmationRequired(with dateSearchTypeToConfirm: INDateSearchType) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithDateSearchTypeToConfirm:(INDateSearchType) dateSearchTypeToConfirm;
```

## Return Value

A new [`INDateSearchTypeResolutionResult`](../indatesearchtyperesolutionresult.md) object.

## Discussion

Use this method when you can’t resolve the parameter to a date type that’s similar to, but not equal to, the one specified in the intent. Don’t use this method to resolve date types that your app doesn’t support.

## Parameters

- `dateSearchTypeToConfirm`: The value that resolves the request but must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INDateSearchType) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indatesearchtyperesolutionresult/confirmationrequired(with:))*