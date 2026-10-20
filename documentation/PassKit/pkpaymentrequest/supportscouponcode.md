# supportsCouponCode

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the payment sheet displays the coupon code field.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var supportsCouponCode: Bool { get set }
```

```objc
@property (nonatomic, assign) BOOL supportsCouponCode;
```

#### Discussion

Set the value to `true` to display the coupon code field.

## See Also

### Working with coupon codes
- [var couponCode: String?](./couponcode.md)
  The initial coupon code for the payment request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/supportscouponcode)*