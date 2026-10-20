# AutomaticReloadPaymentDetails

**Framework**: Apple Pay Merchant Token Usage Information API  
**Kind**: dictionary  
**Role**: Object

Details about an automatic reload payment.

## Declaration

```
object AutomaticReloadPaymentDetails
```

## Properties

- `amount` (CurrencyAmount): The reload amount when the account balance reaches the threshold amount. Omit this property if the reload amount is variable, for example, to match a target account balance.
- `thresholdAmount` (CurrencyAmount): The balance an account reaches before the system applies the automatic reload amount.

## See Also

### Getting payment details
- [object DeferredPaymentDetails](./deferredpaymentdetails.md)
  Details about a deferred payment, such as a hotel booking or a preorder.
- [object PastPayment](./pastpayment.md)
  A past payment.
- [object PaymentIssueDetails](./paymentissuedetails.md)
  Details about a payment issue, such as a declined payment.
- [object RecurringPaymentDetails](./recurringpaymentdetails.md)
  Details about a recurring payment, typically a subscription.
- [object UpcomingPayment](./upcomingpayment.md)
  An upcoming payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation/automaticreloadpaymentdetails)*