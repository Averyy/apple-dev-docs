# PKRecurringPaymentRequest

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

A class that represents a request to set up a recurring payment, typically a subscription.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class PKRecurringPaymentRequest
```

#### Overview

> ❗ **Important**:  You must set the [`recurringPaymentRequest`](pkpaymentrequest/recurringpaymentrequest.md) property on a [`PKPaymentRequest`](pkpaymentrequest.md) object to use this class to request a recurring payment.

 You must set the [`recurringPaymentRequest`](pkpaymentrequest/recurringpaymentrequest.md) property on a [`PKPaymentRequest`](pkpaymentrequest.md) object to use this class to request a recurring payment.

Use a [`PKRecurringPaymentRequest`](pkrecurringpaymentrequest.md) object to provide the user with payment details and a way to manage payment methods for a recurring payment. You can optionally display a billing agreement and set up merchant token life cycle notifications for the request.

For more information about the merchant token life cycle notifications, see Apple Pay Merchant Token Management API.

## Topics

### Creating a recurring payment request
- [init(paymentDescription: String, regularBilling: PKRecurringPaymentSummaryItem, managementURL: URL)](pkrecurringpaymentrequest/init(paymentdescription:regularbilling:managementurl:).md)
  Create a recurring payment object with a description, regular billing information, and a management URL.
### Describing a recurring payment
- [var paymentDescription: String](pkrecurringpaymentrequest/paymentdescription.md)
  A description that you provide of the recurring payment and that Apple Pay displays to the user in the payment sheet.
- [var billingAgreement: String?](pkrecurringpaymentrequest/billingagreement.md)
  A localized billing agreement that the payment sheet displays to the user before the user authorizes the payment.
### Setting payment summary items
- [var regularBilling: PKRecurringPaymentSummaryItem](pkrecurringpaymentrequest/regularbilling.md)
  The regular billing cycle for the recurring payment, including start and end dates, an interval, and an interval count.
- [var trialBilling: PKRecurringPaymentSummaryItem?](pkrecurringpaymentrequest/trialbilling.md)
  The trial billing cycle for the recurring payment.
- [class PKRecurringPaymentSummaryItem](pkrecurringpaymentsummaryitem.md)
  An object that defines a summary item for a payment that occurs repeatedly at a specified interval, such as a subscription.
### Managing payment tokens
- [var tokenNotificationURL: URL?](pkrecurringpaymentrequest/tokennotificationurl.md)
  A URL you provide to receive life-cycle notifications from the Apple Pay servers about the Apple Pay merchant token for the recurring payment.
- [var managementURL: URL](pkrecurringpaymentrequest/managementurl.md)
  A URL to a web page where the user can update or delete the payment method for the recurring payment.

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
- [class PKAutomaticReloadPaymentRequest](pkautomaticreloadpaymentrequest.md)
  A class that represents a request to set up an automatic reload payment, such as a store card top-up or a prepaid account.
- [class PKDeferredPaymentRequest](pkdeferredpaymentrequest.md)
  An object that represents a request to set up a deferred payment, such as a hotel booking or a pre-order.
- [class PKPaymentTokenContext](pkpaymenttokencontext.md)
  A class that defines the context for a single payment token in a payment request for multimerchant payments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkrecurringpaymentrequest)*