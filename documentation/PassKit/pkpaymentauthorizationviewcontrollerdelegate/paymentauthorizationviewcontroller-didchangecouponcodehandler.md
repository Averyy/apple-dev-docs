# paymentAuthorizationViewController(_:didChangeCouponCode:handler:)

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: method

Tells the delegate that the user entered or updated a coupon code.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
optional func paymentAuthorizationViewController(_ controller: PKPaymentAuthorizationViewController, didChangeCouponCode couponCode: String) async -> PKPaymentRequestCouponCodeUpdate
```

## Parameters

- `controller`: The payment authorization view controller.
- `couponCode`: The coupon code.
- `completion`: The completion handler to call with the updated payment summary items and shipping methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentauthorizationviewcontrollerdelegate/paymentauthorizationviewcontroller(_:didchangecouponcode:handler:))*