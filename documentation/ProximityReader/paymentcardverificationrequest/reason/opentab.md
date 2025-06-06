# PaymentCardVerificationRequest.Reason.openTab

**Framework**: ProximityReader  
**Kind**: case

Check if the card is valid.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
case openTab
```

#### Discussion

Choose this reason when you aren’t ready to complete the purchase yet, but want to verify that the person’s credit card information is valid.

## See Also

- [PaymentCardVerificationRequest.Reason.lookUp](paymentcardverificationrequest/reason/lookup.md)
  Verify the payment card to look up a past transaction.
- [PaymentCardVerificationRequest.Reason.saveCard](paymentcardverificationrequest/reason/savecard.md)
  Save the card information for later.
- [PaymentCardVerificationRequest.Reason.other](paymentcardverificationrequest/reason/other.md)
  Verify the card information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardverificationrequest/reason/opentab)*