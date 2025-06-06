# contactFieldUserInfoKey

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

Payment error key that indicates errors with the contact information.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
static let contactFieldUserInfoKey: PKPaymentErrorKey
```

#### Discussion

See [`PKContactField`](pkcontactfield.md) for the values to use with this key.

Use this key with the error code [`PKPaymentError.Code.shippingContactInvalidError`](pkpaymenterror/code/shippingcontactinvaliderror.md) to indicate an error in the name, email address, phone number, or the shipping address as a whole.

Use this key with the error code [`billingContactInvalidError`](pkpaymenterror/billingcontactinvaliderror.md)  to indicate an error with the billing address as a whole, or billing name.

The example code in [`Listing 1`](https://developer.apple.comhttps://developer.apple.com/library/archive/qa/qa1639/_index.html#//apple_ref/doc/uid/DTS40008751-CH1-SOURCECODE2) shows the [`contactFieldUserInfoKey`](pkpaymenterrorkey/contactfielduserinfokey.md) used to indicate a phone number error.

The following example shows an error indicating a problem with the shipping contact’s phone number.

```swift
let phoneError = NSError.init(domain: PKPaymentErrorDomain,
                               code: PKPaymentError.shippingContactInvalidError.rawValue,
                               userInfo: [NSLocalizedDescriptionKey:"Phone number is invalid",
                               PKPaymentErrorKey.contactFieldUserInfoKey:PKContactField.phoneNumber])
```

## See Also

- [static let postalAddressUserInfoKey: PKPaymentErrorKey](pkpaymenterrorkey/postaladdressuserinfokey.md)
  Payment error key that indicates errors with the postal address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenterrorkey/contactfielduserinfokey)*