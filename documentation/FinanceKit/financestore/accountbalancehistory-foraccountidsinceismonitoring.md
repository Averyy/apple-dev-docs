# accountBalanceHistory(forAccountID:since:isMonitoring:)

**Framework**: FinanceKit  
**Kind**: method

Returns the account balance history since a time specified by the provided financial history token.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
func accountBalanceHistory(forAccountID accountID: UUID, since token: FinanceStore.HistoryToken? = nil, isMonitoring: Bool = true) -> FinanceStore.History<AccountBalance>
```

#### Return Value

A `History` that describes the account balances.

#### Discussion

Use this method to monitor the balance of a specific account.  Provide a `historyToken` to specify a starting data and time.

## Parameters

- `accountID`: A   that identifies a specific account a person has added to the finance store.
- `token`: An optional   that defines the starting date and time to return records from.
- `isMonitoring`: A Boolean value that indicates whether the framework should return a   sequence that indicates the changes to the accounts over time. Defaults to  .

## See Also

- [func accountBalances(query: AccountBalanceQuery) async throws -> [AccountBalance]](financestore/accountbalances(query:).md)
  Returns a list of balances that meet the criteria in the provided account query.
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

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/accountbalancehistory(foraccountid:since:ismonitoring:))*