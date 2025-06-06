# applicationData

**Framework**: Apple Pay on the Web  
**Kind**: property

Application-specific data or state you can add to support your app.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
DOMString applicationData;
```

#### Discussion

Use this property for additional data as may be appropriate for your app—for example, a shopping cart identifier or an order number.

The signed payment data (the [`paymentData`](https://developer.apple.com/documentation/PassKit/PKPaymentToken/paymentData) property of [`PKPaymentToken`](https://developer.apple.com/documentation/PassKit/PKPaymentToken)) includes a hash of this data. You’re responsible for sending the full application data to your server, if needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayrequestbase/applicationdata)*