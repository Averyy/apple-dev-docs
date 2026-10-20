# overduePaymentAmount

**Framework**: FinanceKit  
**Kind**: property  
**Role**: Instance Property

The amount by which the account is overdue for the current period.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
let overduePaymentAmount: CurrencyAmount?
```

#### Discussion

If not `nil` and `minimumNextPaymentAmount` is not `nil` then the `minimumNextPaymentAmount` has information about the next bill.

## See Also

### Instance Properties
- [let creditLimit: CurrencyAmount?](./creditlimit.md)
  The credit limit of the account.
- [let minimumNextPaymentAmount: CurrencyAmount?](./minimumnextpaymentamount.md)
  Minimum amount of the next non-overdue payment.
- [let nextPaymentDueDate: Date?](./nextpaymentduedate.md)
  Date of the next payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/accountcreditinformation/overduepaymentamount)*