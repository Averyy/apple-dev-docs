# STATUS_SUCCESS

**Framework**: Apple Pay on the Web  
**Kind**: var

The requested action succeeded.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
const unsigned short STATUS_SUCCESS;
```

#### Discussion

When you call [`completePayment`](applepaysession/completepayment.md) with [`STATUS_SUCCESS`](applepaysession/status_success.md), the payment sheet shows that the transaction was successful, and the sheet is dismissed . For all other methods, the payment sheet remains open.

## See Also

- [STATUS_FAILURE](applepaysession/status_failure.md)
  The requested action failed.
- [STATUS_INVALID_BILLING_POSTAL_ADDRESS](applepaysession/status_invalid_billing_postal_address.md)
  The billing address is invalid.
- [STATUS_INVALID_SHIPPING_CONTACT](applepaysession/status_invalid_shipping_contact.md)
  The shipping contact information is invalid.
- [STATUS_INVALID_SHIPPING_POSTAL_ADDRESS](applepaysession/status_invalid_shipping_postal_address.md)
  The shipping address is invalid.
- [STATUS_PIN_INCORRECT](applepaysession/status_pin_incorrect.md)
  The PIN information is not valid.
- [STATUS_PIN_LOCKOUT](applepaysession/status_pin_lockout.md)
  The maximum number of tries for a PIN has been reached and the user has been locked out.
- [STATUS_PIN_REQUIRED](applepaysession/status_pin_required.md)
  The required PIN information was not provided.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaysession/status_success)*