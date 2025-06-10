# Apple Pay Status Codes

**Framework**: Apple Pay on the Web

Codes used to report the status of an Apple Pay session after a callback.

#### Overview

Use an appropriate status code to report your status when you complete a callback.

> **Note**:  Use a status code that is supported for the completion method you are calling.

| Method | Supported status codes |
| --- | --- |
| [`completePayment`](applepaysession/completepayment.md) | [`STATUS_SUCCESS`](applepaysession/status_success.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`STATUS_FAILURE`](applepaysession/status_failure.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Use for Apple Pay API version 2 or earlier: ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`STATUS_INVALID_BILLING_POSTAL_ADDRESS`](applepaysession/status_invalid_billing_postal_address.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`STATUS_INVALID_SHIPPING_POSTAL_ADDRESS`](applepaysession/status_invalid_shipping_postal_address.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`STATUS_INVALID_SHIPPING_CONTACT`](applepaysession/status_invalid_shipping_contact.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`STATUS_PIN_INCORRECT`](applepaysession/status_pin_incorrect.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`STATUS_PIN_LOCKOUT`](applepaysession/status_pin_lockout.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`STATUS_PIN_REQUIRED`](applepaysession/status_pin_required.md) |
| [`completeShippingContactSelection`](applepaysession/completeshippingcontactselection.md) | [`STATUS_SUCCESS`](applepaysession/status_success.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`STATUS_FAILURE`](applepaysession/status_failure.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) Use for Apple Pay API version 2 or earlier: ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`STATUS_INVALID_SHIPPING_POSTAL_ADDRESS`](applepaysession/status_invalid_shipping_postal_address.md) |
| [`completeShippingMethodSelection`](applepaysession/completeshippingmethodselection.md) | [`STATUS_SUCCESS`](applepaysession/status_success.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`STATUS_FAILURE`](applepaysession/status_failure.md) |

Apple Pay JS API supports customized errors in Apple Pay API version 3 and later. Use only [`STATUS_SUCCESS`](applepaysession/status_success.md) and [`STATUS_FAILURE`](applepaysession/status_failure.md) for code using version 3. See [`ApplePayError`](applepayerror.md) for information on custom errors.

## Topics

### Status Code Constants
- [STATUS_FAILURE](applepaysession/status_failure.md)
  The requested action failed.
- [STATUS_SUCCESS](applepaysession/status_success.md)
  The requested action succeeded.
- [STATUS_INVALID_BILLING_POSTAL_ADDRESS](applepaysession/status_invalid_billing_postal_address.md)
  The billing address is invalid.
- [STATUS_INVALID_SHIPPING_POSTAL_ADDRESS](applepaysession/status_invalid_shipping_postal_address.md)
  The shipping address is invalid.
- [STATUS_INVALID_SHIPPING_CONTACT](applepaysession/status_invalid_shipping_contact.md)
  The shipping contact information is invalid.
- [STATUS_PIN_INCORRECT](applepaysession/status_pin_incorrect.md)
  The PIN information is not valid.
- [STATUS_PIN_LOCKOUT](applepaysession/status_pin_lockout.md)
  The maximum number of tries for a PIN has been reached and the user has been locked out.
- [STATUS_PIN_REQUIRED](applepaysession/status_pin_required.md)
  The required PIN information was not provided.

## See Also

- [supportsVersion](applepaysession/supportsversion.md)
  Detects whether a web browser supports a particular Apple Pay version.
- [ApplePayError](applepayerror.md)
  A customizable error type that you create to indicate problems with the address or contact information on an Apple Pay sheet.
- [ApplePayErrorCode](applepayerrorcode.md)
  The error code that indicates whether an error on the payment sheet is for shipping or billing information, or for another kind of error.
- [ApplePayErrorContactField](applepayerrorcontactfield.md)
  Names of the fields in the shipping or billing contact information, used to locate errors in the payment sheet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/apple-pay-status-codes)*