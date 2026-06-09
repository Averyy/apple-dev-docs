# RecurringPaymentDetails

**Framework**: Apple Pay Merchant Token Usage Information API  
**Kind**: dictionary

Details about a recurring payment, typically a subscription.

## Declaration

```swift
object RecurringPaymentDetails
```

## Topics

### Dictionaries
- [object RecurringPaymentDetails.Interval](recurringpaymentdetails/interval-data.dictionary.md)
  The payment interval.
- [object RecurringPaymentDetails.ScheduledPayments](recurringpaymentdetails/scheduledpayments-data.dictionary.md)
  Future occurrences of the recurring payment.

## Properties

- `endsAfterLastPayment` (boolean): A flag that indicates whether the recurring payment ends after the last scheduled payment. The default value is `false`. Set value to `true` for installments that include all payments of the plan in `scheduledPayments`.
- `interval` (RecurringPaymentDetails.Interval) *(required)*: The payment interval.
- `recurringPaymentType` (string) *(required)*: The recurring payment’s type.
- `scheduledPayments` ([RecurringPaymentDetails.ScheduledPayments]): Future occurrences of the recurring payment. For installments, include all payments of the plan.

## See Also

- [object AutomaticReloadPaymentDetails](automaticreloadpaymentdetails.md)
  Details about an automatic reload payment.
- [object DeferredPaymentDetails](deferredpaymentdetails.md)
  Details about a deferred payment, such as a hotel booking or a preorder.
- [object PastPayment](pastpayment.md)
  A past payment.
- [object PaymentIssueDetails](paymentissuedetails.md)
  Details about a payment issue, such as a declined payment.
- [object UpcomingPayment](upcomingpayment.md)
  An upcoming payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation/recurringpaymentdetails)*