# ApplePayPayment

**Framework**: Apple Pay on the Web  
**Kind**: struct

The result of authorizing a payment request that contains payment information.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
dictionary ApplePayPayment {
	required ApplePayPaymentToken token;
	ApplePayPaymentContact billingContact;
	ApplePayPaymentContact shippingContact;
};
```

## Mentions

- [Setting up the payment request API to accept Apple Pay](setting-up-the-payment-request-api-to-accept-apple-pay.md)

#### Overview

Data in [`ApplePayPaymentToken`](applepaypaymenttoken.md) is encrypted. Billing and shipping contact data are not encrypted.

## Topics

### Payment token
- [token](applepaypayment/token.md)
  The encrypted information for an authorized payment.
- [ApplePayPaymentToken](applepaypaymenttoken.md)
  An object that contains the user’s payment credentials.
- [ApplePayPaymentMethod](applepaypaymentmethod.md)
  A dictionary that describes an Apple Pay payment method.
- [ApplePayPaymentMethodType](applepaypaymentmethodtype.md)
  A string that represents the type of the payment method.
- [ApplePayPaymentPass](applepaypaymentpass.md)
  A provisioned payment card for Apple Pay payments.
### Billing and shipping contacts
- [shippingContact](applepaypayment/shippingcontact.md)
  The shipping contact selected by the user for this transaction.
- [billingContact](applepaypayment/billingcontact.md)
  The billing contact selected by the user for this transaction.
- [ApplePayPaymentContact](applepaypaymentcontact.md)
  Contact information fields to use for billing and shipping contact information.

## See Also

- [onpaymentauthorized](applepaysession/onpaymentauthorized.md)
  An event handler the system calls when the user has authorized the Apple Pay payment with Touch ID, Face ID, or a passcode.
- [completePayment](applepaysession/completepayment.md)
  Completes the payment authorization with a result.
- [ApplePayPaymentAuthorizedEvent](applepaypaymentauthorizedevent.md)
  An event object that contains the token used to authorize a payment.
- [ApplePayPaymentAuthorizationResult](applepaypaymentauthorizationresult.md)
  The result of payment authorization, including status and errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypayment)*