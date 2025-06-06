# completeShippingMethodSelection

**Framework**: Apple Pay on the Web  
**Kind**: method

Completes the selection of a shipping method with an update.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
undefined completeShippingMethodSelection(
	unsigned short
);
```

## Mentions

- [Apple Pay on the Web Version 3 Release Notes](apple-pay-on-the-web-version-3-release-notes.md)

#### Discussion

This method must be called by [`onshippingmethodselected`](applepaysession/onshippingmethodselected.md).

For Apple Pay JS API version 3, the parameter is an [`ApplePayShippingMethodUpdate`](applepayshippingmethodupdate.md) object.

##### Completeshippingmethodselection in Apple Pay Js Api Version 1 and 2

In Apple Pay JS API version 1 and 2, [`completeShippingMethodSelection`](applepaysession/completeshippingmethodselection.md) has the following parameters:

`status`

The status of the shipping method update. For valid values, see [`Apple Pay Status Codes`](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/apple_pay_status_codes). If status is not [`STATUS_SUCCESS`](applepaysession/status_success.md), pass null for the other parameters.

`newTotal`

An [`ApplePayLineItem`](applepaylineitem.md) dictionary representing the total price for the purchase. Set the label to the merchant’s name, and the amount to the total price. The amount must be greater than zero.

`newLineItems`

A sequence of [`ApplePayLineItem`](applepaylineitem.md) dictionaries. Use [`ApplePayLineItem`](applepaylineitem.md) dictionaries to represent all other costs or discounts.

Do not use line items to represent the individual items purchased by the user. Instead, combine all the purchases into a single subtotal item. Use additional line items to represent other costs or discounts (tax, shipping, coupons, and so forth.).

If you do not have any additional costs or discounts, do not use this argument. Set the `newTotal` argument with the total cost of all the purchased items, and either pass an empty array or null for `newLineItems`.

## See Also

- [supportsVersion](applepaysession/supportsversion.md)
  Detects whether a web browser supports a particular Apple Pay version.
- [onshippingmethodselected](applepaysession/onshippingmethodselected.md)
  An event handler to call when the user selects a shipping method.
- [ApplePayShippingMethodSelectedEvent](applepayshippingmethodselectedevent.md)
  An event object that contains the shipping method.
- [ApplePayShippingMethodUpdate](applepayshippingmethodupdate.md)
  Updated transaction details that result from a change in shipping method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaysession/completeshippingmethodselection)*