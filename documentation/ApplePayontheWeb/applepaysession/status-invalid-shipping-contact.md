# STATUS_INVALID_SHIPPING_CONTACT

**Framework**: Apple Pay on the Web  
**Kind**: var

The shipping contact information is invalid.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
const unsigned short STATUS_INVALID_SHIPPING_CONTACT;
```

#### Discussion

Use this status code only for Apple Pay API version 1 or 2 style calls. For version 3, use an [`ApplePayError`](applepayerror.md) with a status of [`STATUS_FAILURE`](applepaysession/status_failure.md)  and error code instead.

The payment sheet remains open and shows the email address and/or phone number highlighted in red.

## See Also

- [supportsVersion](applepaysession/supportsversion.md)
  Detects whether a web browser supports a particular Apple Pay version.
- [STATUS_FAILURE](applepaysession/status_failure.md)
  The requested action failed.
- [STATUS_INVALID_BILLING_POSTAL_ADDRESS](applepaysession/status_invalid_billing_postal_address.md)
  The billing address is invalid.
- [STATUS_INVALID_SHIPPING_POSTAL_ADDRESS](applepaysession/status_invalid_shipping_postal_address.md)
  The shipping address is invalid.
- [STATUS_PIN_INCORRECT](applepaysession/status_pin_incorrect.md)
  The PIN information is not valid.
- [STATUS_PIN_LOCKOUT](applepaysession/status_pin_lockout.md)
  The maximum number of tries for a PIN has been reached and the user has been locked out.
- [STATUS_PIN_REQUIRED](applepaysession/status_pin_required.md)
  The required PIN information was not provided.
- [STATUS_SUCCESS](applepaysession/status_success.md)
  The requested action succeeded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaysession/status_invalid_shipping_contact)*