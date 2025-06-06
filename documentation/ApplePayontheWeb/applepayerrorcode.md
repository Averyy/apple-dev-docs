# ApplePayErrorCode

**Framework**: Apple Pay on the Web  
**Kind**: enum

The error code that indicates whether an error on the payment sheet is for shipping or billing information, or for another kind of error.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
enum ApplePayErrorCode
```

#### Overview

Use the following error codes in the [`code`](applepayerror/code.md) property of [`ApplePayError`](applepayerror.md):

## Topics

### Enumeration Cases
- [addressUnserviceable](applepayerrorcode/addressunserviceable.md)
- [billingContactInvalid](applepayerrorcode/billingcontactinvalid.md)
- [couponCodeExpired](applepayerrorcode/couponcodeexpired.md)
- [couponCodeInvalid](applepayerrorcode/couponcodeinvalid.md)
- [shippingContactInvalid](applepayerrorcode/shippingcontactinvalid.md)
- [unknown](applepayerrorcode/unknown.md)

## See Also

- [ApplePayError](applepayerror.md)
  A customizable error type that you create to indicate problems with the address or contact information on an Apple Pay sheet.
- [ApplePayErrorContactField](applepayerrorcontactfield.md)
  Names of the fields in the shipping or billing contact information, used to locate errors in the payment sheet.
- [Apple Pay Status Codes](apple-pay-status-codes.md)
  Codes used to report the status of an Apple Pay session after a callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayerrorcode)*