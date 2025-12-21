# Balance

**Framework**: FinanceKit  
**Kind**: struct

A structure that describes an account balance.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct Balance
```

## Topics

### Instance Properties
- [let amount: CurrencyAmount](balance/amount.md)
  The amount of the balance.
- [let asOfDate: Date](balance/asofdate.md)
  The date and time the system calculated the balance.
- [let creditDebitIndicator: CreditDebitIndicator](balance/creditdebitindicator.md)
  A value that indicates whether the balance is a credit or a debit balance.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func accountBalances(query: AccountBalanceQuery) async throws -> [AccountBalance]](financestore/accountbalances(query:).md)
  Returns a list of balances that meet the criteria in the provided account query.
- [func accountBalanceHistory(forAccountID: UUID, since: FinanceStore.HistoryToken?, isMonitoring: Bool) -> FinanceStore.History<AccountBalance>](financestore/accountbalancehistory(foraccountid:since:ismonitoring:).md)
  Returns the account balance history since a time specified by the provided financial history token.
- [struct AccountBalance](accountbalance.md)
  A structure that describes the financial balance of an account at a specific point in time. The financial balance of an account at a specific point in time.
- [struct AccountBalanceQuery](accountbalancequery.md)
  A structure that defines an account balance query.
- [enum CreditDebitIndicator](creditdebitindicator.md)
  Values that the framework uses to describe transactions as credits or debits.
- [enum CurrentBalance](currentbalance.md)
  Values that describe the state of an account’s credit balance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/balance)*