# PKPaymentRequest

**Framework**: Passkit  
**Kind**: class

An object that represents a request for payment, including details about payment-processing capabilities, the payment amount, and shipping information.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class PKPaymentRequest
```

#### Overview

Use a [`PKPaymentRequest`](pkpaymentrequest.md) object to represent a merchant request for payment for goods or services. Your app creates a payment request as soon as a person taps the Apple Pay button to make a purchase. Tapping the Apple Pay button in your app initiates the payment request process. If your customers need to enter a discount code, choose a shipping method, or any other task, your app needs to ask for that information  they tap the Apple Pay button.

A payment request object contains information that describes the purchase, including information about the merchant, available payment networks, the payment summary, billing and shipping details, coupon codes, custom data, error messages, and more.

A typical payment request is for a one-time payment. To support different types of payment requests, include one of the following options in the payment request object:

| Payment type request | Property to set |
| --- | --- |
| Recurring payments | [`recurringPaymentRequest`](pkpaymentrequest/recurringpaymentrequest.md) |
| Automatic reload payments | [`automaticReloadPaymentRequest`](pkpaymentrequest/automaticreloadpaymentrequest.md) |
| Deferred payments | [`deferredPaymentRequest`](pkpaymentrequest/deferredpaymentrequest.md) |
| Indicating eligibility for Apple Pay Later | [`applePayLaterAvailability`](pkpaymentrequest/applepaylateravailability-3dxrt.md) |
| Multiple payment tokens to support for multimerchant payments | [`multiTokenContexts`](pkpaymentrequest/multitokencontexts.md) |

> **Note**:  You can set only one optional payment request type on a payment request object.

##### Request a Recurring Payment

Use the [`recurringPaymentRequest`](pkpaymentrequest/recurringpaymentrequest.md) property to set up a recurring payment request using the [`PKRecurringPaymentRequest`](pkrecurringpaymentrequest.md) and [`PKRecurringPaymentSummaryItem`](pkrecurringpaymentsummaryitem.md) classes. Recurring payments, such as subscriptions, can feature different payment intervals (for example, annually or monthly) and billing cycles, such as regular or trial.

##### Request an Automatic Reload Payment

Use the [`automaticReloadPaymentRequest`](pkpaymentrequest/automaticreloadpaymentrequest.md) property to set up an automatic reload payment request using the [`PKAutomaticReloadPaymentRequest`](pkautomaticreloadpaymentrequest.md) and [`PKAutomaticReloadPaymentSummaryItem`](pkautomaticreloadpaymentsummaryitem.md) classes. You can set up automatic reload payments, such as store card top-ups, that feature a balance threshold and a reload amount. The card automatically reloads with the reload amount when the account drops below the balance threshold.

##### Request a Deferred Payment

Use the [`deferredPaymentRequest`](pkpaymentrequest/deferredpaymentrequest.md) property to set up a deferred payment request using the [`PKDeferredPaymentRequest`](pkdeferredpaymentrequest.md) class. Deferred payments include purchases, such as hotel bookings or pre-orders, where the card renders payment at a later date upon the receipt of goods or delivery of services.

##### Set the Apple Pay Later Mode

Use the [`applePayLaterAvailability`](pkpaymentrequest/applepaylateravailability-3dxrt.md) property to indicate whether this payment request is eligible for Apple Pay Later. You can indicate that Apple Pay Later is unavailable for certain kinds of transactions, including subscriptions, items that require recurring payments or prohibited items, such as gift cards.

##### Request Multitoken or Multimerchant Payments

Use the [`multiTokenContexts`](pkpaymentrequestupdate/multitokencontexts.md) property to request payment data for multimerchant payments with the [`PKPaymentTokenContext`](pkpaymenttokencontext.md) class. You can set up multitoken transactions to process and display payment requests with multiple merchants on one payment sheet, for example, a booking site where someone pays for a hotel, flight, and car rental from different merchants.

## Topics

### Selecting the payment networks
- [class func availableNetworks() -> [PKPaymentNetwork]](pkpaymentrequest/availablenetworks.md)
  Returns the list of available payment methods that Apple Pay supports.
- [var supportedNetworks: [PKPaymentNetwork]](pkpaymentrequest/supportednetworks.md)
  The payment methods that you support.
- [struct PKPaymentNetwork](pkpaymentnetwork.md)
  A type that represents a payment method.
### Setting merchant information
- [PKPaymentRequest.MerchantCategoryCode](pkpaymentrequest/merchantcategorycode-swift.struct.md)
  An optional four-digit struct, in ISO 18245 format, that represents the type of goods or service the merchant provides for the transaction.
- [var merchantIdentifier: String](pkpaymentrequest/merchantidentifier.md)
  Your merchant identifier.
- [var merchantCapabilities: PKMerchantCapability](pkpaymentrequest/merchantcapabilities.md)
  A bit field of the payment-processing protocols and card types that you support.
- [struct PKMerchantCapability](pkmerchantcapability.md)
  Capabilities for processing payment.
### Setting currency and region information
- [var currencyCode: String](pkpaymentrequest/currencycode.md)
  The three-letter ISO 4217 currency code that determines the currency the payment request uses.
- [var supportedCountries: Set<String>?](pkpaymentrequest/supportedcountries.md)
  A list of ISO 3166 country codes to limit payments to cards from specific countries or regions.
- [var countryCode: String](pkpaymentrequest/countrycode.md)
  The merchant’s two-letter ISO 3166 country code.
### Setting the payment summary items
- [var paymentSummaryItems: [PKPaymentSummaryItem]](pkpaymentrequest/paymentsummaryitems.md)
  An array of payment summary item objects that summarize the amount of the payment.
- [class PKPaymentSummaryItem](pkpaymentsummaryitem.md)
  An object that defines a summary item in a payment request, taxes, discounts, shipping, a grand total, and the like.
- [class PKRecurringPaymentSummaryItem](pkrecurringpaymentsummaryitem.md)
  An object that defines a summary item for a payment that occurs repeatedly at a specified interval, such as a subscription.
- [class PKDeferredPaymentSummaryItem](pkdeferredpaymentsummaryitem.md)
  An object that defines a summary item for a payment that occurs at a later date, such as a pre-order.
### Requesting recurring, automatic, and deferred payments
- [var recurringPaymentRequest: PKRecurringPaymentRequest?](pkpaymentrequest/recurringpaymentrequest.md)
  An optional request to set up a recurring payment, typically a subscription.
- [class PKRecurringPaymentRequest](pkrecurringpaymentrequest.md)
  A class that represents a request to set up a recurring payment, typically a subscription.
- [var automaticReloadPaymentRequest: PKAutomaticReloadPaymentRequest?](pkpaymentrequest/automaticreloadpaymentrequest.md)
  An optional request to set up an automatic reload payment, such as a store card top-up.
- [class PKAutomaticReloadPaymentRequest](pkautomaticreloadpaymentrequest.md)
  A class that represents a request to set up an automatic reload payment, such as a store card top-up or a prepaid account.
- [var deferredPaymentRequest: PKDeferredPaymentRequest?](pkpaymentrequest/deferredpaymentrequest.md)
  A request to set up a deferred payment, such as a hotel booking or a pre-order.
- [class PKDeferredPaymentRequest](pkdeferredpaymentrequest.md)
  An object that represents a request to set up a deferred payment, such as a hotel booking or a pre-order.
### Requesting multitoken or multimerchant payments
- [var multiTokenContexts: [PKPaymentTokenContext]](pkpaymentrequest/multitokencontexts.md)
  An array of payment token contexts to request multiple payment tokens with one payment token per context.
- [class PKPaymentTokenContext](pkpaymenttokencontext.md)
  A class that defines the context for a single payment token in a payment request for multimerchant payments.
### Requesting billing and shipping contact fields
- [var requiredBillingContactFields: Set<PKContactField>](pkpaymentrequest/requiredbillingcontactfields.md)
  A list of fields that you need for a billing contact to process the transaction.
- [var requiredShippingContactFields: Set<PKContactField>](pkpaymentrequest/requiredshippingcontactfields.md)
  A list of fields that you need for a shipping contact to process the transaction.
- [struct PKContactField](pkcontactfield.md)
  The fields that describe a contact.
### Providing known contact information
- [var billingContact: PKContact?](pkpaymentrequest/billingcontact.md)
  A prepopulated billing address.
- [var shippingContact: PKContact?](pkpaymentrequest/shippingcontact.md)
  A prepopulated shipping address.
- [class PKContact](pkcontact.md)
  An object that encapsulates contact information needed for billing and shipping.
### Setting the shipping methods and types
- [Displaying a Read-Only Pickup Address](displaying-a-read-only-pickup-address.md)
  Configure a payment request to display a read-only pickup address on the payment sheet.
- [var shippingMethods: [PKShippingMethod]?](pkpaymentrequest/shippingmethods.md)
  An array of shipping method objects that describe the supported shipping methods.
- [class PKShippingMethod](pkshippingmethod.md)
  An object that defines a shipping method for delivering physical goods.
- [var shippingType: PKShippingType](pkpaymentrequest/shippingtype.md)
  The type of shipping the request uses.
- [var shippingContactEditingMode: PKShippingContactEditingMode](pkpaymentrequest/shippingcontacteditingmode.md)
  A value that indicates whether the shipping mode prevents the user from editing the shipping address.
- [enum PKShippingType](pkshippingtype.md)
  A complete list of valid shipping types.
- [enum PKShippingContactEditingMode](pkshippingcontacteditingmode.md)
  Constants that indicate whether the shipping mode prevents the user from editing fields of the shipping address.
### Working with coupon codes
- [var couponCode: String?](pkpaymentrequest/couponcode.md)
  The initial coupon code for the payment request.
- [var supportsCouponCode: Bool](pkpaymentrequest/supportscouponcode.md)
  A Boolean value that determines whether the payment sheet displays the coupon code field.
### Adding custom data
- [var applicationData: Data?](pkpaymentrequest/applicationdata.md)
  Application-specific data or state.
### Providing error information
- [class func paymentBillingAddressInvalidError(withKey: String, localizedDescription: String?) -> any Error](pkpaymentrequest/paymentbillingaddressinvaliderror(withkey:localizeddescription:).md)
  Creates a billing address error with the supplied key and user-facing error message.
- [class func paymentContactInvalidError(withContactField: PKContactField, localizedDescription: String?) -> any Error](pkpaymentrequest/paymentcontactinvaliderror(withcontactfield:localizeddescription:).md)
  Creates a contact error with the supplied field and user-facing error message.
- [class func paymentShippingAddressInvalidError(withKey: String, localizedDescription: String?) -> any Error](pkpaymentrequest/paymentshippingaddressinvaliderror(withkey:localizeddescription:).md)
  Creates a shipping address error with the supplied key and user-facing error message.
- [class func paymentShippingAddressUnserviceableError(withLocalizedDescription: String?) -> any Error](pkpaymentrequest/paymentshippingaddressunserviceableerror(withlocalizeddescription:).md)
  Creates an error for an unserviceable address, with the supplied user-facing error message.
- [static func paymentCouponCodeInvalidError(localizedDescription: String?) -> any Error](pkpaymentrequest/paymentcouponcodeinvaliderror(localizeddescription:).md)
  Returns an error object that indicates an invalid coupon.
- [static func paymentCouponCodeExpiredError(localizedDescription: String?) -> any Error](pkpaymentrequest/paymentcouponcodeexpirederror(localizeddescription:).md)
  Returns an error object that indicates an expired coupon.
### Deprecated
- [static var enabled: PKShippingContactEditingMode](pkshippingcontacteditingmode/enabled.md)
  All fields of the shipping contact on the payment sheet are editable by the user.
- [var requiredBillingAddressFields: PKAddressField](pkpaymentrequest/requiredbillingaddressfields.md)
  A bit field of billing address fields that you need in order to process the transaction.
- [var requiredShippingAddressFields: PKAddressField](pkpaymentrequest/requiredshippingaddressfields.md)
  A bit field of shipping address fields that you need in order to process the transaction.
- [struct PKAddressField](pkaddressfield.md)
  Billing or shipping address fields.
- [var billingAddress: ABRecord?](pkpaymentrequest/billingaddress.md)
  A prepopulated billing address.
- [var shippingAddress: ABRecord?](pkpaymentrequest/shippingaddress.md)
  A prepopulated shipping address.
### Enumerations
- [PKPaymentRequest.ApplePayLaterAvailability](pkpaymentrequest/applepaylateravailability-swift.enum.md)
  Values you use to enable or disable Apple Pay Later for a specific transaction.
### Instance Properties
- [var applePayLaterAvailability: PKPaymentRequest.ApplePayLaterAvailability](pkpaymentrequest/applepaylateravailability-3dxrt.md)
  A value that indicates whether Apple Pay Later is available for a transaction.
- [var merchantCategoryCode: PKPaymentRequest.MerchantCategoryCode?](pkpaymentrequest/merchantcategorycode-9kcn6.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class PKRecurringPaymentRequest](pkrecurringpaymentrequest.md)
  A class that represents a request to set up a recurring payment, typically a subscription.
- [class PKAutomaticReloadPaymentRequest](pkautomaticreloadpaymentrequest.md)
  A class that represents a request to set up an automatic reload payment, such as a store card top-up or a prepaid account.
- [class PKDeferredPaymentRequest](pkdeferredpaymentrequest.md)
  An object that represents a request to set up a deferred payment, such as a hotel booking or a pre-order.
- [class PKPaymentTokenContext](pkpaymenttokencontext.md)
  A class that defines the context for a single payment token in a payment request for multimerchant payments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/PassKit/pkpaymentrequest)*