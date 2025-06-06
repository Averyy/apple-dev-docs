# Apple Pay

**Framework**: PassKit (Apple Pay and Wallet)

Request and process Apple Pay payments in your app.

## Topics

### Apple Pay setup
- [Setting up Apple Pay](setting-up-apple-pay.md)
  Fulfill the requirements to provide Apple Pay as a payment option on your website or in your app.
- [Offering Apple Pay in Your App](offering-apple-pay-in-your-app.md)
  Collect payments with iPhone and Apple Watch using Apple Pay.
- [Complying with regional regulations](complying-with-regional-regulations.md)
  Check regional regulations for possible requirements for your Apple Pay-based implementation.
### Apple Pay availability
- [class PKPaymentAuthorizationController](pkpaymentauthorizationcontroller.md)
  An object that presents a sheet that prompts the user to authorize a payment request.
- [class PKPaymentAuthorizationViewController](pkpaymentauthorizationviewcontroller.md)
  An object that presents a sheet that prompts the user to authorize a payment request.
### Apple Pay buttons
- [class PKPaymentButton](pkpaymentbutton.md)
  An object that displays a button either to trigger payments through Apple Pay or to prompt the user to set up a card.
- [struct PayWithApplePayButton](paywithapplepaybutton.md)
- [struct PayWithApplePayButtonLabel](paywithapplepaybuttonlabel.md)
- [struct PayWithApplePayButtonStyle](paywithapplepaybuttonstyle.md)
### Payment requests
- [class PKPaymentRequest](pkpaymentrequest.md)
  An object that represents a request for payment, including details about payment-processing capabilities, the payment amount, and shipping information.
- [class PKRecurringPaymentRequest](pkrecurringpaymentrequest.md)
  A class that represents a request to set up a recurring payment, typically a subscription.
- [class PKAutomaticReloadPaymentRequest](pkautomaticreloadpaymentrequest.md)
  A class that represents a request to set up an automatic reload payment, such as a store card top-up or a prepaid account.
- [class PKDeferredPaymentRequest](pkdeferredpaymentrequest.md)
  An object that represents a request to set up a deferred payment, such as a hotel booking or a pre-order.
- [class PKPaymentTokenContext](pkpaymenttokencontext.md)
  A class that defines the context for a single payment token in a payment request for multimerchant payments.
### Disbursement requests
- [class PKDisbursementRequest](pkdisbursementrequest.md)
  An object that represents a request to disburse funds from a merchant to an individual.
### Payment sheet interactions and authorization
- [class PKPaymentAuthorizationResult](pkpaymentauthorizationresult.md)
  An object that reports the status code and errors for a payment authorization request.
- [class PKPaymentOrderDetails](pkpaymentorderdetails.md)
  Optional metadata with payment order details for the placed order.
- [class PKPaymentAuthorizationController](pkpaymentauthorizationcontroller.md)
  An object that presents a sheet that prompts the user to authorize a payment request.
- [class PKPaymentAuthorizationViewController](pkpaymentauthorizationviewcontroller.md)
  An object that presents a sheet that prompts the user to authorize a payment request.
- [class PKPayment](pkpayment.md)
  Represents the result of authorizing a payment request and contains payment information, encrypted in the payment token.
### Payment sheet updates
- [class PKPaymentRequestMerchantSessionUpdate](pkpaymentrequestmerchantsessionupdate.md)
  An object that updates a payment request with a merchant validation.
- [class PKPaymentRequestPaymentMethodUpdate](pkpaymentrequestpaymentmethodupdate.md)
  An object that updates the payment request after the payment method changes.
- [class PKPaymentRequestShippingContactUpdate](pkpaymentrequestshippingcontactupdate.md)
  An object that updates the payment request after the shipping contact information changes.
- [class PKPaymentRequestShippingMethodUpdate](pkpaymentrequestshippingmethodupdate.md)
  An object that updates the payment request after the shipping method changed.
- [class PKPaymentRequestCouponCodeUpdate](pkpaymentrequestcouponcodeupdate.md)
  An object that updates the payment request after the coupon code changes.
- [class PKPaymentRequestUpdate](pkpaymentrequestupdate.md)
  The base class for updating the payment request after the user makes changes on the payment sheet.
### QR transaction information
- [class PKPaymentInformationEventExtension](pkpaymentinformationeventextension.md)
  An abstract superclass for an extension to collect payment information and sign transaction data in a QR code purchase.
- [protocol PKPaymentInformationRequestHandling](pkpaymentinformationrequesthandling.md)
### Entitlements
- [Merchant IDs Entitlement](../BundleResources/Entitlements/com.apple.developer.in-app-payments.md)
  A list of merchant IDs your app uses for Apple Pay support.
### Payment token format
- [Payment token format reference](payment-token-format-reference.md)
  Verify an Apple Pay payment token and validate a transaction.
### Errors
- [struct PKDisbursementError](pkdisbursementerror.md)
  A structure that describes errors that can occur while processing the disbursement.
- [struct PKDisbursementErrorKey](pkdisbursementerrorkey.md)
  Values that describe errors that can occur when processing disbursements.
- [struct PKPaymentError](pkpaymenterror.md)
  An error type that you create to indicate problems with address or contact information on an Apple Pay sheet.
- [PKPaymentError.Code](pkpaymenterror/code.md)
  An error code that you provide to indicate problems with address or contact information on an Apple Pay sheet.
- [struct PKPaymentErrorKey](pkpaymenterrorkey.md)
  Additional details about an error on the Apple Pay sheet.
- [PKDisbursementError.Code](pkdisbursementerror/code.md)
  Values that describe errors that can occur while processing the disbursement.
- [let PKPaymentErrorDomain: String](pkpaymenterrordomain.md)
  The error domain for specific errors associated with Apple Pay in-app or web payments.
- [let PKDisbursementErrorDomain: String](pkdisbursementerrordomain.md)
  The error domain to use for errors with in-app disbursements.
### Deprecated
- [var applePayLaterAvailability: PKPaymentRequest.ApplePayLaterAvailability](pkpaymentrequest/applepaylateravailability-3dxrt.md)
  A value that indicates whether Apple Pay Later is available for a transaction.
- [PKPaymentRequest.ApplePayLaterAvailability](pkpaymentrequest/applepaylateravailability-swift.enum.md)
  Values you use to enable or disable Apple Pay Later for a specific transaction.
- [struct PKAddressField](pkaddressfield.md)
  Billing or shipping address fields.
- [enum PKApplePayLaterAvailability](pkapplepaylateravailability.md)
  Values you use to enable or disable Apple Pay Later for a specific transaction.

## See Also

- [Apple Pay Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/ApplePay_Guide/index.html#//apple_ref/doc/uid/TP40014764)
- [iOS Human Interface Guidelines](https://developer.apple.comhttps://developer.apple.com/ios/human-interface-guidelines/)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/apple-pay)*