# ApplePayPaymentAuthorizedEvent

**Framework**: Apple Pay on the Web  
**Kind**: class

An event object that contains the token used to authorize a payment.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
interface ApplePayPaymentAuthorizedEvent
```

#### Overview

The event handler [`onpaymentauthorized`](applepaysession/onpaymentauthorized.md) receives this event object when a payment is authorized.

## Topics

### Payment property
- [payment](applepaypaymentauthorizedevent/payment.md)
  The authorized payment information for this transaction.

## See Also

- [onpaymentauthorized](applepaysession/onpaymentauthorized.md)
  An event handler the system calls when the user has authorized the Apple Pay payment with Touch ID, Face ID, or a passcode.
- [completePayment](applepaysession/completepayment.md)
  Completes the payment authorization with a result.
- [ApplePayPayment](applepaypayment.md)
  The result of authorizing a payment request that contains payment information.
- [ApplePayPaymentAuthorizationResult](applepaypaymentauthorizationresult.md)
  The result of payment authorization, including status and errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentauthorizedevent)*