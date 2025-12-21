# creditDebitIndicator

**Framework**: FinanceKit  
**Kind**: property

A value that indicates whether the balance is a credit or a debit balance.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
let creditDebitIndicator: CreditDebitIndicator
```

#### Discussion

If an asset account has a positive balance, then the [`CreditDebitIndicator`](creditdebitindicator.md) is [`CreditDebitIndicator.credit`](creditdebitindicator/credit.md). If it has a negative balance, then the `CreditDebitIndicator` is [`CreditDebitIndicator.debit`](creditdebitindicator/debit.md).

If a liability account has a  balance, then the `CreditDebitIndicator` is `CreditDebitIndicator/debit`. If it has been  then the `CreditDebitIndicator` is `CreditDebitIndicator/credit`.

> **Note**:  FinanceKit considers a zero balance to be a credit balance.

## See Also

- [let amount: CurrencyAmount](balance/amount.md)
  The amount of the balance.
- [let asOfDate: Date](balance/asofdate.md)
  The date and time the system calculated the balance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/balance/creditdebitindicator)*