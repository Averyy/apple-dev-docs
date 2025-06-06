# ApplePayPaymentMethodUpdate

**Framework**: Apple Pay on the Web  
**Kind**: struct

Updated transaction details to provide after the user changes the payment method in the payment sheet.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
dictionary ApplePayPaymentMethodUpdate {
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

If a user changes their payment method on the payment sheet, you respond by updating the payment request details in [`ApplePayPaymentMethodUpdate`](applepaypaymentmethodupdate.md).

You must provide an updated total for the transaction in the `newTotal` line item. You can optionally provide updated line items if the change to the payment method changes the line items.

## Topics

### Updating payment method properties
- [newLineItems](applepaypaymentmethodupdate/newlineitems.md)
  An optional list of updated line items for the payment request that results from the user’s change to the payment method.
- [newTotal](applepaypaymentmethodupdate/newtotal.md)
  The new total that results from the user’s change to the payment method.
- [errors](applepaypaymentmethodupdate/errors.md)
  A list of customized errors you provide that results from the user’s change to the payment method.
- [newShippingMethods](applepaypaymentmethodupdate/newshippingmethods.md)
  The updated list of available shipping methods that results from the user’s change to the payment method.
### Updating automatic reload payments
- [newAutomaticReloadPaymentRequest](applepaypaymentmethodupdate/newautomaticreloadpaymentrequest.md)
  An updated request for an automatic reload payment.
- [ApplePayAutomaticReloadPaymentRequest](applepayautomaticreloadpaymentrequest.md)
  A dictionary that represents a request to set up an automatic reload payment, such as a store card top-up or a prepaid account.
### Updating deferred payments
- [newDeferredPaymentRequest](applepaypaymentmethodupdate/newdeferredpaymentrequest.md)
  An updated request for a deferred payment.
### Updating recurring payments
- [newRecurringPaymentRequest](applepaypaymentmethodupdate/newrecurringpaymentrequest.md)
  An updated request for a recurring payment.
- [ApplePayRecurringPaymentRequest](applepayrecurringpaymentrequest.md)
  A dictionary that represents a request to set up a recurring payment, typically a subscription.
### Updating multitoken or multimerchant payments
- [newMultiTokenContexts](applepaypaymentmethodupdate/newmultitokencontexts.md)
  An array of updated multitoken contexts for a multimerchant payment request.
- [ApplePayPaymentTokenContext](applepaypaymenttokencontext.md)
  A dictionary that defines the context for a single payment token in a payment request for multimerchant payments.

## See Also

- [onpaymentmethodselected](applepaysession/onpaymentmethodselected.md)
  An event handler to call when the user selects a new payment method.
- [completePaymentMethodSelection](applepaysession/completepaymentmethodselection.md)
  Completes the selection of a payment method with an update.
- [ApplePayPaymentMethodSelectedEvent](applepaypaymentmethodselectedevent.md)
  An event object that contains the payment method.
- [ApplePayPaymentMethod](applepaypaymentmethod.md)
  A dictionary that describes an Apple Pay payment method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentmethodupdate)*