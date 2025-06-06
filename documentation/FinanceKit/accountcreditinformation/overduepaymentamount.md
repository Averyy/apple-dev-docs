# overduePaymentAmount

**Framework**: FinanceKit  
**Kind**: property

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/accountcreditinformation/overduepaymentamount)*