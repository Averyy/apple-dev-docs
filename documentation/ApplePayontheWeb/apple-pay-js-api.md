# Apple Pay JS API

**Framework**: Apple Pay on the Web

Implement Apple Pay on the web using Apple’s JavaScript API.

## Topics

### Apple Pay availability
- [Checking for Apple Pay availability](checking-for-apple-pay-availability.md)
  Use the Apple Pay JS API to check whether Apple Pay is available, to check whether a device has a payment credential provisioned in Wallet, and to determine when to display an Apple Pay button.
- [canMakePayments](applepaysession/canmakepayments.md)
  Indicates whether the device supports Apple Pay.
- [applePayCapabilities](applepaysession/applepaycapabilities.md)
  Indicates whether the device supports Apple Pay and whether the person has an active card in Wallet that qualifies for web payments.
- [canMakePaymentsWithActiveCard](applepaysession/canmakepaymentswithactivecard.md)
  Indicates whether the device supports Apple Pay and whether the user has an active card in Wallet.
- [PaymentCredentialStatus](paymentcredentialstatus.md)
  Information about whether the device supports Apple Pay and the possible payment credentials the person has provisioned in Wallet.
- [PaymentCredentialStatusResponse](paymentcredentialstatusresponse.md)
  The response for information about the device’s support for Apple Pay and the payment credential status.
### Apple Pay payment request
- [ApplePayPaymentRequest](applepaypaymentrequest.md)
  A request for payment, which includes information about payment-processing capabilities, the payment amount, and shipping information.
- [ApplePayDeferredPaymentRequest](applepaydeferredpaymentrequest.md)
  A dictionary that represents a request to set up a deferred payment, such as a hotel booking or a pre-order.
### Apple Pay session
- [Creating an Apple Pay Session](creating-an-apple-pay-session.md)
  Provide a payment request and create the session.
- [Providing Merchant Validation](providing-merchant-validation.md)
  Validate your merchant identity and receive a session object for each payment request.
- [Requesting an Apple Pay payment session](requesting-an-apple-pay-payment-session.md)
  Request a valid session from the Apple Pay server.
- [ApplePaySession](applepaysession.md)
  A session object for managing the payment process on the web.
### Status and errors
- [ApplePayError](applepayerror.md)
  A customizable error type that you create to indicate problems with the address or contact information on an Apple Pay sheet.
- [ApplePayErrorCode](applepayerrorcode.md)
  The error code that indicates whether an error on the payment sheet is for shipping or billing information, or for another kind of error.
- [ApplePayErrorContactField](applepayerrorcontactfield.md)
  Names of the fields in the shipping or billing contact information, used to locate errors in the payment sheet.
- [Apple Pay Status Codes](apple-pay-status-codes.md)
  Codes used to report the status of an Apple Pay session after a callback.

## See Also

- [Choosing an API for Implementing Apple Pay on Your Website](choosing-an-api-for-implementing-apple-pay-on-your-website.md)
  Compare Apple Pay JS and Payment Request API to choose the right implementation for your website.
- [Apple Pay on the Web version history](apple-pay-on-the-web-version-history.md)
  Learn about features in each version of Apple Pay on the Web.
- [Payment Request API](payment-request-api.md)
  Accept payments on your website with Apple Pay using the Payment Request API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/apple-pay-js-api)*