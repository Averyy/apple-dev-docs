# ApplePayPaymentRequest

**Framework**: Apple Pay on the Web  
**Kind**: struct

A request for payment, which includes information about payment-processing capabilities, the payment amount, and shipping information.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
dictionary ApplePayPaymentRequest {
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
	required ApplePayLineItem total;
	sequence <ApplePayLineItem> lineItems;
	required DOMString currencyCode;
	ApplePayShippingType shippingType;
	sequence <ApplePayShippingMethod> shippingMethods;
	sequence <ApplePayPaymentTokenContext> multiTokenContexts;
	ApplePayAutomaticReloadPaymentRequest automaticReloadPaymentRequest;
	ApplePayRecurringPaymentRequest recurringPaymentRequest;
	ApplePayDeferredPaymentRequest deferredPaymentRequest;
};
```

## Mentions

- [Apple Pay on the Web Version 12 Release Notes](apple-pay-on-the-web-version-12-release-notes.md)
- [Apple Pay on the Web Version 14 Release Notes](apple-pay-on-the-web-version-14-release-notes.md)
- [Apple Pay on the Web Version 3 Release Notes](apple-pay-on-the-web-version-3-release-notes.md)
- [Apple Pay on the Web Version 4 Release Notes](apple-pay-on-the-web-version-4-release-notes.md)
- [Creating an Apple Pay Session](creating-an-apple-pay-session.md)

#### Overview

Use an [`ApplePayPaymentRequest`](applepaypaymentrequest.md) dictionary to represent a merchant request for payment for goods or services. Your website creates a payment request as soon as the user taps the Apple Pay button to make a purchase.

A payment request contains information that describes the purchase, such as the merchant information, supported payment networks, and the line items, including the total, the currency code, the billing and shipping contact, and more.

A typical payment request is for a one-time payment. To support different types of payment requests, provide one of the following options in the payment request:

- A [`recurringPaymentRequest`](applepaypaymentrequest/recurringpaymentrequest.md) object to request a recurring payment. Recurring payments, such as subscriptions, can feature different payment intervals (for example, annually or monthly), and either regular or trial billing cycles.
- An [`automaticReloadPaymentRequest`](applepaypaymentrequest/automaticreloadpaymentrequest.md) object to set up automatic reload payments. Automatic reload payments, such as store card top-ups, feature a balance threshold and a reload amount. The card automatically reloads with the reload amount when the account drops below the balance threshold.
- Use the [`deferredPaymentRequest`](applepaypaymentrequest/deferredpaymentrequest.md) property to set up a deferred payment request using the [`ApplePayDeferredPaymentRequest`](applepaydeferredpaymentrequest.md) class. Deferred payments include purchases, such as hotel bookings or pre-orders, where the card renders payment at a later date upon the receipt of goods or delivery of services.
- Use the [`applePayLaterAvailability`](applepayrequestbase/applepaylateravailability.md) property to indicate whether this payment request is eligible for Apple Pay Later. You can indicate that Apple Pay Later is unavailable for certain kinds of transactions, including subscriptions, items that require recurring payments or prohibited items, such as gift cards.
- A [`multiTokenContexts`](applepaypaymentrequest/multitokencontexts.md) sequence to request multiple payment tokens to support multimerchant payments. Set up multitoken transactions to process and display payment requests with multiple merchants on one payment sheet, for example, a booking site where a user pays for a hotel, flight, and car rental from different merchants.

> **Note**:  You can set only one of these optional payment request type properties on a payment request object.

For recurring payments and automatic reload payments, you can optionally set up merchant token life-cycle notifications for the request. For more information, see [`Apple Pay Merchant Token Management API`](https://developer.apple.com/documentation/MerchantTokenNotificationServices).

## Topics

### Setting the total and summary line items
- [total](applepaypaymentrequest/total.md)
  A line item that represents the total for the payment.
- [lineItems](applepaypaymentrequest/lineitems.md)
  A set of line items that explain recurring payments and additional charges and discounts.
- [ApplePayLineItem](applepaylineitem.md)
  A line item in a payment request—for example, total, tax, discount, or grand total.
- [ApplePayLineItemType](applepaylineitemtype.md)
  A type that indicates whether a line item is final or pending.
### Requesting recurring payments
- [recurringPaymentRequest](applepaypaymentrequest/recurringpaymentrequest.md)
  A property that requests a recurring payment, typically a subscription.
- [ApplePayRecurringPaymentRequest](applepayrecurringpaymentrequest.md)
  A dictionary that represents a request to set up a recurring payment, typically a subscription.
### Requesting automatic reload payments
- [automaticReloadPaymentRequest](applepaypaymentrequest/automaticreloadpaymentrequest.md)
  A property that requests an automatic reload payment, such as a store card top-up.
- [ApplePayAutomaticReloadPaymentRequest](applepayautomaticreloadpaymentrequest.md)
  A dictionary that represents a request to set up an automatic reload payment, such as a store card top-up or a prepaid account.
### Requesting deferred payments
- [deferredPaymentRequest](applepaypaymentrequest/deferredpaymentrequest.md)
  A property that requests a deferred payment, such as a hotel booking or a pre-order.
### Requesting multitoken or multimerchant payments
- [multiTokenContexts](applepaypaymentrequest/multitokencontexts.md)
  An array of payment token contexts that requests multiple payment tokens to support a multimerchant payment.
- [ApplePayPaymentTokenContext](applepaypaymenttokencontext.md)
  A dictionary that defines the context for a single payment token in a payment request for multimerchant payments.
### Working with transaction information
- [countryCode](applepaypaymentrequest/countrycode.md)
  The merchant’s two-letter ISO 3166 country code.
- [currencyCode](applepaypaymentrequest/currencycode.md)
  The three-letter ISO 4217 currency code for the payment.
- [merchantCapabilities](applepaypaymentrequest/merchantcapabilities.md)
  An array of the payment capabilities that the merchant supports, such as credit or debit.
- [shippingMethods](applepaypaymentrequest/shippingmethods.md)
  The list of shipping methods available for a payment request.
- [shippingType](applepaypaymentrequest/shippingtype.md)
  An optional value that indicates how to ship purchased items.
- [supportedCountries](applepaypaymentrequest/supportedcountries.md)
  A list of two-letter country codes for limiting payment to cards from specific countries or regions.
- [supportedNetworks](applepaypaymentrequest/supportednetworks.md)
  The payment networks the merchant supports.
- [ApplePayMerchantCapability](applepaymerchantcapability.md)
  The payment capabilities the merchant supports.
- [ApplePayShippingMethod](applepayshippingmethod.md)
  A dictionary that describes the shipping method for delivering physical goods.
- [ApplePayShippingType](applepayshippingtype.md)
  A type that indicates how to ship purchased items.
### Requesting billing and shipping contact information
- [requiredBillingContactFields](applepaypaymentrequest/requiredbillingcontactfields.md)
  The fields of billing information the user must provide to process the transaction.
- [requiredShippingContactFields](applepaypaymentrequest/requiredshippingcontactfields.md)
  The fields of shipping information the user must provide to fulfill the order.
- [shippingContactEditingMode](applepaypaymentrequest/shippingcontacteditingmode.md)
  A value that indicates whether the shipping mode prevents the user from editing the shipping address.
- [ApplePayContactField](applepaycontactfield.md)
  Field names for requesting contact information in a payment request.
- [ApplePayShippingContactEditingMode](applepayshippingcontacteditingmode.md)
  Values that indicate whether the shipping mode prevents the user from editing fields of the shipping address.
### Providing known contact information
- [billingContact](applepaypaymentrequest/billingcontact.md)
  Billing contact information for the user.
- [shippingContact](applepaypaymentrequest/shippingcontact.md)
  Shipping contact information for the user.
- [ApplePayPaymentContact](applepaypaymentcontact.md)
  Contact information fields to use for billing and shipping contact information.
### Working with coupon codes
- [couponCode](applepaypaymentrequest/couponcode.md)
  The initial coupon code for the payment request.
- [supportsCouponCode](applepaypaymentrequest/supportscouponcode.md)
  A Boolean value that determines whether the payment sheet displays the coupon code field.
### Adding custom data
- [applicationData](applepaypaymentrequest/applicationdata.md)
  A Base64-encoded string for application-specific data.

## See Also

- [ApplePayDeferredPaymentRequest](applepaydeferredpaymentrequest.md)
  A dictionary that represents a request to set up a deferred payment, such as a hotel booking or a pre-order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepaypaymentrequest)*