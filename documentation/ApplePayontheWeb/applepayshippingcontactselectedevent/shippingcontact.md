# shippingContact

**Framework**: Apple Pay on the Web  
**Kind**: property

The shipping address selected by the user.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
readonly attribute ApplePayPaymentContact shippingContact;
```

#### Discussion

This attribute is contained by the [`onshippingcontactselected`](applepaysession/onshippingcontactselected.md) event. Access this attribute using the event parameter in the callback function; for example, `var myShippingContact = event.shippingContact;`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayshippingcontactselectedevent/shippingcontact)*