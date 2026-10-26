# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves the successful matching of the specified attribute.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func success(with resolvedAccountType: INAccountType) -> Self
```

```objc
+ (instancetype) successWithResolvedAccountType:(INAccountType) resolvedAccountType;
```

#### Return Value

A new [`INAccountTypeResolutionResult`](../inaccounttyperesolutionresult.md) object.

#### Discussion

Use this method to create a result object when you are able to resolve the account successfully to a recognizable value in your app.

## Parameters

- `resolvedAccountType`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INAccountType) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaccounttyperesolutionresult/success(with:))*