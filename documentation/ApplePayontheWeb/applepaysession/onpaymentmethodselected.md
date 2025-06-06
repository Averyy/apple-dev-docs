# onpaymentmethodselected

**Framework**: Apple Pay on the Web  
**Kind**: property

An event handler to call when the user selects a new payment method.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
attribute EventHandler onpaymentmethodselected;
```

#### Discussion

This attribute must be set to a function that accepts an `events` argument; for example, `session.onpaymentmethodselected = function(event) {}`.

The event parameter contains the [`paymentMethod`](applepaypaymentmethodselectedevent/paymentmethod.md) attribute. Access it like this:

`var myPaymentMethod = event.paymentMethod;`

The [`onpaymentmethodselected`](applepaysession/onpaymentmethodselected.md) function must respond by calling [`completePaymentMethodSelection`](applepaysession/completepaymentmethodselection.md) before the 30 second timeout, after which a message appears stating that the payment could not be completed.

## See Also

- [completePaymentMethodSelection](applepaysession/completepaymentmethodselection.md)
  Completes the selection of a payment method with an update.
- [ApplePayPaymentMethodUpdate](applepaypaymentmethodupdate.md)
  Updated transaction details to provide after the user changes the payment method in the payment sheet.
- [ApplePayPaymentMethodSelectedEvent](applepaypaymentmethodselectedevent.md)
  An event object that contains the payment method.
- [ApplePayPaymentMethod](applepaypaymentmethod.md)
  A dictionary that describes an Apple Pay payment method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaysession/onpaymentmethodselected)*