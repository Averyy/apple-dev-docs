# PaymentCardVerificationRequest.Reason

**Framework**: ProximityReader  
**Kind**: enum

The reason for the verification request.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
enum Reason
```

## Topics

### Getting the verification reason
- [PaymentCardVerificationRequest.Reason.lookUp](paymentcardverificationrequest/reason/lookup.md)
  Verify the payment card to look up a past transaction.
- [PaymentCardVerificationRequest.Reason.openTab](paymentcardverificationrequest/reason/opentab.md)
  Check if the card is valid.
- [PaymentCardVerificationRequest.Reason.saveCard](paymentcardverificationrequest/reason/savecard.md)
  Save the card information for later.
- [PaymentCardVerificationRequest.Reason.other](paymentcardverificationrequest/reason/other.md)
  Verify the card information.
### Operators
- [static func == (PaymentCardVerificationRequest.Reason, PaymentCardVerificationRequest.Reason) -> Bool](paymentcardverificationrequest/reason/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](paymentcardverificationrequest/reason/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](paymentcardverificationrequest/reason/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](paymentcardverificationrequest/reason/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let currencyCode: String](paymentcardverificationrequest/currencycode.md)
  The ISO 4217 code that indicates the currency type.
- [let verificationReason: PaymentCardVerificationRequest.Reason](paymentcardverificationrequest/verificationreason.md)
  The reason you asked to verify someone’s card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardverificationrequest/reason)*