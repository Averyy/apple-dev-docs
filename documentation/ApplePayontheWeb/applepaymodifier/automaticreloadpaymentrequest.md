# automaticReloadPaymentRequest

**Framework**: Apple Pay on the Web  
**Kind**: property

A property that requests an automatic reload payment, such as a store card top-up.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
ApplePayAutomaticReloadPaymentRequest automaticReloadPaymentRequest;
```

## Mentions

- [Apple Pay on the Web Version 14 Release Notes](apple-pay-on-the-web-version-14-release-notes.md)

#### Discussion

Set this property to indicate that the payment request is for an automatic reload payment.

Apple Pay issues an Apple Pay Merchant Token if the user’s payment network supports merchant-specific payment tokens. Otherwise, Apple Pay issues a device token for the payment request.

> ❗ **Important**:  You can’t use this property with [`multiTokenContexts`](applepaymodifier/multitokencontexts.md) or [`recurringPaymentRequest`](applepaymodifier/recurringpaymentrequest.md) properties. Simultaneous use of these properties results in an error and cancels the payment request.

 You can’t use this property with [`multiTokenContexts`](applepaymodifier/multitokencontexts.md) or [`recurringPaymentRequest`](applepaymodifier/recurringpaymentrequest.md) properties. Simultaneous use of these properties results in an error and cancels the payment request.

## See Also

- [ApplePayAutomaticReloadPaymentRequest](applepayautomaticreloadpaymentrequest.md)
  A dictionary that represents a request to set up an automatic reload payment, such as a store card top-up or a prepaid account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaymodifier/automaticreloadpaymentrequest)*