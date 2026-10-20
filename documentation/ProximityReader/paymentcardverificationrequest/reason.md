# PaymentCardVerificationRequest.Reason

**Framework**: ProximityReader  
**Kind**: enum  
**Role**: Enumeration

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
- [PaymentCardVerificationRequest.Reason.lookUp](./reason/lookup.md)
  Verify the payment card to look up a past transaction.
- [PaymentCardVerificationRequest.Reason.openTab](./reason/opentab.md)
  Check if the card is valid.
- [PaymentCardVerificationRequest.Reason.saveCard](./reason/savecard.md)
  Save the card information for later.
- [PaymentCardVerificationRequest.Reason.other](./reason/other.md)
  Verify the card information.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the request details
- [let currencyCode: String](./currencycode.md)
  The ISO 4217 code that indicates the currency type.
- [let verificationReason: PaymentCardVerificationRequest.Reason](./verificationreason.md)
  The reason you asked to verify someone’s card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardverificationrequest/reason)*