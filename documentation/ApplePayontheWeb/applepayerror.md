# ApplePayError

**Framework**: Apple Pay on the Web  
**Kind**: class

A customizable error type that you create to indicate problems with the address or contact information on an Apple Pay sheet.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
interface ApplePayError
```

## Mentions

- [Apple Pay on the Web Version 3 Release Notes](apple-pay-on-the-web-version-3-release-notes.md)
- [Setting up the payment request API to accept Apple Pay](setting-up-the-payment-request-api-to-accept-apple-pay.md)
- [Choosing an API for Implementing Apple Pay on Your Website](choosing-an-api-for-implementing-apple-pay-on-your-website.md)

#### Overview

When you determine that there’s a problem with an address or contact information on the payment sheet, you can use [`ApplePayError`](applepayerror.md) to create a customized error message. Apple Pay highlights the area with an error and displays your message, making it easier for users to correct errors.

Users must resolve any errors that you report on the Apple Pay sheet before they can finalize their transaction.

The details you provide in an Apple Pay error include:

-  — An error code that identifies the area of the error.
-  — The specific field on the payment sheet with the error.
-  — Your custom error message to display on the payment sheet.

For example, if you found an error in the postal code of the shipping address, create an [`ApplePayError`](applepayerror.md) with the custom message text `"ZIP Code is invalid"`, as follows:

```javascript
new ApplePayError("shippingContactInvalid", "postalCode", "ZIP Code is invalid")
```

Apple Pay highlights the postal code field and displays the message text on the payment sheet.

> **Note**:  [`ApplePayError`](applepayerror.md) requires Apple Pay API version 3 and later, and is only supported in Apple Pay JS API; it’s not available in the [`Payment Request API`](https://developer.apple.com/documentation/apple_pay_on_the_web/payment_request_api).

 [`ApplePayError`](applepayerror.md) requires Apple Pay API version 3 and later, and is only supported in Apple Pay JS API; it’s not available in the [`Payment Request API`](https://developer.apple.com/documentation/apple_pay_on_the_web/payment_request_api).

## Topics

### Creating an Apple Pay Error
- [ApplePayError](applepayerror/applepayerror.md)
  Creates an Apple Pay error object.
### Error Properties
- [code](applepayerror/code.md)
  The error code for this instance.
- [contactField](applepayerror/contactfield.md)
  The field name that contains the error on the payment sheet.
- [message](applepayerror/message.md)
  A localized, user-facing string that describes the error.

## See Also

- [ApplePayErrorCode](applepayerrorcode.md)
  The error code that indicates whether an error on the payment sheet is for shipping or billing information, or for another kind of error.
- [ApplePayErrorContactField](applepayerrorcontactfield.md)
  Names of the fields in the shipping or billing contact information, used to locate errors in the payment sheet.
- [Apple Pay Status Codes](apple-pay-status-codes.md)
  Codes used to report the status of an Apple Pay session after a callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayerror)*