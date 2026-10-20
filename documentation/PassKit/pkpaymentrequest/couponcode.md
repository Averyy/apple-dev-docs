# couponCode

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The initial coupon code for the payment request.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var couponCode: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * couponCode;
```

#### Discussion

Set the value to `nil` or the empty string to indicate that there’s no initial coupon.

> ❗ **Important**:  The system doesn’t send a change event for an initial coupon code. You must apply the code to the initial payment summary items.

## See Also

### Working with coupon codes
- [var supportsCouponCode: Bool](./supportscouponcode.md)
  A Boolean value that determines whether the payment sheet displays the coupon code field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/couponcode)*