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
class func success(with resolvedBalanceType: INBalanceType) -> Self
```

```objc
+ (instancetype) successWithResolvedBalanceType:(INBalanceType) resolvedBalanceType;
```

#### Return Value

A new [`INBalanceTypeResolutionResult`](../inbalancetyperesolutionresult.md) object.

#### Discussion

Use this method to create a result object when you are able to resolve the balance type to a recognizable value in your app.

## Parameters

- `resolvedBalanceType`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INBalanceType) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbalancetyperesolutionresult/success(with:))*