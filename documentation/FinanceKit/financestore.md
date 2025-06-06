# FinanceStore

**Framework**: FinanceKit  
**Kind**: class

Secure storage for Apple Wallet orders.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
class FinanceStore
```

## Topics

### Retrieving the shared instance
- [static let shared: FinanceStore](financestore/shared.md)
  The shared instance of the store that you make calls through.
### Determining data availability
- [static func isDataAvailable(FinanceStore.DataType) -> Bool](financestore/isdataavailable(_:).md)
  Returns a Boolean value that indicates if data that represents the provided type is available in the finance store.
### Checking authorization status and requesting authorization
- [func authorizationStatus() async throws -> AuthorizationStatus](financestore/authorizationstatus.md)
  Checks the authorization status for the calling application.
- [func requestAuthorization() async throws -> AuthorizationStatus](financestore/requestauthorization.md)
  Prompts a person to give FinanceKit authorization to access financial data.
### Finding accounts
- [func accountHistory(since: FinanceStore.HistoryToken?, isMonitoring: Bool) -> FinanceStore.History<Account>](financestore/accounthistory(since:ismonitoring:).md)
  Returns a list of accounts a person added since a time specified by the provided financial history token.
- [func accounts(query: AccountQuery) async throws -> [Account]](financestore/accounts(query:).md)
  Returns a list of accounts a person added to their Wallet that meet the criteria in the provided account query.
### Getting account balances
- [func accountBalances(query: AccountBalanceQuery) async throws -> [AccountBalance]](financestore/accountbalances(query:).md)
  Returns a list of balances that meet the criteria in the provided account query.
- [func accountBalanceHistory(forAccountID: UUID, since: FinanceStore.HistoryToken?, isMonitoring: Bool) -> FinanceStore.History<AccountBalance>](financestore/accountbalancehistory(foraccountid:since:ismonitoring:).md)
  Returns the account balance history since a time specified by the provided financial history token.
### Searching for a specific order
- [func containsOrder(matching: FullyQualifiedOrderIdentifier, updatedDate: Date?) async throws -> FinanceStore.ContainsOrderResult](financestore/containsorder(matching:updateddate:).md)
  Checks whether the finance store contains an order.
### Saving or updating orders
- [func saveOrder(signedArchive: Data) async throws -> FinanceStore.SaveOrderResult](financestore/saveorder(signedarchive:).md)
  Adds an order to the store or updates an existing order.
### Monitoring transactions
- [func transactionHistory(forAccountID: UUID, since: FinanceStore.HistoryToken?, isMonitoring: Bool) -> FinanceStore.History<Transaction>](financestore/transactionhistory(foraccountid:since:ismonitoring:).md)
  Returns the transactions for the specified account ID, optional starting time, and monitoring indicator for long running transaction queries.
- [func transactions(query: TransactionQuery) async throws -> [Transaction]](financestore/transactions(query:).md)
  Returns transactions that match the provided transaction query.
### Enumerations
- [FinanceStore.ContainsOrderResult](financestore/containsorderresult.md)
  Result type for queries against the finance store’s orders.
- [FinanceStore.DataType](financestore/datatype.md)
  Values that describe the kinds of data in the finance store.
- [FinanceStore.SaveOrderResult](financestore/saveorderresult.md)
  Result type for the finance store’s save order method.
### Structures
- [FinanceStore.Changes](financestore/changes.md)
  A structure that records changes to the finance store.
- [FinanceStore.History](financestore/history.md)
  A structure the framework uses to collect and iterate over finance store model objects.
- [FinanceStore.HistoryToken](financestore/historytoken.md)
  A structure that describes the starting point to use for financial data queries.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore)*