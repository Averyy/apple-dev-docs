# multiTokenContexts

**Framework**: Apple Pay on the Web  
**Kind**: property  
**Role**: Instance Property

An array of payment token contexts that requests multiple payment tokens to support a multimerchant payment.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
sequence <ApplePayPaymentTokenContext> multiTokenContexts;
```

## Mentions

- [Apple Pay on the Web Version 14 Release Notes](../apple-pay-on-the-web-version-14-release-notes.md)

## Discussion

Use multitoken contexts to indicate payments for multiple merchants. The sum of the [`amount`](../applepaypaymenttokencontext/amount.md) of all the payment token contexts must be less than or equal to the grand total amount of the enclosing payment request. Otherwise, the request results in an error and cancels the payment request.

> ❗ **Important**:  You can’t use this array with [`recurringPaymentRequest`](./recurringpaymentrequest.md) or [`automaticReloadPaymentRequest`](./automaticreloadpaymentrequest.md) properties. Simultaneous use of these properties results in an error and cancels the payment request.

## See Also

### Requesting multitoken or multimerchant payments
- [ApplePayPaymentTokenContext](../applepaypaymenttokencontext.md)
  A dictionary that defines the context for a single payment token in a payment request for multimerchant payments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentrequest/multitokencontexts)*