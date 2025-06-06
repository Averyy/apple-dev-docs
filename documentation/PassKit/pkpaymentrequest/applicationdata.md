# applicationData

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

Application-specific data or state.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var applicationData: Data? { get set }
```

#### Discussion

Use this property for additional data as may be appropriate for your app—for example, a shopping cart identifier or an order number.

A hash of this data is included in the signed payment data (the [`paymentData`](pkpaymenttoken/paymentdata.md) property of [`PKPaymentToken`](pkpaymenttoken.md)). You are responsible for sending the full application data to your server, if needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/applicationdata)*