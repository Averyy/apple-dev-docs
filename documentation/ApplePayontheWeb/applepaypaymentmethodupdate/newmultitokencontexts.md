# newMultiTokenContexts

**Framework**: Apple Pay on the Web  
**Kind**: property  
**Role**: Instance Property

An array of updated multitoken contexts for a multimerchant payment request.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
sequence <ApplePayPaymentTokenContext> newMultiTokenContexts;
```

#### Discussion

Provide this object to update the [`multiTokenContexts`](../applepaypaymentrequest/multitokencontexts.md) value in the original [`ApplePayPaymentRequest`](../applepaypaymentrequest.md), if necessary, after the user updated their payment method.

> ❗ **Important**:  You can’t use this property with [`newAutomaticReloadPaymentRequest`](../applepayshippingmethodupdate/newautomaticreloadpaymentrequest.md) or [`newRecurringPaymentRequest`](./newrecurringpaymentrequest.md) properties. Simultaneous use of these properties results in an error and cancels the payment request.

## See Also

### Updating multitoken or multimerchant payments
- [ApplePayPaymentTokenContext](../applepaypaymenttokencontext.md)
  A dictionary that defines the context for a single payment token in a payment request for multimerchant payments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentmethodupdate/newmultitokencontexts)*