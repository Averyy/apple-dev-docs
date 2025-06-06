# AccountBalanceQuery

**Framework**: FinanceKit  
**Kind**: struct

A structure that defines an account balance query.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct AccountBalanceQuery
```

#### Overview

Use an `AccountBalanceQuery` to find and filter specific balances in a person’s accounts.

## Topics

### Initializers
- [init(sortDescriptors: [SortDescriptor<AccountBalance>], predicate: Predicate<AccountBalance>?, limit: Int?, offset: Int?)](accountbalancequery/init(sortdescriptors:predicate:limit:offset:).md)
  Creates a new account balance query structure with the provided sort descriptors.
### Type Methods
- [static func predicate(availableSince: Date, until: Date?) -> Predicate<AccountBalance>](accountbalancequery/predicate(availablesince:until:).md)
  A predicate that returns available account balances since a specified date, and, optionally, until another date.
- [static func predicate(bookedSince: Date, until: Date?) -> Predicate<AccountBalance>](accountbalancequery/predicate(bookedsince:until:).md)
  A predicate that returns booked account balances since a specified date until another date.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [func accountBalances(query: AccountBalanceQuery) async throws -> [AccountBalance]](financestore/accountbalances(query:).md)
  Returns a list of balances that meet the criteria in the provided account query.
- [func accountBalanceHistory(forAccountID: UUID, since: FinanceStore.HistoryToken?, isMonitoring: Bool) -> FinanceStore.History<AccountBalance>](financestore/accountbalancehistory(foraccountid:since:ismonitoring:).md)
  Returns the account balance history since a time specified by the provided financial history token.
- [struct AccountBalance](accountbalance.md)
  A structure that describes the financial balance of an account at a specific point in time.
- [struct Balance](balance.md)
  A structure that describes an account balance.
- [enum CreditDebitIndicator](creditdebitindicator.md)
  Values that the framework uses to describe transactions as credits or debits.
- [enum CurrentBalance](currentbalance.md)
  Values that describe the state of an account’s credit balance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/accountbalancequery)*