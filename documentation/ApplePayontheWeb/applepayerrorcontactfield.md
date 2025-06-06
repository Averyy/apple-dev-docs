# ApplePayErrorContactField

**Framework**: Apple Pay on the Web  
**Kind**: enum

Names of the fields in the shipping or billing contact information, used to locate errors in the payment sheet.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
enum ApplePayErrorContactField
```

#### Overview

When shipping or billing contact information has an error, you use the error [`code`](applepayerror/code.md) values of either `"shippingContactInvalid"` or `"billingContactInvalid"` to indicate which one has the error. You use the contact field to indicate the exact field with the error. The corresponding field in the shipping or billing section of the payment sheet is highlighted.

Note that the remaining error codes, `"addressUnserviceable"` and `"unknown"`, do not require contact fields.

Use contact field values in the [`contactField`](applepayerror/contactfield.md) property of an [`ApplePayError`](applepayerror.md) when you return errors in the completion functions, as shown in the following table.

Contact field values are available in all versions of the API except as stated in the table.

| Contact Field Value | Completion methods that support `"shippingContactInvalid"` error code | Completion methods that support `"billingContactInvalid"` error code |
| --- | --- | --- |
| `"phoneNumber"` | [`completePayment`](applepaysession/completepayment.md) |  |
| `"emailAddress"` | [`completePayment`](applepaysession/completepayment.md) |  |
| `"name"` | [`completePayment`](applepaysession/completepayment.md) | [`completePayment`](applepaysession/completepayment.md) |
| `"phoneticName"` ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) (available starting in API version 3) | [`completePayment`](applepaysession/completepayment.md) | [`completePayment`](applepaysession/completepayment.md) |
| `"postalAddress"` | [`completeShippingContactSelection`](applepaysession/completeshippingcontactselection.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`completePayment`](applepaysession/completepayment.md) | [`completePayment`](applepaysession/completepayment.md) |
| `"addressLines"` | [`completePayment`](applepaysession/completepayment.md) | [`completePayment`](applepaysession/completepayment.md) |
| `"locality"` | [`completeShippingContactSelection`](applepaysession/completeshippingcontactselection.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`completePayment`](applepaysession/completepayment.md) | [`completePayment`](applepaysession/completepayment.md) |
| `"subLocality"` | [`completeShippingContactSelection`](applepaysession/completeshippingcontactselection.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`completePayment`](applepaysession/completepayment.md) | [`completePayment`](applepaysession/completepayment.md) |
| `"postalCode"` | [`completeShippingContactSelection`](applepaysession/completeshippingcontactselection.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`completePayment`](applepaysession/completepayment.md) | [`completePayment`](applepaysession/completepayment.md) |
| `"administrativeArea"` | [`completeShippingContactSelection`](applepaysession/completeshippingcontactselection.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`completePayment`](applepaysession/completepayment.md) | [`completePayment`](applepaysession/completepayment.md) |
| `"subAdministrativeArea"` | [`completeShippingContactSelection`](applepaysession/completeshippingcontactselection.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`completePayment`](applepaysession/completepayment.md) | [`completePayment`](applepaysession/completepayment.md) |
| `"country"` | [`completeShippingContactSelection`](applepaysession/completeshippingcontactselection.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`completePayment`](applepaysession/completepayment.md) | [`completePayment`](applepaysession/completepayment.md) |
| `"countryCode"` | [`completeShippingContactSelection`](applepaysession/completeshippingcontactselection.md) ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) [`completePayment`](applepaysession/completepayment.md) | [`completePayment`](applepaysession/completepayment.md) |

## Topics

### Enumeration Cases
- [addressLines](applepayerrorcontactfield/addresslines.md)
- [administrativeArea](applepayerrorcontactfield/administrativearea.md)
- [country](applepayerrorcontactfield/country.md)
- [countryCode](applepayerrorcontactfield/countrycode.md)
- [emailAddress](applepayerrorcontactfield/emailaddress.md)
- [locality](applepayerrorcontactfield/locality.md)
- [name](applepayerrorcontactfield/name.md)
- [phoneNumber](applepayerrorcontactfield/phonenumber.md)
- [phoneticName](applepayerrorcontactfield/phoneticname.md)
- [postalAddress](applepayerrorcontactfield/postaladdress.md)
- [postalCode](applepayerrorcontactfield/postalcode.md)
- [subAdministrativeArea](applepayerrorcontactfield/subadministrativearea.md)
- [subLocality](applepayerrorcontactfield/sublocality.md)

## See Also

- [ApplePayError](applepayerror.md)
  A customizable error type that you create to indicate problems with the address or contact information on an Apple Pay sheet.
- [ApplePayErrorCode](applepayerrorcode.md)
  The error code that indicates whether an error on the payment sheet is for shipping or billing information, or for another kind of error.
- [Apple Pay Status Codes](apple-pay-status-codes.md)
  Codes used to report the status of an Apple Pay session after a callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayerrorcontactfield)*