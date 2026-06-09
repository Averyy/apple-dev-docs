# PaymentIssueDetails

**Framework**: Apple Pay Merchant Token Usage Information API  
**Kind**: dictionary

Details about a payment issue, such as a declined payment.

## Declaration

```swift
object PaymentIssueDetails
```

## Properties

- `issueKind` (string) *(required)*: The kind of payment issue.
- `issueDate` (date) *(required)*: The date of the payment issue in ISO 8601 format.

## See Also

- [object AutomaticReloadPaymentDetails](automaticreloadpaymentdetails.md)
  Details about an automatic reload payment.
- [object DeferredPaymentDetails](deferredpaymentdetails.md)
  Details about a deferred payment, such as a hotel booking or a preorder.
- [object PastPayment](pastpayment.md)
  A past payment.
- [object RecurringPaymentDetails](recurringpaymentdetails.md)
  Details about a recurring payment, typically a subscription.
- [object UpcomingPayment](upcomingpayment.md)
  An upcoming payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation/paymentissuedetails)*