# ApplePayRequest

**Framework**: Apple Pay on the Web  
**Kind**: struct

A dictionary that defines the Apple Pay payment request object to use for the W3C Payment Request API.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
dictionary ApplePayRequest {
	required long version;
	required DOMString merchantIdentifier;
	required sequence <ApplePayMerchantCapability> merchantCapabilities;
	required sequence <DOMString> supportedNetworks;
	required DOMString countryCode;
	sequence <ApplePayContactField> requiredBillingContactFields;
	ApplePayPaymentContact billingContact;
	sequence <ApplePayContactField> requiredShippingContactFields;
	ApplePayPaymentContact shippingContact;
	DOMString applicationData;
	sequence <DOMString> supportedCountries;
	boolean supportsCouponCode;
	DOMString couponCode;
	ApplePayShippingContactEditingMode shippingContactEditingMode;
};
```

## Mentions

- [Apple Pay on the Web Version 12 Release Notes](apple-pay-on-the-web-version-12-release-notes.md)
- [Setting up the payment request API to accept Apple Pay](setting-up-the-payment-request-api-to-accept-apple-pay.md)
- [Apple Pay on the Web Version 6 Release Notes](apple-pay-on-the-web-version-6-release-notes.md)

#### Overview

The dictionary contains the supported Apple Pay properties for the `data` object of the `PaymentMethodData` dictionary in the Payment Request API.

For more information on `PaymentMethodData`, see the [`W3C Payment Request API specification`](https://developer.apple.comhttps://www.w3.org/TR/payment-request/#paymentmethoddata-dictionary).

## Topics

### Identifier and version information
- [merchantIdentifier](applepayrequest/merchantidentifier.md)
  The merchant identifier you registered with Apple for use with Apple Pay.
- [version](applepayrequest/version.md)
  The Apple Pay version supported on your website.
### Transaction information
- [countryCode](applepayrequest/countrycode.md)
  The merchant’s two-letter ISO 3166 country code.
- [merchantCapabilities](applepayrequest/merchantcapabilities.md)
  An array of the payment capabilities the merchant supports, such as credit or debit.
- [supportedNetworks](applepayrequest/supportednetworks.md)
  The payment networks the merchant supports.
- [supportedCountries](applepayrequest/supportedcountries.md)
  A list of two-letter country codes for limiting payment to cards from specific countries or regions.
### Setting the Apple Pay Later mode
- [applePayLaterAvailability](applepayrequestbase/applepaylateravailability.md)
  A value that indicates whether Apple Pay Later is available for a transaction.
- [ApplePayLaterAvailability](applepaylateravailability.md)
  Values you use to enable or disable Apple Pay Later for a specific transaction.
### Coupon codes
- [couponCode](applepayrequest/couponcode.md)
  The initial coupon code for the payment request.
- [supportsCouponCode](applepayrequest/supportscouponcode.md)
  A Boolean value that determines whether the payment sheet displays the coupon code field.
### Requesting billing and shipping contact information
- [requiredBillingContactFields](applepayrequest/requiredbillingcontactfields.md)
  The fields of billing information the user must provide to process the transaction.
- [requiredShippingContactFields](applepayrequest/requiredshippingcontactfields.md)
  The fields of shipping information the user must provide to fulfill the order.
### Known contact information
- [billingContact](applepayrequest/billingcontact.md)
  The customer’s billing contact information.
- [shippingContact](applepayrequest/shippingcontact.md)
  The customer’s shipping contact information.
- [shippingContactEditingMode](applepayrequest/shippingcontacteditingmode.md)
  A value that indicates if the shipping mode prevents the user editing the shipping address.
- [ApplePayPaymentContact](applepaypaymentcontact.md)
  Contact information fields to use for billing and shipping contact information.
- [ApplePayShippingContactEditingMode](applepayshippingcontacteditingmode.md)
  Values that indicate whether the shipping mode prevents the user from editing fields of the shipping address.
### Respond to payment request change events
- [PaymentMethodChangeEvent](paymentmethodchangeevent.md)
  The Apple Pay extensions to the Payment Request payment change event.
- [ApplePayCouponCodeDetails](applepaycouponcodedetails.md)
  A dictionary that contains the updated coupon code.
### Custom data
- [applicationData](applepayrequest/applicationdata.md)
  A Base64-encoded string used to contain your application-specific data.

## See Also

- [Setting up the payment request API to accept Apple Pay](setting-up-the-payment-request-api-to-accept-apple-pay.md)
  Support payments using Apple Pay on your website.
- [ApplePayRequestBase](applepayrequestbase.md)
  A dictionary that defines basic payment and contact information that the Apple Pay payment request object uses for the W3C Payment Request API.
- [ApplePayModifier](applepaymodifier.md)
  A dictionary that defines the Apple Pay modifiers for a payment type in the W3C Payment Request API.
- [ApplePayPaymentCompleteDetails](applepaypaymentcompletedetails.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayrequest)*