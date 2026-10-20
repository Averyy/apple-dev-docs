# CreditDebitIndicator

**Framework**: FinanceKit  
**Kind**: enum  
**Role**: Enumeration

Values that the framework uses to describe transactions as credits or debits.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
enum CreditDebitIndicator
```

## Topics

### Enumeration Cases
- [CreditDebitIndicator.credit](./creditdebitindicator/credit.md)
  A value that indicates an amount which increases an asset or decreases a liability.
- [CreditDebitIndicator.debit](./creditdebitindicator/debit.md)
  A value that indicates an amount which increases a liability or decreases an asset.

## Relationships

### Conforms To
- [CaseIterable](../Swift/caseiterable.md)
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Balances
- [func accountBalances(query: AccountBalanceQuery) async throws -> [AccountBalance]](./financestore/accountbalances%28query%29.md)
  Returns a list of balances that meet the criteria in the provided account query.
- [func accountBalanceHistory(forAccountID: UUID, since: FinanceStore.HistoryToken?, isMonitoring: Bool) -> FinanceStore.History<AccountBalance>](./financestore/accountbalancehistory%28foraccountid,since,ismonitoring%29.md)
  Returns the account balance history since a time specified by the provided financial history token.
- [struct AccountBalance](./accountbalance.md)
  A structure that describes the financial balance of an account at a specific point in time. The financial balance of an account at a specific point in time.
- [struct AccountBalanceQuery](./accountbalancequery.md)
  A structure that defines an account balance query.
- [struct Balance](./balance.md)
  A structure that describes an account balance.
- [enum CurrentBalance](./currentbalance.md)
  Values that describe the state of an account’s credit balance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/creditdebitindicator)*