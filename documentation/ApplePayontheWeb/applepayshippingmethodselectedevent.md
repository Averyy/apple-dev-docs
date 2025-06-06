# ApplePayShippingMethodSelectedEvent

**Framework**: Apple Pay on the Web  
**Kind**: class

An event object that contains the shipping method.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
interface ApplePayShippingMethodSelectedEvent
```

#### Overview

The event handler [`onshippingmethodselected`](applepaysession/onshippingmethodselected.md) receives this event object when the user selects a shipping method.

## Topics

### Shipping method properties
- [shippingMethod](applepayshippingmethodselectedevent/shippingmethod.md)
  The shipping method selected by the user.

## See Also

- [onshippingmethodselected](applepaysession/onshippingmethodselected.md)
  An event handler to call when the user selects a shipping method.
- [completeShippingMethodSelection](applepaysession/completeshippingmethodselection.md)
  Completes the selection of a shipping method with an update.
- [ApplePayShippingMethodUpdate](applepayshippingmethodupdate.md)
  Updated transaction details that result from a change in shipping method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayshippingmethodselectedevent)*