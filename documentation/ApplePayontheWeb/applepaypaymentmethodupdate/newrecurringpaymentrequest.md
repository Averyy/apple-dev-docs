# newRecurringPaymentRequest

**Framework**: Apple Pay on the Web  
**Kind**: property

An updated request for a recurring payment.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
ApplePayRecurringPaymentRequest newRecurringPaymentRequest;
```

#### Discussion

Provide this object to update the [`recurringPaymentRequest`](applepaypaymentrequest/recurringpaymentrequest.md) value in the original [`ApplePayPaymentRequest`](applepaypaymentrequest.md), if necessary, after the user updated their payment method.

> ❗ **Important**:  You can’t use this property with [`newMultiTokenContexts`](applepaypaymentmethodupdate/newmultitokencontexts.md) or [`newAutomaticReloadPaymentRequest`](applepaypaymentmethodupdate/newautomaticreloadpaymentrequest.md) properties. Simultaneous use of these properties results in an error and cancels the payment request.

## See Also

- [ApplePayRecurringPaymentRequest](applepayrecurringpaymentrequest.md)
  A dictionary that represents a request to set up a recurring payment, typically a subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentmethodupdate/newrecurringpaymentrequest)*