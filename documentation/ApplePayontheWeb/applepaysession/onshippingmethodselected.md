# onshippingmethodselected

**Framework**: Apple Pay on the Web  
**Kind**: property

An event handler to call when the user selects a shipping method.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
attribute EventHandler onshippingmethodselected;
```

#### Discussion

This attribute must be set to a function that accepts an `events` argument; for example, `session.onshippingmethodselected = function(event) {}`.

The event parameter contains the [`shippingMethod`](applepayshippingmethodselectedevent/shippingmethod.md) attribute.

The [`onshippingmethodselected`](applepaysession/onshippingmethodselected.md) function must respond by calling [`completeShippingMethodSelection`](applepaysession/completeshippingmethodselection.md) before the 30 second timeout, after which a message appears stating that the payment could not be completed.

## See Also

- [completeShippingMethodSelection](applepaysession/completeshippingmethodselection.md)
  Completes the selection of a shipping method with an update.
- [ApplePayShippingMethodSelectedEvent](applepayshippingmethodselectedevent.md)
  An event object that contains the shipping method.
- [ApplePayShippingMethodUpdate](applepayshippingmethodupdate.md)
  Updated transaction details that result from a change in shipping method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaysession/onshippingmethodselected)*