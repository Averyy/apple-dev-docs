# STATUS_PIN_REQUIRED

**Framework**: Apple Pay on the Web  
**Kind**: var

The required PIN information was not provided.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
const unsigned short STATUS_PIN_REQUIRED;
```

## Discussion

Cards on the China Union Pay payment network may require a PIN to authenticate the transaction.

## See Also

### Status code constants
- [STATUS_FAILURE](./status_failure.md)
  The requested action failed.
- [STATUS_INVALID_BILLING_POSTAL_ADDRESS](./status_invalid_billing_postal_address.md)
  The billing address is invalid.
- [STATUS_INVALID_SHIPPING_CONTACT](./status_invalid_shipping_contact.md)
  The shipping contact information is invalid.
- [STATUS_INVALID_SHIPPING_POSTAL_ADDRESS](./status_invalid_shipping_postal_address.md)
  The shipping address is invalid.
- [STATUS_PIN_INCORRECT](./status_pin_incorrect.md)
  The PIN information is not valid.
- [STATUS_PIN_LOCKOUT](./status_pin_lockout.md)
  The maximum number of tries for a PIN has been reached and the user has been locked out.
- [STATUS_SUCCESS](./status_success.md)
  The requested action succeeded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaysession/status_pin_required)*