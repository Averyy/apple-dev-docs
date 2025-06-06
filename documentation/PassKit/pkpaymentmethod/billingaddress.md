# billingAddress

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The user’s billing address.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@NSCopying
var billingAddress: CNContact? { get }
```

#### Discussion

For privacy, PassKit partially redacts the user’s billing address. PassKit populates this property only when the app doesn’t request a shipping address.

## See Also

- [var type: PKPaymentMethodType](pkpaymentmethod/type.md)
  A value that represents the card’s type.
- [enum PKPaymentMethodType](pkpaymentmethodtype.md)
  The type of cards available in Apple Pay.
- [var displayName: String?](pkpaymentmethod/displayname.md)
  A string, suitable for display, that describes the card.
- [var network: PKPaymentNetwork?](pkpaymentmethod/network.md)
  A string, suitable for display, that describes the payment network for the card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentmethod/billingaddress)*