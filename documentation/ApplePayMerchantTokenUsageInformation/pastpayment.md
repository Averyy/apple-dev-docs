# PastPayment

**Framework**: Apple Pay Merchant Token Usage Information API  
**Kind**: dictionary

A past payment.

## Declaration

```swift
object PastPayment
```

## Topics

### Dictionaries
- [object PastPayment.LineItems](pastpayment/lineitems-data.dictionary.md)
  The goods or services paid for.
- [object PastPayment.SummaryItems](pastpayment/summaryitems-data.dictionary.md)
  Items that summarize the total amount, such as taxes or shipping cost.

## Properties

- `identifier` (string) *(required)*: An opaque value that uniquely identifies this payment in the usage information. The value isn’t displayed to the user.
- `lineItems` ([PastPayment.LineItems]): The goods or services paid for.
- `paymentDate` (string) *(required)*: The date, in the past, of the payment, in ISO 8601 format; time is optional.
- `summaryItems` ([PastPayment.SummaryItems]): Items that summarize the total amount, such as taxes or shipping cost.
- `totalAmount` (CurrencyAmount) *(required)*: The total amount of the payment.

## See Also

- [object AutomaticReloadPaymentDetails](automaticreloadpaymentdetails.md)
  Details about an automatic reload payment.
- [object DeferredPaymentDetails](deferredpaymentdetails.md)
  Details about a deferred payment, such as a hotel booking or a preorder.
- [object PaymentIssueDetails](paymentissuedetails.md)
  Details about a payment issue, such as a declined payment.
- [object RecurringPaymentDetails](recurringpaymentdetails.md)
  Details about a recurring payment, typically a subscription.
- [object UpcomingPayment](upcomingpayment.md)
  An upcoming payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation/pastpayment)*