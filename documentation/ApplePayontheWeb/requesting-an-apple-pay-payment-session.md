# Requesting an Apple Pay payment session

**Framework**: Apple Pay on the Web

Request a valid session from the Apple Pay server.

#### Overview

Use a new Apple Pay payment session for each transaction.

##### Post a Request

Your server posts a request using mutual TLS (mTLS) by calling the Apple Pay server’s Payment Session endpoint.

The endpoint returns an opaque Apple Pay session object for Apple Pay on the web, Apple Pay on macOS, and for Apple Pay in Apple Messages for Business.

For Apple Pay on the web, you can also use the endpoint `POST https://<validation URL>/paymentSession` with a fully qualified validation URL that you receive in [`onvalidatemerchant`](applepaysession/onvalidatemerchant.md). Be sure to allow all of the domains listed in [`Setting Up Your Server`](https://developer.apple.com/documentation/apple_pay_on_the_web/setting_up_your_server).

> ❗ **Important**:  Ensure that your server accesses only the validation URLs provided by Apple in [`Setting Up Your Server`](https://developer.apple.com/documentation/apple_pay_on_the_web/setting_up_your_server), and fails for other URLs. It’s a best practice to use a strict allow list for the validation URLs. You must send the payment session request from your server; never request the session from the client.

 Ensure that your server accesses only the validation URLs provided by Apple in [`Setting Up Your Server`](https://developer.apple.com/documentation/apple_pay_on_the_web/setting_up_your_server), and fails for other URLs. It’s a best practice to use a strict allow list for the validation URLs. You must send the payment session request from your server; never request the session from the client.

##### Provide Request Parameters

Use the merchant identity certificate associated with your merchant ID in the request. See [`Configuring Your Environment`](https://developer.apple.com/documentation/apple_pay_on_the_web/configuring_your_environment) for more information.

The values for `initiative` and `initiativeContext` depend on the kind of application you’re building:

- For Apple Pay on the web, use `“web”` for the `initiative` parameter. For the `initiativeContext` parameter, provide your fully qualified domain name associated with your Apple Pay Merchant Identity Certificate.
- For Apple Messages for Business, use `“messaging”` for the `initiative` parameter. For the `initiativeContext` parameter, provide your payment gateway URL. See [`Type Interactive`](https://developer.apple.comhttps://register.apple.com/resources/messages/msp-rest-api/type-interactive) for more information.
- For Apple Pay on macOS, use `“in_app”` for the `initiative` parameter. For the `initiativeContext` parameter, provide your developer team ID.

On supported models of MacBook Pro, the Touch Bar displays the value you supply for the `displayName` parameter. The following table lists the valid fonts.

| Language | Font |
| --- | --- |
| Arabic | MyriadArabic-Regular.otf |
| Bengali | KohinoorBangla-Regular.otf |
| Chinese | PingFangTC-Regular.otf |
| English | SF-Compact-Text-Regular.otf |
| Hebrew | Myriad-Hebrew.ttc |
| Hindi | KohinoorDevanagari-Regular.otf |
| Japanese | PingFangTC-Regular.otf |
| Korean | NanumGothic.ttf |
| Telegu | KohinoorTelugu-Regular.otf |
| Thai | Ayuthaya.ttf |

##### Receive the Payment Session Object

In response to the `POST` request, your server receives an opaque Apple Pay session object. The session expires after five minutes.

- For Apple Pay on the web, pass the session object to the completion method, [`completeMerchantValidation`](applepaysession/completemerchantvalidation.md).
- For Apple Pay in Apple Messages for Business, pass the session object to your Messaging Service Provider (MSP), which handles communicating with Apple Messages for Business on your behalf.

##### Example

A session request with a JSON payload for Apple Pay on the web.

```javascript
{
    merchantIdentifier: "merchant.com.example.mystore",
    displayName: "MyStore",
    initiative: "web",
    initiativeContext: "mystore.example.com"
}
```

The `displayName` you provide in the payload appears in the Touch Bar like this:

![A screenshot of the Touch Bar requesting Touch ID for an Apple Pay transaction.](https://docs-assets.developer.apple.com/published/73df4987bb2df22455118477c50306ab/media-3199964%402x.png)

> **Note**:  Start Session is being phased out and replaced by Payment Session.

 Start Session is being phased out and replaced by Payment Session.

## See Also

- [Creating an Apple Pay Session](creating-an-apple-pay-session.md)
  Provide a payment request and create the session.
- [Providing Merchant Validation](providing-merchant-validation.md)
  Validate your merchant identity and receive a session object for each payment request.
- [ApplePaySession](applepaysession.md)
  A session object for managing the payment process on the web.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/requesting-an-apple-pay-payment-session)*