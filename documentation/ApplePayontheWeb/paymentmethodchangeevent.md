# PaymentMethodChangeEvent

**Framework**: Apple Pay on the Web  
**Kind**: class

The Apple Pay extensions to the Payment Request payment change event.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
interface PaymentMethodChangeEvent
```

## Mentions

- [Setting up the payment request API to accept Apple Pay](setting-up-the-payment-request-api-to-accept-apple-pay.md)
- [Apple Pay on the Web Version 12 Release Notes](apple-pay-on-the-web-version-12-release-notes.md)

#### Overview

The Payment Request API sends a [`PaymentMethodChangeEvent`](paymentmethodchangeevent.md) when the user updates transaction information. For more information on [`PaymentMethodChangeEvent`](paymentmethodchangeevent.md), see the [`W3C Payment Request API`](https://developer.apple.comhttps://www.w3.org/TR/payment-request/#paymentmethodchangeevent-interface).

##### Apple Pay Events

Custom Apple Pay events include information in the [`methodDetails`](paymentmethodchangeevent/methoddetails.md) attribute of the change event:

## Topics

### Change Information
- [methodName](paymentmethodchangeevent/methodname.md)
  The identifier for the payment method to use for the transaction.
- [methodDetails](paymentmethodchangeevent/methoddetails.md)
  A dictionary that contains the details of the change.

## See Also

- [ApplePayPaymentMethod](applepaypaymentmethod.md)
  A dictionary that describes an Apple Pay payment method.
- [ApplePayCouponCodeDetails](applepaycouponcodedetails.md)
  A dictionary that contains the updated coupon code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/paymentmethodchangeevent)*