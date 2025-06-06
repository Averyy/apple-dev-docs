# ApplePayShippingContactUpdate

**Framework**: Apple Pay on the Web  
**Kind**: struct

Updated transaction details that result from a change in shipping contact, including any errors.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
dictionary ApplePayShippingContactUpdate {
	required ApplePayLineItem newTotal;
	sequence <ApplePayLineItem> newLineItems;
	sequence <ApplePayPaymentTokenContext> newMultiTokenContexts;
	ApplePayAutomaticReloadPaymentRequest newAutomaticReloadPaymentRequest;
	ApplePayRecurringPaymentRequest newRecurringPaymentRequest;
	ApplePayDeferredPaymentRequest newDeferredPaymentRequest;
	sequence <ApplePayError> errors;
	sequence <ApplePayShippingMethod> newShippingMethods;
};
```

## Mentions

- [Apple Pay on the Web Version 3 Release Notes](apple-pay-on-the-web-version-3-release-notes.md)

#### Overview

You must provide an updated total after shipping contact information changes. You can optionally provide a list of errors, updated shipping methods, or updated line items.

The system assumes the shipping contact update is successful if you don’t provide any `errors` in the [`ApplePayShippingContactUpdate`](applepayshippingcontactupdate.md).

## Topics

### Updating shipping contact properties
- [errors](applepayshippingcontactupdate/errors.md)
  A list of custom errors to display on the payment sheet.
- [newLineItems](applepayshippingcontactupdate/newlineitems.md)
  An optional list of updated line items.
- [newShippingMethods](applepayshippingcontactupdate/newshippingmethods.md)
  A list of shipping methods that are available to the updated shipping contact.
- [newTotal](applepayshippingcontactupdate/newtotal.md)
  The new total that results from a change in the shipping contact.
### Updating recurrring payments
- [newRecurringPaymentRequest](applepayshippingcontactupdate/newrecurringpaymentrequest.md)
  An updated request for a recurring payment.
- [ApplePayRecurringPaymentRequest](applepayrecurringpaymentrequest.md)
  A dictionary that represents a request to set up a recurring payment, typically a subscription.
### Updating deferred payments
- [newDeferredPaymentRequest](applepayshippingcontactupdate/newdeferredpaymentrequest.md)
  An updated request for a deferred payment.
### Updating automatic reload payments
- [newAutomaticReloadPaymentRequest](applepayshippingcontactupdate/newautomaticreloadpaymentrequest.md)
  An updated request for an automatic reload payment.
- [ApplePayAutomaticReloadPaymentRequest](applepayautomaticreloadpaymentrequest.md)
  A dictionary that represents a request to set up an automatic reload payment, such as a store card top-up or a prepaid account.
### Updating multitoken or multimerchant payments
- [newMultiTokenContexts](applepayshippingcontactupdate/newmultitokencontexts.md)
  An array of updated multitoken contexts for a multimerchant payment request.
- [ApplePayPaymentTokenContext](applepaypaymenttokencontext.md)
  A dictionary that defines the context for a single payment token in a payment request for multimerchant payments.

## See Also

- [onshippingcontactselected](applepaysession/onshippingcontactselected.md)
  An event handler to call when the user selects a shipping contact in the payment sheet.
- [completeShippingContactSelection](applepaysession/completeshippingcontactselection.md)
  Completes the selection of a shipping contact with an update.
- [ApplePayShippingContactSelectedEvent](applepayshippingcontactselectedevent.md)
  An event object that contains the shipping address the user selects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayshippingcontactupdate)*