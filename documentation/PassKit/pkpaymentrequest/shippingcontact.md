# shippingContact

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

A prepopulated shipping address.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var shippingContact: PKContact? { get set }
```

## Mentions

- [Displaying a Read-Only Pickup Address](displaying-a-read-only-pickup-address.md)

#### Discussion

If you have an up-to-date shipping address on file, you can set this property to that address. This shipping address appears in the payment sheet. When the framework presents the [`PKPaymentAuthorizationViewController`](pkpaymentauthorizationviewcontroller.md), the user can either keep the address you specified or enter a different address.

Note that a [`PKContact`](pkcontact.md) object that represents a shipping contact contains information for only the [`postalAddress`](pkcontact/postaladdress.md), [`emailAddress`](pkcontact/emailaddress.md), and [`phoneNumber`](pkcontact/phonenumber.md) properties. The framework sets all other properties in the object to `nil`.

## See Also

- [var billingContact: PKContact?](pkpaymentrequest/billingcontact.md)
  A prepopulated billing address.
- [class PKContact](pkcontact.md)
  An object that encapsulates contact information needed for billing and shipping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/shippingcontact)*