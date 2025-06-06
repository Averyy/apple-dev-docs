# onvalidatemerchant

**Framework**: Applepayontheweb  
**Kind**: property

An event handler the system calls when it displays the payment sheet.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
attribute EventHandler onvalidatemerchant;
```

## Mentions

- [Providing Merchant Validation](providing-merchant-validation.md)
- [Requesting an Apple Pay payment session](requesting-an-apple-pay-payment-session.md)

#### Discussion

Use this attribute to request and return a merchant session. You must set this attribute to the following function:

```javascript
session.onvalidatemerchant = function(event) {}
```

where `event` is an [`ApplePayValidateMerchantEvent`](applepayvalidatemerchantevent.md) object.

The process to complete the merchant validation is as follows:

1. Your [`onvalidatemerchant`](applepaysession/onvalidatemerchant.md) function calls your server, and passes it the static hostname `apple-pay-gateway.apple.com` as the validation URL. In the China region, use `cn-apple-pay-gateway.apple.com`.
2. Your server uses the validation URL to request a session from the Apple Pay server, as described in [`Requesting an Apple Pay payment session`](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/requesting_an_apple_pay_payment_session).
3. In response, your server receives an opaque merchant session object, `MerchantSession`.
4. You pass the merchant session object to the completion method, [`completeMerchantValidation`](applepaysession/completemerchantvalidation.md).

The system enables the payment sheet.

> **Note**:  Previous merchant validation instructions stated that your [`onvalidatemerchant`](applepaysession/onvalidatemerchant.md) function must call your server and pass it the URL from the event’s [`validationURL`](applepayvalidatemerchantevent/validationurl.md) attribute. Apple Pay continues to support this flow for existing implementations.

## See Also

- [Providing Merchant Validation](providing-merchant-validation.md)
  Validate your merchant identity and receive a session object for each payment request.
- [begin](applepaysession/begin.md)
  Begins the merchant validation process.
- [completeMerchantValidation](applepaysession/completemerchantvalidation.md)
  Completes the validation for a merchant session.
- [ApplePayValidateMerchantEvent](applepayvalidatemerchantevent.md)
  An event object that contains the validation URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ApplePayontheWeb/applepaysession/onvalidatemerchant)*