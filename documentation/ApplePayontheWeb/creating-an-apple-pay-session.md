# Creating an Apple Pay Session

**Framework**: Apple Pay on the Web

Provide a payment request and create the session.

#### Overview

After you’ve checked that the Apple Pay JS API is available and is enabled on the current device, you’re ready to create the payment request and start the session.  You can create a session only when a user explicitly asks to make a payment.  For example, you can create the session when the user taps the Apple Pay button.

You supply two parameters to [`ApplePaySession`](applepaysession/applepaysession.md):

- Version number. The Apple Pay version you’re using.  (See doc://com.apple.documentation/documentation/apple_pay_on_the_web/apple_pay_on_the_web_version_history for version information.)
- Payment Request. An [`ApplePayPaymentRequest`](applepaypaymentrequest.md) dictionary that contains all the information needed to display the payment sheet.

Creating an [`ApplePaySession`](applepaysession.md) object throws a JavaScript exception if any of the following occur:

- Any Apple Pay JS API is called from an insecure page.
- You pass an invalid payment request. Payment requests are invalid if they contain missing, unknown, or invalid properties, or if they have a total that is zero or less.
- You attempt to create the [`ApplePaySession`](applepaysession.md) outside of a user gesture handler.  The exception error  “Must create a new ApplePaySession from a user gesture handler” appears.

After the session is created, call its [`begin`](applepaysession/begin.md) method to show the payment sheet.

[`Creating an Apple Pay Session`](creating-an-apple-pay-session.md) shows creating a payment request and a new Apple Pay session, and displaying the payment sheet.

Listing 1. Example of constructing an Apple Pay session

```javascript
var request = {
  countryCode: 'US',
  currencyCode: 'USD',
  supportedNetworks: ['visa', 'masterCard', 'amex', 'discover'],
  merchantCapabilities: ['supports3DS'],
  total: { label: 'Your Merchant Name', amount: '10.00' },
}
var session = new ApplePaySession(3, request);
```

## See Also

- [Providing Merchant Validation](providing-merchant-validation.md)
  Validate your merchant identity and receive a session object for each payment request.
- [Requesting an Apple Pay payment session](requesting-an-apple-pay-payment-session.md)
  Request a valid session from the Apple Pay server.
- [ApplePaySession](applepaysession.md)
  A session object for managing the payment process on the web.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/creating-an-apple-pay-session)*