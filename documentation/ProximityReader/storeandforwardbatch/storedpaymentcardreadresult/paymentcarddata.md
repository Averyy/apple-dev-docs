# paymentCardData

**Framework**: ProximityReader  
**Kind**: property

A Base64-encoded string that contains the encrypted payment information to send to your payment provider.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- visionOS 2.4+

## Declaration

```swift
let paymentCardData: String
```

#### Discussion

This information is present any time the system reads a card, including for purchases, refunds, and card verification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/storeandforwardbatch/storedpaymentcardreadresult/paymentcarddata)*