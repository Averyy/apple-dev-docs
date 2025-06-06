# completeShippingContactSelection

**Framework**: Apple Pay on the Web  
**Kind**: method

Completes the selection of a shipping contact with an update.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
undefined completeShippingContactSelection(
	unsigned short,
	ApplePayLineItem newTotal,
	sequence<ApplePayLineItem> newLineItems
);
```

## Mentions

- [Apple Pay on the Web Version 3 Release Notes](apple-pay-on-the-web-version-3-release-notes.md)

#### Discussion

This method must be called by [`onshippingcontactselected`](applepaysession/onshippingcontactselected.md).

In Apple Pay JS API version 3, the parameter is an [`ApplePayShippingContactUpdate`](applepayshippingcontactupdate.md).

##### Completeshippingcontactselection in Apple Pay Js Version 1 and 2

In version 1 and 2 of the Apple Pay JS API, [`completeShippingContactSelection`](applepaysession/completeshippingcontactselection.md) has the following parameters:

| status | The status of the shipping contact update. For valid values, see [`Apple Pay Status Codes`](https://developer.apple.com/documentation/apple_pay_on_the_web/apple_pay_js_api/apple_pay_status_codes). |
| --- | --- |
| newShippingMethods | A sequence of [`ApplePayShippingMethod`](applepayshippingmethod.md) dictionaries that represents shipping costs (if any). |
| newTotal | An [`ApplePayLineItem`](applepaylineitem.md) dictionary representing the total price for the purchase. Set the [`label`](applepaylineitem/label.md) to the merchant’s name, and the [`amount`](applepaylineitem/amount.md) to the total price. The amount must be greater than zero. |
| newLineItems | A sequence of [`ApplePayLineItem`](applepaylineitem.md) dictionaries. Use [`ApplePayLineItem`](applepaylineitem.md) dictionaries to represent all other costs or discounts. Do not use line items to represent the individual items purchased by the user. Instead, combine all the purchases into a single subtotal item. Use additional line items to represent other costs or discounts (tax, shipping, coupons, and so forth.). If you do not have any additional costs or discounts, do not use this argument. Set the [`newTotal`](applepaypaymentmethodupdate/newtotal.md) argument with the total cost of all the purchased items, and either pass an empty array or null for [`newLineItems`](applepayshippingcontactupdate/newlineitems.md). |

## See Also

- [supportsVersion](applepaysession/supportsversion.md)
  Detects whether a web browser supports a particular Apple Pay version.
- [onshippingcontactselected](applepaysession/onshippingcontactselected.md)
  An event handler to call when the user selects a shipping contact in the payment sheet.
- [ApplePayShippingContactSelectedEvent](applepayshippingcontactselectedevent.md)
  An event object that contains the shipping address the user selects.
- [ApplePayShippingContactUpdate](applepayshippingcontactupdate.md)
  Updated transaction details that result from a change in shipping contact, including any errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaysession/completeshippingcontactselection)*