# PaymentCardReadResult.CardExpirationState

**Framework**: ProximityReader  
**Kind**: enum  
**Role**: Enumeration

Values that describe the expiration state of the card that the system read.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
enum CardExpirationState
```

## Topics

### Enumeration Cases
- [PaymentCardReadResult.CardExpirationState.expired](./cardexpirationstate-swift.enum/expired.md)
  The card is expired.
- [PaymentCardReadResult.CardExpirationState.invalid](./cardexpirationstate-swift.enum/invalid.md)
  The card expiration date is invalid.
- [PaymentCardReadResult.CardExpirationState.notExpired](./cardexpirationstate-swift.enum/notexpired.md)
  The card is valid.
- [PaymentCardReadResult.CardExpirationState.unknown](./cardexpirationstate-swift.enum/unknown.md)
  The card expiration date is not available.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadresult/cardexpirationstate-swift.enum)*