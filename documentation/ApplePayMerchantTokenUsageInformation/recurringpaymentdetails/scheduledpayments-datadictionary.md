# RecurringPaymentDetails.ScheduledPayments

**Framework**: Apple Pay Merchant Token Usage Information API  
**Kind**: dictionary

Future occurrences of the recurring payment.

## Declaration

```swift
object RecurringPaymentDetails.ScheduledPayments
```

#### Discussion

For installments, include all payments of the plan.

## Properties

- `amount` (CurrencyAmount): The amount to be charged. Omit if the amount isn’t yet known, for example, in usage-based billing.
- `paymentDate` (date) *(required)*: The date, in the future, of the payment, in ISO 8601 format. This property ignores the time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation/recurringpaymentdetails/scheduledpayments-data.dictionary)*