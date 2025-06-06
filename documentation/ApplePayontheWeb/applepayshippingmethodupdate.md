# ApplePayShippingMethodUpdate

**Framework**: Apple Pay on the Web  
**Kind**: struct

Updated transaction details that result from a change in shipping method.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
dictionary ApplePayShippingMethodUpdate {
	required ApplePayLineItem newTotal;
	sequence <ApplePayLineItem> newLineItems;
	sequence <ApplePayPaymentTokenContext> newMultiTokenContexts;
	ApplePayAutomaticReloadPaymentRequest newAutomaticReloadPaymentRequest;
	ApplePayRecurringPaymentRequest newRecurringPaymentRequest;
	ApplePayDeferredPaymentRequest newDeferredPaymentRequest;
	sequence <ApplePayShippingMethod> newShippingMethods;
};
```

## Mentions

- [Apple Pay on the Web Version 3 Release Notes](apple-pay-on-the-web-version-3-release-notes.md)

#### Overview

Provide updated transaction details if the user changes the shipping method in the payment sheet. Recalculate the total for the payment, because it may change as a result of shipping method changes. The [`newTotal`](applepayshippingcontactupdate/newtotal.md) value is required.

## Topics

### Updating shipping method properties
- [newLineItems](applepayshippingmethodupdate/newlineitems.md)
  An optional list of updated line items.
- [newTotal](applepayshippingmethodupdate/newtotal.md)
  The new total that results from a change in the shipping method.
- [newShippingMethods](applepayshippingmethodupdate/newshippingmethods.md)
  An updated list of new shipping methods.
### Updating automatic reload payments
- [newAutomaticReloadPaymentRequest](applepayshippingmethodupdate/newautomaticreloadpaymentrequest.md)
  An updated request for an automatic reload payment.
### Updating multitoken or multimerchant payment
- [newMultiTokenContexts](applepayshippingmethodupdate/newmultitokencontexts.md)
  An array of updated multitoken contexts for a multimerchant payment request.
### Updating recurring payments
- [newRecurringPaymentRequest](applepayshippingmethodupdate/newrecurringpaymentrequest.md)
  An updated request for a recurring payment.
### Updating deferred payments
- [newDeferredPaymentRequest](applepayshippingmethodupdate/newdeferredpaymentrequest.md)
  An updated request for a deferred payment.

## See Also

- [onshippingmethodselected](applepaysession/onshippingmethodselected.md)
  An event handler to call when the user selects a shipping method.
- [completeShippingMethodSelection](applepaysession/completeshippingmethodselection.md)
  Completes the selection of a shipping method with an update.
- [ApplePayShippingMethodSelectedEvent](applepayshippingmethodselectedevent.md)
  An event object that contains the shipping method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayshippingmethodupdate)*