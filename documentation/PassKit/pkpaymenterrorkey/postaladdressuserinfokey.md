# postalAddressUserInfoKey

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Type Property

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

```c
extern PKPaymentErrorKey const PKPaymentErrorPostalAddressUserInfoKey;
```

#### Discussion

See [`CNPostalAddress`](../../Contacts/cnpostaladdress.md) for the values that can be used with this key. These values point to the specific area of the address that is at fault, for example, [`CNPostalAddressStreetKey`](../../Contacts/cnpostaladdressstreetkey.md) indicates the street. When you supply the key values in a payment error, the Apple Pay sheet highlights the appropriate field, enabling the user to correct errors.

## See Also

### Error keys
- [static let contactFieldUserInfoKey: PKPaymentErrorKey](./contactfielduserinfokey.md)
  Payment error key that indicates errors with the contact information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymenterrorkey/postaladdressuserinfokey)*