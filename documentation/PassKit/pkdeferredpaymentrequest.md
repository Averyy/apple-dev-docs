# PKDeferredPaymentRequest

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that represents a request to set up a deferred payment, such as a hotel booking or a pre-order.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- visionOS 1.0+

## Declaration

```swift
class PKDeferredPaymentRequest
```

#### Overview

This request receives a merchant-specific payment token, if the payment network supports merchant-specific payment tokens.

> ❗ **Important**:  You must set the [`deferredPaymentRequest`](pkpaymentrequest/deferredpaymentrequest.md) property on a [`PKPaymentRequest`](pkpaymentrequest.md) object to use the `PKDeferredPaymentRequest` class and set up a deferred payment.

Use a `PKDeferredPaymentRequest` object to provide the user with payment details and a way to manage payment methods for a deferred payment. You can optionally display a billing agreement and set up merchant token life cycle notifications for the request.

For more information about the merchant token life cycle notifications, see [`Apple Pay Merchant Token Management API`](https://developer.apple.com/documentation/MerchantTokenNotificationServices).

## Topics

### Creating a deferred payment request
- [init(paymentDescription: String, deferredBilling: PKDeferredPaymentSummaryItem, managementURL: URL)](pkdeferredpaymentrequest/init(paymentdescription:deferredbilling:managementurl:).md)
  Creates a deferred payment request with the payment description, deferred billing summary, and management URL you provide.
### Describing a deferred payment
- [var freeCancellationDate: Date?](pkdeferredpaymentrequest/freecancellationdate.md)
  The date before which you must cancel a deferred payment without incurring any cancellation charges.
- [var billingAgreement: String?](pkdeferredpaymentrequest/billingagreement.md)
  The localized billing agreement the framework displays to the user prior to payment authorization.
- [var paymentDescription: String](pkdeferredpaymentrequest/paymentdescription.md)
  A description of the deferred payment.
- [var freeCancellationDateTimeZone: TimeZone?](pkdeferredpaymentrequest/freecancellationdatetimezone.md)
  The time zone at the destination location of the payment.
### Setting payment summary items
- [var deferredBilling: PKDeferredPaymentSummaryItem](pkdeferredpaymentrequest/deferredbilling.md)
  An object that contains details about the deferred payment.
- [class PKDeferredPaymentSummaryItem](pkdeferredpaymentsummaryitem.md)
  An object that defines a summary item for a payment that occurs at a later date, such as a pre-order.
### Managing payment tokens
- [var managementURL: URL](pkdeferredpaymentrequest/managementurl.md)
  A URL that links to a page on your web site where the user can manage the payment method for the deferred payment, including deleting it.
- [var tokenNotificationURL: URL?](pkdeferredpaymentrequest/tokennotificationurl.md)
  A URL to receive life-cycle notifications for the merchant-specific payment token the system issues for the request, if applicable.

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

- [class PKPaymentRequest](pkpaymentrequest.md)
  An object that represents a request for payment, including details about payment-processing capabilities, the payment amount, and shipping information.
- [class PKRecurringPaymentRequest](pkrecurringpaymentrequest.md)
  A class that represents a request to set up a recurring payment, typically a subscription.
- [class PKAutomaticReloadPaymentRequest](pkautomaticreloadpaymentrequest.md)
  A class that represents a request to set up an automatic reload payment, such as a store card top-up or a prepaid account.
- [class PKPaymentTokenContext](pkpaymenttokencontext.md)
  A class that defines the context for a single payment token in a payment request for multimerchant payments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdeferredpaymentrequest)*