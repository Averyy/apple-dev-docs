# PaymentCardReadResult.CardEffectiveState

**Framework**: ProximityReader  
**Kind**: enum

Values that describe the effective state of the card that was read.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
enum CardEffectiveState
```

## Topics

### Operators
- [static func == (PaymentCardReadResult.CardEffectiveState, PaymentCardReadResult.CardEffectiveState) -> Bool](paymentcardreadresult/cardeffectivestate-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [PaymentCardReadResult.CardEffectiveState.active](paymentcardreadresult/cardeffectivestate-swift.enum/active.md)
  The card is active.
- [PaymentCardReadResult.CardEffectiveState.inactive](paymentcardreadresult/cardeffectivestate-swift.enum/inactive.md)
  The card is inactive.
- [PaymentCardReadResult.CardEffectiveState.invalid](paymentcardreadresult/cardeffectivestate-swift.enum/invalid.md)
  The card effective state is invalid.
- [PaymentCardReadResult.CardEffectiveState.unknown](paymentcardreadresult/cardeffectivestate-swift.enum/unknown.md)
  The card effective state is not available.
### Instance Properties
- [var hashValue: Int](paymentcardreadresult/cardeffectivestate-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](paymentcardreadresult/cardeffectivestate-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](paymentcardreadresult/cardeffectivestate-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadresult/cardeffectivestate-swift.enum)*