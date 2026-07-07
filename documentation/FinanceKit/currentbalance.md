# CurrentBalance

**Framework**: FinanceKit  
**Kind**: enum

Values that describe the state of an account’s credit balance.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
enum CurrentBalance
```

## Topics

### Enumeration Cases
- [CurrentBalance.available(_:)](currentbalance/available(_:).md)
  Only the available balance is present.
- [case availableAndBooked(available: Balance, booked: Balance)](currentbalance/availableandbooked(available:booked:).md)
  Both available and booked balances are present.
- [CurrentBalance.booked(_:)](currentbalance/booked(_:).md)
  Only the booked balance is present.

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
- [struct Balance](balance.md)
  A structure that describes an account balance.
- [enum CreditDebitIndicator](creditdebitindicator.md)
  Values that the framework uses to describe transactions as credits or debits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/currentbalance)*