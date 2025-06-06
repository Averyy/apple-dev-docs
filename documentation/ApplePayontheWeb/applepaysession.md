# ApplePaySession

**Framework**: Apple Pay on the Web  
**Kind**: class

A session object for managing the payment process on the web.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
interface ApplePaySession
```

## Mentions

- [Creating an Apple Pay Session](creating-an-apple-pay-session.md)

#### Overview

[`ApplePaySession`](applepaysession.md) is the entry point for Apple Pay on the web.  All the steps of the payment process for a single transaction occur in a session.

[`ApplePaySession`](applepaysession.md) belongs to the Apple Pay JS API.

## Topics

### Determining support for API and payments
- [supportsVersion](applepaysession/supportsversion.md)
  Detects whether a web browser supports a particular Apple Pay version.
- [applePayCapabilities](applepaysession/applepaycapabilities.md)
  Indicates whether the device supports Apple Pay and whether the person has an active card in Wallet that qualifies for web payments.
- [canMakePayments](applepaysession/canmakepayments.md)
  Indicates whether the device supports Apple Pay.
- [canMakePaymentsWithActiveCard](applepaysession/canmakepaymentswithactivecard.md)
  Indicates whether the device supports Apple Pay and whether the user has an active card in Wallet.
### Creating an Apple Pay session
- [ApplePaySession](applepaysession/applepaysession.md)
  The entry point for Apple Pay on the web.
### Getting merchant validation
- [begin](applepaysession/begin.md)
  Begins the merchant validation process.
- [onvalidatemerchant](applepaysession/onvalidatemerchant.md)
  An event handler the system calls when it displays the payment sheet.
- [completeMerchantValidation](applepaysession/completemerchantvalidation.md)
  Completes the validation for a merchant session.
- [ApplePayValidateMerchantEvent](applepayvalidatemerchantevent.md)
  An event object that contains the validation URL.
### Handling payment method updates
- [onpaymentmethodselected](applepaysession/onpaymentmethodselected.md)
  An event handler to call when the user selects a new payment method.
- [completePaymentMethodSelection](applepaysession/completepaymentmethodselection.md)
  Completes the selection of a payment method with an update.
- [ApplePayPaymentMethodUpdate](applepaypaymentmethodupdate.md)
  Updated transaction details to provide after the user changes the payment method in the payment sheet.
- [ApplePayPaymentMethodSelectedEvent](applepaypaymentmethodselectedevent.md)
  An event object that contains the payment method.
- [ApplePayPaymentMethod](applepaypaymentmethod.md)
  A dictionary that describes an Apple Pay payment method.
### Handling coupons
- [oncouponcodechanged](applepaysession/oncouponcodechanged.md)
  An event handler called by the system when the user enters or updates a coupon code.
- [completeCouponCodeChange](applepaysession/completecouponcodechange.md)
  Completes the entry of a coupon code with an update.
- [ApplePayCouponCodeChangedEvent](applepaycouponcodechangedevent.md)
  An event object that contains the coupon code entered by the user.
- [ApplePayCouponCodeUpdate](applepaycouponcodeupdate.md)
  A dictionary that contains the updated transaction details for responding to a coupon changed event.
### Handling shipping contact updates
- [onshippingcontactselected](applepaysession/onshippingcontactselected.md)
  An event handler to call when the user selects a shipping contact in the payment sheet.
- [completeShippingContactSelection](applepaysession/completeshippingcontactselection.md)
  Completes the selection of a shipping contact with an update.
- [ApplePayShippingContactSelectedEvent](applepayshippingcontactselectedevent.md)
  An event object that contains the shipping address the user selects.
- [ApplePayShippingContactUpdate](applepayshippingcontactupdate.md)
  Updated transaction details that result from a change in shipping contact, including any errors.
### Handling shipping method updates
- [onshippingmethodselected](applepaysession/onshippingmethodselected.md)
  An event handler to call when the user selects a shipping method.
- [completeShippingMethodSelection](applepaysession/completeshippingmethodselection.md)
  Completes the selection of a shipping method with an update.
- [ApplePayShippingMethodSelectedEvent](applepayshippingmethodselectedevent.md)
  An event object that contains the shipping method.
- [ApplePayShippingMethodUpdate](applepayshippingmethodupdate.md)
  Updated transaction details that result from a change in shipping method.
### Handling payment authorization
- [onpaymentauthorized](applepaysession/onpaymentauthorized.md)
  An event handler the system calls when the user has authorized the Apple Pay payment with Touch ID, Face ID, or a passcode.
- [completePayment](applepaysession/completepayment.md)
  Completes the payment authorization with a result.
- [ApplePayPaymentAuthorizedEvent](applepaypaymentauthorizedevent.md)
  An event object that contains the token used to authorize a payment.
- [ApplePayPayment](applepaypayment.md)
  The result of authorizing a payment request that contains payment information.
- [ApplePayPaymentAuthorizationResult](applepaypaymentauthorizationresult.md)
  The result of payment authorization, including status and errors.
### Ending the session
- [oncancel](applepaysession/oncancel.md)
  An event handler that is automatically called when the payment UI is dismissed.
- [abort](applepaysession/abort.md)
  Aborts the current Apple Pay session.
### Displaying an Apple Pay setup button
- [openPaymentSetup](applepaysession/openpaymentsetup.md)
  A method that displays the Set up Apple Pay button.
### Status code constants
- [STATUS_FAILURE](applepaysession/status_failure.md)
  The requested action failed.
- [STATUS_INVALID_BILLING_POSTAL_ADDRESS](applepaysession/status_invalid_billing_postal_address.md)
  The billing address is invalid.
- [STATUS_INVALID_SHIPPING_CONTACT](applepaysession/status_invalid_shipping_contact.md)
  The shipping contact information is invalid.
- [STATUS_INVALID_SHIPPING_POSTAL_ADDRESS](applepaysession/status_invalid_shipping_postal_address.md)
  The shipping address is invalid.
- [STATUS_PIN_INCORRECT](applepaysession/status_pin_incorrect.md)
  The PIN information is not valid.
- [STATUS_PIN_LOCKOUT](applepaysession/status_pin_lockout.md)
  The maximum number of tries for a PIN has been reached and the user has been locked out.
- [STATUS_PIN_REQUIRED](applepaysession/status_pin_required.md)
  The required PIN information was not provided.
- [STATUS_SUCCESS](applepaysession/status_success.md)
  The requested action succeeded.

## See Also

- [Creating an Apple Pay Session](creating-an-apple-pay-session.md)
  Provide a payment request and create the session.
- [Providing Merchant Validation](providing-merchant-validation.md)
  Validate your merchant identity and receive a session object for each payment request.
- [Requesting an Apple Pay payment session](requesting-an-apple-pay-payment-session.md)
  Request a valid session from the Apple Pay server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaysession)*