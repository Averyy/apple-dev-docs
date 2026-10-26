# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves the successful matching of the specified value.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func success(with resolvedPaymentAccount: INPaymentAccount) -> Self
```

```objc
+ (instancetype) successWithResolvedPaymentAccount:(INPaymentAccount *) resolvedPaymentAccount;
```

#### Return Value

A new [`INPaymentAccountResolutionResult`](../inpaymentaccountresolutionresult.md) object.

#### Discussion

Use this method to create a result object when you are able to resolve the parameter successfully to a recognizable user account in your app.

## Parameters

- `resolvedPaymentAccount`: The value that resolves the requested value of the intent. The account you specify may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INPaymentAccount?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user confirm the value before proceeding.
- [class func disambiguation(with: [INPaymentAccount]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentaccountresolutionresult/success(with:))*