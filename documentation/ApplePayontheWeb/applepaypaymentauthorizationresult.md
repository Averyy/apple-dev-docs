# ApplePayPaymentAuthorizationResult

**Framework**: Apple Pay on the Web  
**Kind**: struct

The result of payment authorization, including status and errors.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
dictionary ApplePayPaymentAuthorizationResult {
	required short status;
	sequence <ApplePayError> errors;
	ApplePayPaymentOrderDetails orderDetails;
};
```

## Mentions

- [Apple Pay on the Web Version 3 Release Notes](apple-pay-on-the-web-version-3-release-notes.md)

#### Overview

Use the [`Apple Pay Status Codes`](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/apple_pay_status_codes) values of [`STATUS_SUCCESS`](applepaysession/status_success.md) to indicate when the payment authorization succeeds, or [`STATUS_FAILURE`](applepaysession/status_failure.md), along with the errors, when it fails.

## Topics

### Providing authorization results
- [status](applepaypaymentauthorizationresult/status.md)
  The status code for the authorization result.
- [errors](applepaypaymentauthorizationresult/errors.md)
  A list of custom errors to display on the payment sheet.
### Providing order details
- [orderDetails](applepaypaymentauthorizationresult/orderdetails.md)
  Optional metadata for an order that the customer placed using this payment method.
- [ApplePayPaymentOrderDetails](applepaypaymentorderdetails.md)
  A dictionary that contains metadata related to an order.

## See Also

- [onpaymentauthorized](applepaysession/onpaymentauthorized.md)
  An event handler the system calls when the user has authorized the Apple Pay payment with Touch ID, Face ID, or a passcode.
- [completePayment](applepaysession/completepayment.md)
  Completes the payment authorization with a result.
- [ApplePayPaymentAuthorizedEvent](applepaypaymentauthorizedevent.md)
  An event object that contains the token used to authorize a payment.
- [ApplePayPayment](applepaypayment.md)
  The result of authorizing a payment request that contains payment information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentauthorizationresult)*