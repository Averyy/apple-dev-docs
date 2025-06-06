# ApplePayRecurringPaymentRequest

**Framework**: Apple Pay on the Web  
**Kind**: struct

A dictionary that represents a request to set up a recurring payment, typically a subscription.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
dictionary ApplePayRecurringPaymentRequest {
	required DOMString paymentDescription;
	required ApplePayLineItem regularBilling;
	ApplePayLineItem trialBilling;
	DOMString billingAgreement;
	required DOMString managementURL;
	DOMString tokenNotificationURL;
};
```

#### Overview

> ❗ **Important**:  You must include the [`recurringPaymentRequest`](applepaypaymentrequest/recurringpaymentrequest.md) property in the [`ApplePayPaymentRequest`](applepaypaymentrequest.md) object to specify a request for a recurring payment.

 You must include the [`recurringPaymentRequest`](applepaypaymentrequest/recurringpaymentrequest.md) property in the [`ApplePayPaymentRequest`](applepaypaymentrequest.md) object to specify a request for a recurring payment.

Use an [`ApplePayRecurringPaymentRequest`](applepayrecurringpaymentrequest.md) object to provide the user with payment details and a way to manage payment methods for a recurring payment. You can optionally display a billing agreement and set up merchant token life-cycle notifications for the request.

For more information about the merchant token life-cycle notifications, see [`Apple Pay Merchant Token Management API`](https://developer.apple.com/documentation/MerchantTokenNotificationServices).

## Topics

### Describing the recurring payment
- [paymentDescription](applepayrecurringpaymentrequest/paymentdescription.md)
  A description of the recurring payment that Apple Pay displays to the user in the payment sheet.
- [billingAgreement](applepayrecurringpaymentrequest/billingagreement.md)
  A localized billing agreement that the payment sheet displays to the user before the user authorizes the payment.
### Setting the payment summary items
- [regularBilling](applepayrecurringpaymentrequest/regularbilling.md)
  The regular billing cycle for the recurring payment, including start and end dates, an interval, and an interval count.
- [trialBilling](applepayrecurringpaymentrequest/trialbilling.md)
  The trial billing cycle for the recurring payment.
- [ApplePayLineItem](applepaylineitem.md)
  A line item in a payment request—for example, total, tax, discount, or grand total.
### Receiving payment token notifications
- [tokenNotificationURL](applepayrecurringpaymentrequest/tokennotificationurl.md)
  A URL you provide for receiving life-cycle notifications from the Apple Pay servers about the Apple Pay merchant token for the recurring payment.
### Managing the recurring payment
- [managementURL](applepayrecurringpaymentrequest/managementurl.md)
  A URL to a web page where the user can update or delete the payment method for the recurring payment.

## See Also

- [recurringPaymentRequest](applepaypaymentrequest/recurringpaymentrequest.md)
  A property that requests a recurring payment, typically a subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayrecurringpaymentrequest)*