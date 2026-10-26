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
class func disambiguation(with paymentAccountsToDisambiguate: [INPaymentAccount]) -> Self
```

```objc
+ (instancetype) disambiguationWithPaymentAccountsToDisambiguate:(NSArray<INPaymentAccount *> *) paymentAccountsToDisambiguate;
```

#### Return Value

A new [`INPaymentAccountResolutionResult`](../inpaymentaccountresolutionresult.md) object.

#### Discussion

Use this method when you cannot resolve the user account uniquely and need the user to select from a limited set of possible options.

## Parameters

- `paymentAccountsToDisambiguate`: An array of [`INPaymentAccount`](../inpaymentaccount.md) objects from which to select. Specify as few objects as possible, and preferably no more than five.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INPaymentAccount) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified value.
- [class func confirmationRequired(with: INPaymentAccount?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentaccountresolutionresult/disambiguation(with:))*