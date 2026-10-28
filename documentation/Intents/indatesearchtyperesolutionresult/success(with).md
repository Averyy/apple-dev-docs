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

> **Deprecated**: INDateSearchTypeResolutionResult is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
class func success(with resolvedDateSearchType: INDateSearchType) -> Self
```

```objc
+ (instancetype) successWithResolvedDateSearchType:(INDateSearchType) resolvedDateSearchType;
```

## Return Value

A new [`INDateSearchTypeResolutionResult`](../indatesearchtyperesolutionresult.md) object.

## Discussion

Use this method to create a result object when you’re able to search for notes based on the specified date type.

## Parameters

- `resolvedDateSearchType`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INDateSearchType) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/indatesearchtyperesolutionresult/success(with:))*