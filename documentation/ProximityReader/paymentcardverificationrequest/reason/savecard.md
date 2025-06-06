# PaymentCardVerificationRequest.Reason.saveCard

**Framework**: ProximityReader  
**Kind**: case

Save the card information for later.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
case saveCard
```

#### Discussion

If your application saves card data, it’s your responsibility to ensure that the customer is aware of how and why before you read their card.

## See Also

- [PaymentCardVerificationRequest.Reason.lookUp](paymentcardverificationrequest/reason/lookup.md)
  Verify the payment card to look up a past transaction.
- [PaymentCardVerificationRequest.Reason.openTab](paymentcardverificationrequest/reason/opentab.md)
  Check if the card is valid.
- [PaymentCardVerificationRequest.Reason.other](paymentcardverificationrequest/reason/other.md)
  Verify the card information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardverificationrequest/reason/savecard)*