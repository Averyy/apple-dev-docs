# billingContact

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A prepopulated billing address.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var billingContact: PKContact? { get set }
```

#### Discussion

If you have an up-to-date billing address on file, you can set it here. This billing address appears in the payment sheet. The user can either use the address you specify or select a different address.

Note that a [`PKContact`](pkcontact.md) object that represents a billing contact contains information for only the [`postalAddress`](pkcontact/postaladdress.md) property. All other properties in the object are set to `nil`.

## See Also

- [var shippingContact: PKContact?](pkpaymentrequest/shippingcontact.md)
  A prepopulated shipping address.
- [class PKContact](pkcontact.md)
  An object that encapsulates contact information needed for billing and shipping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/billingcontact)*