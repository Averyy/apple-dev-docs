# completePayment

**Framework**: Apple Pay on the Web  
**Kind**: method

Completes the payment authorization with a result.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
undefined completePayment();
```

## Mentions

- [Apple Pay on the Web Version 3 Release Notes](apple-pay-on-the-web-version-3-release-notes.md)

#### Discussion

This method must be called by [`onpaymentauthorized`](applepaysession/onpaymentauthorized.md).

Use status values of [`STATUS_SUCCESS`](applepaysession/status_success.md) or [`STATUS_FAILURE`](applepaysession/status_failure.md) only.  You should pass in [`STATUS_FAILURE`](applepaysession/status_failure.md) along with the errors.

##### Completepayment in Apple Pay Js Api Version 1 and 2

The parameter for [`completePayment`](applepaysession/completepayment.md) in versions 1 and 2 is the following:

`status`

The status of the payment, whether it succeeded or failed. See [`Apple Pay Status Codes`](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/apple_pay_status_codes).

The Apple Pay payment sheet is dismissed when this method is called with a status value of [`STATUS_SUCCESS`](applepaysession/status_success.md) or [`STATUS_FAILURE`](applepaysession/status_failure.md). Other status values display an error on the payment sheet to prompt the user to update the information and authenticate again.

## Parameters

- `result`: The result of the payment authorization, including its status and list of errors. See  .

## See Also

- [supportsVersion](applepaysession/supportsversion.md)
  Detects whether a web browser supports a particular Apple Pay version.
- [onpaymentauthorized](applepaysession/onpaymentauthorized.md)
  An event handler the system calls when the user has authorized the Apple Pay payment with Touch ID, Face ID, or a passcode.
- [ApplePayPaymentAuthorizedEvent](applepaypaymentauthorizedevent.md)
  An event object that contains the token used to authorize a payment.
- [ApplePayPayment](applepaypayment.md)
  The result of authorizing a payment request that contains payment information.
- [ApplePayPaymentAuthorizationResult](applepaypaymentauthorizationresult.md)
  The result of payment authorization, including status and errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaysession/completepayment)*