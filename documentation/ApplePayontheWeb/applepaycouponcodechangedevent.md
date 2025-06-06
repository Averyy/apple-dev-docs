# ApplePayCouponCodeChangedEvent

**Framework**: Apple Pay on the Web  
**Kind**: class

An event object that contains the coupon code entered by the user.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
interface ApplePayCouponCodeChangedEvent
```

## Mentions

- [Apple Pay on the Web Version 12 Release Notes](apple-pay-on-the-web-version-12-release-notes.md)

## Topics

### Reading the Coupon Code
- [couponCode](applepaycouponcodechangedevent/couponcode.md)
  The updated coupon code from the payment sheet.

## See Also

- [oncouponcodechanged](applepaysession/oncouponcodechanged.md)
  An event handler called by the system when the user enters or updates a coupon code.
- [completeCouponCodeChange](applepaysession/completecouponcodechange.md)
  Completes the entry of a coupon code with an update.
- [ApplePayCouponCodeUpdate](applepaycouponcodeupdate.md)
  A dictionary that contains the updated transaction details for responding to a coupon changed event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaycouponcodechangedevent)*