# oncouponcodechanged

**Framework**: Apple Pay on the Web  
**Kind**: property  
**Role**: Instance Property

An event handler called by the system when the user enters or updates a coupon code.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```
attribute EventHandler oncouponcodechanged;
```

#### Discussion

Set this attribute to a function with one parameter that contains an [`ApplePayCouponCodeChangedEvent`](../applepaycouponcodechangedevent.md). This function processes the coupon code update, and then calls [`completeCouponCodeChange`](./completecouponcodechange.md) with the results.

The code below shows adding a listener for the coupon code changed event to the Apple Pay session:

```javascript
// Add a listener for the couponcodechanged event to the Apple Pay session.
session.addEventListener("couponcodechanged", function(event) {
    var newCode = event.couponCode;

    // Process the coupon code.
    ...

    // Call the Apple Pay session completion method for this event.
    session.completeCouponCodeChange({
        // Update the payment request with any changed information.
        newTotal: ...
    });
});
```

> **Note**:  Call `completeCouponCodeChange` within `30` seconds to prevent the system ending the payment request.

## See Also

### Handling coupons
- [completeCouponCodeChange](./completecouponcodechange.md)
  Completes the entry of a coupon code with an update.
- [ApplePayCouponCodeChangedEvent](../applepaycouponcodechangedevent.md)
  An event object that contains the coupon code entered by the user.
- [ApplePayCouponCodeUpdate](../applepaycouponcodeupdate.md)
  A dictionary that contains the updated transaction details for responding to a coupon changed event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaysession/oncouponcodechanged)*