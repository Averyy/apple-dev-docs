# type

**Framework**: Passkit  
**Kind**: property

A value that represents the card’s type.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var type: PKPaymentMethodType { get }
```

#### Discussion

For a list of possible card types, see [`PKPaymentMethodType`](pkpaymentmethodtype.md).

> **Note**:  Some older cards might not have card type information. Those cards have the value [`PKPaymentMethodType.unknown`](pkpaymentmethodtype/unknown.md).

## See Also

- [enum PKPaymentMethodType](pkpaymentmethodtype.md)
  The type of cards available in Apple Pay.
- [var displayName: String?](pkpaymentmethod/displayname.md)
  A string, suitable for display, that describes the card.
- [var network: PKPaymentNetwork?](pkpaymentmethod/network.md)
  A string, suitable for display, that describes the payment network for the card.
- [var billingAddress: CNContact?](pkpaymentmethod/billingaddress.md)
  The user’s billing address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentmethod/type)*