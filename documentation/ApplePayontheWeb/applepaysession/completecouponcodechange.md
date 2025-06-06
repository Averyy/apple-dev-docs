# completeCouponCodeChange

**Framework**: Apple Pay on the Web  
**Kind**: method

Completes the entry of a coupon code with an update.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
undefined completeCouponCodeChange(
	ApplePayCouponCodeUpdate update
);
```

## Mentions

- [Apple Pay on the Web Version 12 Release Notes](apple-pay-on-the-web-version-12-release-notes.md)

#### Discussion

This is the method called by [`oncouponcodechanged`](applepaysession/oncouponcodechanged.md) to complete the event.

## See Also

- [oncouponcodechanged](applepaysession/oncouponcodechanged.md)
  An event handler called by the system when the user enters or updates a coupon code.
- [ApplePayCouponCodeChangedEvent](applepaycouponcodechangedevent.md)
  An event object that contains the coupon code entered by the user.
- [ApplePayCouponCodeUpdate](applepaycouponcodeupdate.md)
  A dictionary that contains the updated transaction details for responding to a coupon changed event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaysession/completecouponcodechange)*