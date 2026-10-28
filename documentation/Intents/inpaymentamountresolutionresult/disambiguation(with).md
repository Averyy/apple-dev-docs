# disambiguation(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires the user to select from among the specified objects.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func disambiguation(with paymentAmountsToDisambiguate: [INPaymentAmount]) -> Self
```

```objc
+ (instancetype) disambiguationWithPaymentAmountsToDisambiguate:(NSArray<INPaymentAmount *> *) paymentAmountsToDisambiguate;
```

## Return Value

A new [`INPaymentAmountResolutionResult`](../inpaymentamountresolutionresult.md) object.

## Discussion

Use this method when you cannot resolve the user request uniquely and want the user to select from a limited set of possible options. For example, you might use this method if the user’s initial request did not specify a payment amount and you want to specify options to pay the minimum amount due or the total amount.

> **Note**:  In watchOS, it is preferable to choose an appropriate amount and ask for confirmation rather than to ask the user to disambiguate from among several values.

## Parameters

- `paymentAmountsToDisambiguate`: An array of [`INPaymentAmount`](../inpaymentamount.md) objects from which to select. Specify as few objects as possible, and preferably no more than five.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INPaymentAmount) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified value.
- [class func confirmationRequired(with: INPaymentAmount?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentamountresolutionresult/disambiguation(with:))*