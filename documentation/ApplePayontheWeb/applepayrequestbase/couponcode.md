# couponCode

**Framework**: Apple Pay on the Web  
**Kind**: property

The initial coupon code for the payment request.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
DOMString couponCode;
```

#### Discussion

Set the value to `nil` or the empty string to indicate that there’s no initial coupon.

> ❗ **Important**:  The system doesn’t send a change event for an initial coupon code. You must apply the code to the initial payment summary items.

 The system doesn’t send a change event for an initial coupon code. You must apply the code to the initial payment summary items.

## See Also

- [supportsCouponCode](applepayrequestbase/supportscouponcode.md)
  A Boolean value that determines whether the payment sheet displays the coupon code field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayrequestbase/couponcode)*