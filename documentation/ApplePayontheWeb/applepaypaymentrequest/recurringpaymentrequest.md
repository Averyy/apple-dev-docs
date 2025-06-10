# recurringPaymentRequest

**Framework**: Apple Pay on the Web  
**Kind**: property

A property that requests a recurring payment, typically a subscription.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
ApplePayRecurringPaymentRequest recurringPaymentRequest;
```

## Mentions

- [Apple Pay on the Web Version 14 Release Notes](apple-pay-on-the-web-version-14-release-notes.md)

#### Discussion

This property is optional. Use it to indicate that the payment request is for a recurring payment.

Apple Pay issues an Apple Pay Merchant Token if the user’s payment network supports merchant-specific payment tokens. Otherwise, Apple Pay issues a device token for the payment request.

> ❗ **Important**:  You can’t use this property with [`multiTokenContexts`](applepaypaymentrequest/multitokencontexts.md) or [`automaticReloadPaymentRequest`](applepaypaymentrequest/automaticreloadpaymentrequest.md) properties. Simultaneous use of these properties results in an error and cancels the payment request.

## See Also

- [ApplePayRecurringPaymentRequest](applepayrecurringpaymentrequest.md)
  A dictionary that represents a request to set up a recurring payment, typically a subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentrequest/recurringpaymentrequest)*