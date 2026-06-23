# requestPayment(for:using:delegate:)

**Framework**: ProximityReader  
**Kind**: method

Opens a form so a customer can select a payment option.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final func requestPayment(for shoppingCartToken: CustomerEngagement.ShoppingCartToken, using paymentRequest: PKPaymentRequest, delegate: any PKPaymentAuthorizationControllerDelegate) async throws -> Bool
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/customerengagementsession/requestpayment(for:using:delegate:))*