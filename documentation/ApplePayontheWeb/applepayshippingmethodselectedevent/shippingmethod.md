# shippingMethod

**Framework**: Apple Pay on the Web  
**Kind**: property

The shipping method selected by the user.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
readonly attribute ApplePayShippingMethod shippingMethod;
```

#### Discussion

See [`ApplePayShippingMethod`](applepayshippingmethod.md).

This attribute is contained by the [`onshippingmethodselected`](applepaysession/onshippingmethodselected.md) event. Access this attribute using the `event` parameter in the callback function; for example, `var myShippingMethod = event.shippingMethod;`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayshippingmethodselectedevent/shippingmethod)*