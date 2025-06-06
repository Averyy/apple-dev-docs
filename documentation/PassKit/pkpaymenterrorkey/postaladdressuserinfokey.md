# postalAddressUserInfoKey

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

Payment error key that indicates errors with the postal address.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
static let postalAddressUserInfoKey: PKPaymentErrorKey
```

#### Discussion

See [`CNPostalAddress`](https://developer.apple.com/documentation/Contacts/CNPostalAddress) for the values that can be used with this key. These values point to the specific area of the address that is at fault, for example, [`CNPostalAddressStreetKey`](https://developer.apple.com/documentation/Contacts/CNPostalAddressStreetKey) indicates the street. When you supply the key values in a payment error, the Apple Pay sheet highlights the appropriate field, enabling the user to correct errors.

## See Also

- [static let contactFieldUserInfoKey: PKPaymentErrorKey](pkpaymenterrorkey/contactfielduserinfokey.md)
  Payment error key that indicates errors with the contact information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenterrorkey/postaladdressuserinfokey)*