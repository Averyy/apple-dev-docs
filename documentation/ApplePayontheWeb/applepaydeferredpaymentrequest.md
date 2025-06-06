# ApplePayDeferredPaymentRequest

**Framework**: Apple Pay on the Web  
**Kind**: struct

A dictionary that represents a request to set up a deferred payment, such as a hotel booking or a pre-order.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
dictionary ApplePayDeferredPaymentRequest {
	DOMString billingAgreement;
	required ApplePayLineItem deferredBilling;
	Date freeCancellationDate;
	DOMString freeCancellationDateTimeZone;
	required DOMString managementURL;
	required DOMString paymentDescription;
	DOMString tokenNotificationURL;
};
```

## Topics

### Describing a deferred payment
- [billingAgreement](applepaydeferredpaymentrequest/billingagreement.md)
  The localized billing agreement the framework displays to the user prior to payment authorization.
- [paymentDescription](applepaydeferredpaymentrequest/paymentdescription.md)
  A description of the deferred payment.
- [freeCancellationDate](applepaydeferredpaymentrequest/freecancellationdate.md)
  The time zone at the destination location of the payment.
- [freeCancellationDateTimeZone](applepaydeferredpaymentrequest/freecancellationdatetimezone.md)
  The time zone at the destination location of the payment.
### Setting payment summary items
- [deferredBilling](applepaydeferredpaymentrequest/deferredbilling.md)
  A dictionary that contains details about the deferred payment.
### Managing payment tokens
- [managementURL](applepaydeferredpaymentrequest/managementurl.md)
  A URL that links to a page on your web site where the user can manage the payment method for the deferred payment, including deleting it.
- [tokenNotificationURL](applepaydeferredpaymentrequest/tokennotificationurl.md)
  A URL to receive life-cycle notifications for the merchant-specific payment token the system issues for the request, if applicable.

## See Also

- [ApplePayPaymentRequest](applepaypaymentrequest.md)
  A request for payment, which includes information about payment-processing capabilities, the payment amount, and shipping information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaydeferredpaymentrequest)*