# PKPaymentMethodType

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum

The type of cards available in Apple Pay.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum PKPaymentMethodType
```

## Topics

### Payment Method Type Constants
- [PKPaymentMethodType.unknown](pkpaymentmethodtype/unknown.md)
  The card’s type is unknown.
- [PKPaymentMethodType.debit](pkpaymentmethodtype/debit.md)
  A debit card.
- [PKPaymentMethodType.eMoney](pkpaymentmethodtype/emoney.md)
  An electronic money card.
- [PKPaymentMethodType.credit](pkpaymentmethodtype/credit.md)
  A credit card.
- [PKPaymentMethodType.prepaid](pkpaymentmethodtype/prepaid.md)
  A prepaid card.
- [PKPaymentMethodType.store](pkpaymentmethodtype/store.md)
  A store card.
### Initializers
- [init?(rawValue: UInt)](pkpaymentmethodtype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var type: PKPaymentMethodType](pkpaymentmethod/type.md)
  A value that represents the card’s type.
- [var displayName: String?](pkpaymentmethod/displayname.md)
  A string, suitable for display, that describes the card.
- [var network: PKPaymentNetwork?](pkpaymentmethod/network.md)
  A string, suitable for display, that describes the payment network for the card.
- [var billingAddress: CNContact?](pkpaymentmethod/billingaddress.md)
  The user’s billing address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentmethodtype)*