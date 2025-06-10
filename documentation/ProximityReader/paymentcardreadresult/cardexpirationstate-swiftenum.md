# PaymentCardReadResult.CardExpirationState

**Framework**: ProximityReader  
**Kind**: enum

Values that describe the expiration state of the card that the system read.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
enum CardExpirationState
```

## Topics

### Operators
- [static func == (PaymentCardReadResult.CardExpirationState, PaymentCardReadResult.CardExpirationState) -> Bool](paymentcardreadresult/cardexpirationstate-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [PaymentCardReadResult.CardExpirationState.expired](paymentcardreadresult/cardexpirationstate-swift.enum/expired.md)
  The card is expired.
- [PaymentCardReadResult.CardExpirationState.invalid](paymentcardreadresult/cardexpirationstate-swift.enum/invalid.md)
  The card expiration date is invalid.
- [PaymentCardReadResult.CardExpirationState.notExpired](paymentcardreadresult/cardexpirationstate-swift.enum/notexpired.md)
  The card is valid.
- [PaymentCardReadResult.CardExpirationState.unknown](paymentcardreadresult/cardexpirationstate-swift.enum/unknown.md)
  The card expiration date is not available.
### Instance Properties
- [var hashValue: Int](paymentcardreadresult/cardexpirationstate-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](paymentcardreadresult/cardexpirationstate-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](paymentcardreadresult/cardexpirationstate-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadresult/cardexpirationstate-swift.enum)*