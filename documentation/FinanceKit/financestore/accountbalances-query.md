# accountBalances(query:)

**Framework**: FinanceKit  
**Kind**: method

Returns a list of balances that meet the criteria in the provided account query.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
func accountBalances(query: AccountBalanceQuery) async throws -> [AccountBalance]
```

#### Return Value

An array of [`AccountBalance`](accountbalance.md) structures.

## Parameters

- `query`: An   that describes the kinds of accounts to look for.

## See Also

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
- [enum CurrentBalance](currentbalance.md)
  Values that describe the state of an account’s credit balance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/accountbalances(query:))*