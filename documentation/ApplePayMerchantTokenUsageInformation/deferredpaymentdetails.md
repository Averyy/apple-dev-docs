# DeferredPaymentDetails

**Framework**: Apple Pay Merchant Token Usage Information API  
**Kind**: dictionary

Details about a deferred payment, such as a hotel booking or a preorder.

## Declaration

```swift
object DeferredPaymentDetails
```

## Properties

- `amount` (CurrencyAmount): The amount to be charged. Omit if the amount isn’t yet known, for example, for mini-bar charges at a hotel.
- `paymentDate` (date): The date, in the future, of the payment, in ISO 8601 format, with the time ignored. Omit if the payment date isn’t yet known, for example, for goods yet to be produced.

## See Also

- [object AutomaticReloadPaymentDetails](automaticreloadpaymentdetails.md)
  Details about an automatic reload payment.
- [object PastPayment](pastpayment.md)
  A past payment.
- [object RecurringPaymentDetails](recurringpaymentdetails.md)
  Details about a recurring payment, typically a subscription.
- [object UpcomingPayment](upcomingpayment.md)
  An upcoming payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation/deferredpaymentdetails)*