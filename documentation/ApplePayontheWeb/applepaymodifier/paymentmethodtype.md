# paymentMethodType

**Framework**: Apple Pay on the Web  
**Kind**: property

The type of card the customer uses to complete the transaction.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
ApplePayPaymentMethodType paymentMethodType;
```

#### Discussion

This property in the [`ApplePayModifier`](applepaymodifier.md) dictionary indicates the type of payment card that the [`ApplePayModifier`](applepaymodifier.md) applies to: `"credit"`, `"debit"`, `"prepaid"`, or `"store"`. To create a modifier that works with all payment types, don’t provide a value for the [`paymentMethodType`](applepaymodifier/paymentmethodtype.md).

The payment request uses the [`ApplePayModifier`](applepaymodifier.md) that matches the payment method that the customer chooses. For example, if the customer chooses to pay with a debit card, the payment request uses the [`ApplePayModifier`](applepaymodifier.md) with a [`paymentMethodType`](applepaymodifier/paymentmethodtype.md) of `"debit"`, or a modifier that doesn’t specify any [`paymentMethodType`](applepaymodifier/paymentmethodtype.md).

## See Also

- [ApplePayPaymentMethodType](applepaypaymentmethodtype.md)
  A string that represents the type of the payment method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaymodifier/paymentmethodtype)*