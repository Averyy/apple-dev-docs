# completePayment

**Framework**: Apple Pay on the Web  
**Kind**: method  
**Role**: Instance Method

Completes the payment authorization with a result.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
undefined completePayment();
```

## Mentions

- [Apple Pay on the Web Version 3 Release Notes](../apple-pay-on-the-web-version-3-release-notes.md)

#### Discussion

This method must be called by [`onpaymentauthorized`](./onpaymentauthorized.md).

Use status values of [`STATUS_SUCCESS`](./status_success.md) or [`STATUS_FAILURE`](./status_failure.md) only.  You should pass in [`STATUS_FAILURE`](./status_failure.md) along with the errors.

##### completePayment in Apple Pay JS API version 1 and 2

The parameter for [`completePayment`](./completepayment.md) in versions 1 and 2 is the following:

`status`

The status of the payment, whether it succeeded or failed. See [Apple Pay Status Codes](../apple-pay-status-codes.md).

The Apple Pay payment sheet is dismissed when this method is called with a status value of [`STATUS_SUCCESS`](./status_success.md) or [`STATUS_FAILURE`](./status_failure.md). Other status values display an error on the payment sheet to prompt the user to update the information and authenticate again.

## Parameters

- `result`: The result of the payment authorization, including its status and list of errors. See [`ApplePayPaymentAuthorizationResult`](../applepaypaymentauthorizationresult.md).

## See Also

### Related Documentation
- [supportsVersion](./supportsversion.md)
  Detects whether a web browser supports a particular Apple Pay version.
### Handling payment authorization
- [onpaymentauthorized](./onpaymentauthorized.md)
  An event handler the system calls when the user has authorized the Apple Pay payment with Touch ID, Face ID, or a passcode.
- [ApplePayPaymentAuthorizedEvent](../applepaypaymentauthorizedevent.md)
  An event object that contains the token used to authorize a payment.
- [ApplePayPayment](../applepaypayment.md)
  The result of authorizing a payment request that contains payment information.
- [ApplePayPaymentAuthorizationResult](../applepaypaymentauthorizationresult.md)
  The result of payment authorization, including status and errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaysession/completepayment)*