# completePaymentMethodSelection

**Framework**: Apple Pay on the Web  
**Kind**: method

Completes the selection of a payment method with an update.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
undefined completePaymentMethodSelection(
	ApplePayLineItem newTotal,
	sequence<ApplePayLineItem> newLineItems
);
```

## Mentions

- [Apple Pay on the Web Version 3 Release Notes](apple-pay-on-the-web-version-3-release-notes.md)

#### Discussion

This method must be called by [`onpaymentmethodselected`](applepaysession/onpaymentmethodselected.md) .

The parameter for the Apple Pay JS API version 3 is an [`ApplePayPaymentMethodUpdate`](applepaypaymentmethodupdate.md) instance. Use the [`newLineItems`](applepayshippingmethodupdate/newlineitems.md) only if you have new or updated costs or discounts, otherwise pass an empty array or null. Set the [`newTotal`](applepaypaymentmethodupdate/newtotal.md) argument with the total cost of all the purchased items.

##### Completepaymentmethodselection in Apple Pay Js Api Versions 1 and 2

The parameters for [`completePaymentMethodSelection`](applepaysession/completepaymentmethodselection.md) in API versions 1 and 2 are:

`newTotal`

An [`ApplePayLineItem`](applepaylineitem.md) dictionary representing the total price for the purchase. Set the `label` to the merchant’s name, and the `amount` to the total price. The `amount` must be greater than zero.

`newLineItems`

A sequence of [`ApplePayLineItem`](applepaylineitem.md) dictionaries. Use these line items to represent all other costs or discounts.

Do not use line items to represent the individual items purchased by the user. Instead, combine all the purchases into a single subtotal item. Use additional line items to represent other costs or discounts (tax, shipping, coupons, and so forth.).

## See Also

- [supportsVersion](applepaysession/supportsversion.md)
  Detects whether a web browser supports a particular Apple Pay version.
- [onpaymentmethodselected](applepaysession/onpaymentmethodselected.md)
  An event handler to call when the user selects a new payment method.
- [ApplePayPaymentMethodUpdate](applepaypaymentmethodupdate.md)
  Updated transaction details to provide after the user changes the payment method in the payment sheet.
- [ApplePayPaymentMethodSelectedEvent](applepaypaymentmethodselectedevent.md)
  An event object that contains the payment method.
- [ApplePayPaymentMethod](applepaypaymentmethod.md)
  A dictionary that describes an Apple Pay payment method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaysession/completepaymentmethodselection)*