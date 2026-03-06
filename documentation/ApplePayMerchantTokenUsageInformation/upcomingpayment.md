# UpcomingPayment

**Framework**: Apple Pay Merchant Token Usage Information API  
**Kind**: dictionary

An upcoming payment.

## Declaration

```swift
object UpcomingPayment
```

## Properties

- `automaticReloadPaymentDetails` (AutomaticReloadPaymentDetails): The details about an automatic reload payment. Required if `paymentType` is `automaticReload`.
- `deferredPaymentDetails` (DeferredPaymentDetails): The details about a deferred payment. Required if `paymentType` is `deferred`.
- `identifier` (string) *(required)*: An opaque value that uniquely identifies the payment in the usage information. The value isn’t displayed to the user.
- `imageName` (string): The name of an image that represents the payment.
- `label` (string) *(required)*: A short, localized description of the payment, such as the service name.
- `paymentType` (string) *(required)*: The payment’s type.
- `recurringPaymentDetails` (RecurringPaymentDetails): Details about a recurring payment. Required if `paymentType` is `recurring`.

## See Also

- [object AutomaticReloadPaymentDetails](automaticreloadpaymentdetails.md)
  Details about an automatic reload payment.
- [object DeferredPaymentDetails](deferredpaymentdetails.md)
  Details about a deferred payment, such as a hotel booking or a preorder.
- [object PastPayment](pastpayment.md)
  A past payment.
- [object RecurringPaymentDetails](recurringpaymentdetails.md)
  Details about a recurring payment, typically a subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation/upcomingpayment)*