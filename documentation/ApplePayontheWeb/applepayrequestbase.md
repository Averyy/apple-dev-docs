# ApplePayRequestBase

**Framework**: Apple Pay on the Web  
**Kind**: struct

A dictionary that defines basic payment and contact information that the Apple Pay payment request object uses for the W3C Payment Request API.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
dictionary ApplePayRequestBase {
	sequence <ApplePayFeature> features;
	required sequence <ApplePayMerchantCapability> merchantCapabilities;
	required sequence <DOMString> supportedNetworks;
	required DOMString countryCode;
	sequence <ApplePayContactField> requiredBillingContactFields;
	ApplePayPaymentContact billingContact;
	sequence <ApplePayContactField> requiredShippingContactFields;
	ApplePayPaymentContact shippingContact;
	DOMString applicationData;
	sequence <DOMString> supportedCountries;
	ApplePayInstallmentConfiguration installmentConfiguration;
	boolean supportsCouponCode;
	DOMString couponCode;
	ApplePayShippingContactEditingMode shippingContactEditingMode;
	ApplePayLaterAvailability applePayLaterAvailability;
};
```

## Topics

### Setting the transaction information
- [countryCode](applepayrequestbase/countrycode.md)
  The merchant’s two-letter ISO-3166 country code.
- [merchantCapabilities](applepayrequestbase/merchantcapabilities.md)
  An array of the payment capabilities that the merchant supports, such as credit or debit card payments.
- [supportedNetworks](applepayrequestbase/supportednetworks.md)
  The payment networks the merchant provides to their customers.
- [supportedCountries](applepayrequestbase/supportedcountries.md)
  A list of two-letter country codes for limiting payment to credit cards from specific countries or regions.
### Managing coupon codes
- [couponCode](applepayrequestbase/couponcode.md)
  The initial coupon code for the payment request.
- [supportsCouponCode](applepayrequestbase/supportscouponcode.md)
  A Boolean value that determines whether the payment sheet displays the coupon code field.
### Billing and shipping information
- [requiredBillingContactFields](applepayrequestbase/requiredbillingcontactfields.md)
  A list of fields use for processing the transaction, including the name, address, and other information associated with the payment method.
- [requiredShippingContactFields](applepayrequestbase/requiredshippingcontactfields.md)
  A list of fields used for processing the transaction, including the recipient’s name, mailing address, and other contact details.
### Setting contact information
- [billingContact](applepayrequestbase/billingcontact.md)
  A prepopulated billing address.
- [shippingContact](applepayrequestbase/shippingcontact.md)
  The customer’s address, used for sending products or services for to the person.
- [shippingContactEditingMode](applepayrequestbase/shippingcontacteditingmode.md)
  A value that indicates whether the shipping mode prevents the user from editing the shipping address.
### Adding custom data
- [applicationData](applepayrequestbase/applicationdata.md)
  Application-specific data or state you can add to support your app.
### Adding an installment configuration
- [installmentConfiguration](applepayrequestbase/installmentconfiguration.md)
### Adding features
- [features](applepayrequestbase/features.md)
### Deprecated
- [ApplePayLaterAvailability](applepaylateravailability.md)
  Values you use to enable or disable Apple Pay Later for a specific transaction.
- [applePayLaterAvailability](applepayrequestbase/applepaylateravailability.md)
  A value that indicates whether Apple Pay Later is available for a transaction.

## See Also

- [Setting up the payment request API to accept Apple Pay](setting-up-the-payment-request-api-to-accept-apple-pay.md)
  Support payments using Apple Pay on your website.
- [ApplePayRequest](applepayrequest.md)
  A dictionary that defines the Apple Pay payment request object to use for the W3C Payment Request API.
- [ApplePayModifier](applepaymodifier.md)
  A dictionary that defines the Apple Pay modifiers for a payment type in the W3C Payment Request API.
- [ApplePayPaymentCompleteDetails](applepaypaymentcompletedetails.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayrequestbase)*