# newAutomaticReloadPaymentRequest

**Framework**: Apple Pay on the Web  
**Kind**: property  
**Role**: Instance Property

An updated request for an automatic reload payment.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
ApplePayAutomaticReloadPaymentRequest newAutomaticReloadPaymentRequest;
```

## Discussion

Provide this object to update the [`automaticReloadPaymentRequest`](../applepaypaymentrequest/automaticreloadpaymentrequest.md) value in the original [`ApplePayPaymentRequest`](../applepaypaymentrequest.md), if necessary, after the user updated their payment method.

> ❗ **Important**:  You can’t use this property with [`newMultiTokenContexts`](./newmultitokencontexts.md) or [`newRecurringPaymentRequest`](./newrecurringpaymentrequest.md) properties. Simultaneous use of these properties results in an error and cancels the payment request.

## See Also

### Updating automatic reload payments
- [ApplePayAutomaticReloadPaymentRequest](../applepayautomaticreloadpaymentrequest.md)
  A dictionary that represents a request to set up an automatic reload payment, such as a store card top-up or a prepaid account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentmethodupdate/newautomaticreloadpaymentrequest)*