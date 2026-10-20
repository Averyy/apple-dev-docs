# verificationReason

**Framework**: ProximityReader  
**Kind**: property  
**Role**: Instance Property

The reason you asked to verify someone’s card.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
let verificationReason: PaymentCardVerificationRequest.Reason
```

#### Discussion

The system uses the supplied reason to display an appropriate message in the system UI about why they need to present their card.

## See Also

### Getting the request details
- [let currencyCode: String](./currencycode.md)
  The ISO 4217 code that indicates the currency type.
- [PaymentCardVerificationRequest.Reason](./reason.md)
  The reason for the verification request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardverificationrequest/verificationreason)*