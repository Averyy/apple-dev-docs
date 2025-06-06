# Providing Merchant Validation

**Framework**: Apple Pay on the Web

Validate your merchant identity and receive a session object for each payment request.

#### Overview

As soon as the system displays the payment sheet, the Apple Pay JS API calls your session object’s [`onvalidatemerchant`](applepaysession/onvalidatemerchant.md) event handler to verify that the request is coming from a valid merchant. It passes the function an [`ApplePayValidateMerchantEvent`](applepayvalidatemerchantevent.md) object that contains the validation URL.

> ❗ **Important**:  The URL you receive can vary, so always use the URL provided in the [`validationURL`](applepayvalidatemerchantevent/validationurl.md) property. Your server must provide allow-listed access to all the validation URLs, specified in [`Setting Up Your Server`](https://developer.apple.com/documentation/apple_pay_on_the_web/setting_up_your_server).

 The URL you receive can vary, so always use the URL provided in the [`validationURL`](applepayvalidatemerchantevent/validationurl.md) property. Your server must provide allow-listed access to all the validation URLs, specified in [`Setting Up Your Server`](https://developer.apple.com/documentation/apple_pay_on_the_web/setting_up_your_server).

In your [`onvalidatemerchant`](applepaysession/onvalidatemerchant.md) function:

1. You call your server, passing it the URL from the event’s [`validationURL`](applepayvalidatemerchantevent/validationurl.md) property.
2. Your server uses the validation URL to request a session from the Apple Pay server, as described in [`Requesting an Apple Pay payment session`](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/requesting_an_apple_pay_payment_session). Never send the request for a merchant session from the client.
3. In response, your server receives an opaque merchant session object.
4. You pass the merchant session object to your Apple Pay session’s [`completeMerchantValidation`](applepaysession/completemerchantvalidation.md) method. You can use the merchant session object a single time. It expires five minutes after it is created.

## See Also

- [Configuring Your Environment](configuring-your-environment.md)
  Create your Apple Pay merchant ID and certificates, and verify your domain.
- [Setting Up Your Server](setting-up-your-server.md)
  Set up your server for secure communications with Apple Pay.
- [Creating an Apple Pay Session](creating-an-apple-pay-session.md)
  Provide a payment request and create the session.
- [Requesting an Apple Pay payment session](requesting-an-apple-pay-payment-session.md)
  Request a valid session from the Apple Pay server.
- [ApplePaySession](applepaysession.md)
  A session object for managing the payment process on the web.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/providing-merchant-validation)*