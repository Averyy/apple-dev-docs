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
class func success(with resolvedPaymentAmount: INPaymentAmount) -> Self
```

```objc
+ (instancetype) successWithResolvedPaymentAmount:(INPaymentAmount *) resolvedPaymentAmount;
```

#### Return Value

A new [`INPaymentAmountResolutionResult`](../inpaymentamountresolutionresult.md) object.

#### Discussion

Use this method to create a result object when you are able to resolve the payment amount for a bill. For payment amounts representing the account’s current balance, amount due, or minimum amount due, a successful resolution signifies that you know the amount of money to transfer from the user’s account to the bill payee.

## Parameters

- `resolvedPaymentAmount`: The value that resolves the requested value of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INPaymentAmount?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user confirm the value before proceeding.
- [class func disambiguation(with: [INPaymentAmount]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentamountresolutionresult/success(with:))*