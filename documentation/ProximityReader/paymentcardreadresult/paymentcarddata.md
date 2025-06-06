# paymentCardData

**Framework**: ProximityReader  
**Kind**: property

A Base64-encoded string that contains the encrypted payment information to send to your payment provider.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
let paymentCardData: String?
```

## Mentions

- [Adding support for Tap to Pay on iPhone to your app](adding-support-for-tap-to-pay-on-iphone-to-your-app.md)

#### Discussion

This information is present any time the system reads a card, including for purchases, refunds, and card verification.

## See Also

- [let generalCardData: String?](paymentcardreadresult/generalcarddata.md)
  A Base64-encoded string that contains general cardholder and terminal data in tag-length-value (TLV) format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadresult/paymentcarddata)*