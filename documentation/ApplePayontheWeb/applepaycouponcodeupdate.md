# ApplePayCouponCodeUpdate

**Framework**: Apple Pay on the Web  
**Kind**: struct

A dictionary that contains the updated transaction details for responding to a coupon changed event.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
dictionary ApplePayCouponCodeUpdate {
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

- [Apple Pay on the Web Version 12 Release Notes](apple-pay-on-the-web-version-12-release-notes.md)

## Topics

### Setting updated transaction details
- [newLineItems](applepaycouponcodeupdate/newlineitems.md)
  The list of updated line items incorporating the coupon code update.
- [newShippingMethods](applepaycouponcodeupdate/newshippingmethods.md)
  The list of available shipping methods.
- [newTotal](applepaycouponcodeupdate/newtotal.md)
  The updated total resulting from the coupon code update.
- [errors](applepaycouponcodeupdate/errors.md)
  A list of errors resulting from the coupon code update.
### Updating automatic reload payments
- [newAutomaticReloadPaymentRequest](applepaycouponcodeupdate/newautomaticreloadpaymentrequest.md)
  An updated request for an automatic reload payment.
### Updating deferred payments
- [newDeferredPaymentRequest](applepaycouponcodeupdate/newdeferredpaymentrequest.md)
  An updated request for a deferred payment.
### Updating recurring payments
- [newRecurringPaymentRequest](applepaycouponcodeupdate/newrecurringpaymentrequest.md)
  An updated request for a recurring payment.
### Updating multi-token or multi-merchant payments
- [newMultiTokenContexts](applepaycouponcodeupdate/newmultitokencontexts.md)
  An array of updated multitoken contexts for a multimerchant payment request.

## See Also

- [oncouponcodechanged](applepaysession/oncouponcodechanged.md)
  An event handler called by the system when the user enters or updates a coupon code.
- [completeCouponCodeChange](applepaysession/completecouponcodechange.md)
  Completes the entry of a coupon code with an update.
- [ApplePayCouponCodeChangedEvent](applepaycouponcodechangedevent.md)
  An event object that contains the coupon code entered by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaycouponcodeupdate)*