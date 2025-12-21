# ApplePayPaymentMethod

**Framework**: Apple Pay on the Web  
**Kind**: struct

A dictionary that describes an Apple Pay payment method.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
dictionary ApplePayPaymentMethod {
	DOMString displayName;
	DOMString network;
	ApplePayPaymentMethodType type;
	ApplePayPaymentPass paymentPass;
	ApplePayPaymentContact billingContact;
};
```

## Mentions

- [Apple Pay on the Web Version 10 Release Notes](apple-pay-on-the-web-version-10-release-notes.md)
- [Setting up the payment request API to accept Apple Pay](setting-up-the-payment-request-api-to-accept-apple-pay.md)

## Topics

### Accessing payment method data
- [displayName](applepaypaymentmethod/displayname.md)
  A string, suitable for display, that describes the card.
- [network](applepaypaymentmethod/network.md)
  A string, suitable for display, that is the name of the payment network backing the card.
- [type](applepaypaymentmethod/type.md)
  A string value representing the card’s type of payment.
- [paymentPass](applepaypaymentmethod/paymentpass.md)
  The payment pass object currently selected to complete the payment.
- [billingContact](applepaypaymentmethod/billingcontact.md)
  The billing contact associated with the card.

## See Also

- [onpaymentmethodselected](applepaysession/onpaymentmethodselected.md)
  An event handler to call when the user selects a new payment method.
- [completePaymentMethodSelection](applepaysession/completepaymentmethodselection.md)
  Completes the selection of a payment method with an update.
- [ApplePayPaymentMethodUpdate](applepaypaymentmethodupdate.md)
  Updated transaction details to provide after the user changes the payment method in the payment sheet.
- [ApplePayPaymentMethodSelectedEvent](applepaypaymentmethodselectedevent.md)
  An event object that contains the payment method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentmethod)*