# FinanceStore

**Framework**: FinanceKit  
**Kind**: class  
**Role**: Class

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
- [static let shared: FinanceStore](./financestore/shared.md)
  The shared instance of the store that you make calls through.
### Determining data availability
- [static func isDataAvailable(FinanceStore.DataType) -> Bool](./financestore/isdataavailable%28_%29.md)
  Returns a Boolean value that indicates if data that represents the provided type is available in the finance store.
### Checking authorization status and requesting authorization
- [func authorizationStatus() async throws -> AuthorizationStatus](./financestore/authorizationstatus%28%29.md)
  Checks the authorization status for the calling application.
- [func requestAuthorization() async throws -> AuthorizationStatus](./financestore/requestauthorization%28%29.md)
  Prompts a person to give FinanceKit authorization to access financial data.
### Finding accounts
- [func accountHistory(since: FinanceStore.HistoryToken?, isMonitoring: Bool) -> FinanceStore.History<Account>](./financestore/accounthistory%28since,ismonitoring%29.md)
  Returns a list of accounts a person added since a time specified by the provided financial history token.
- [func accounts(query: AccountQuery) async throws -> [Account]](./financestore/accounts%28query%29.md)
  Returns a list of accounts a person added to their Wallet that meet the criteria in the provided account query.
### Getting account balances
- [func accountBalances(query: AccountBalanceQuery) async throws -> [AccountBalance]](./financestore/accountbalances%28query%29.md)
  Returns a list of balances that meet the criteria in the provided account query.
- [func accountBalanceHistory(forAccountID: UUID, since: FinanceStore.HistoryToken?, isMonitoring: Bool) -> FinanceStore.History<AccountBalance>](./financestore/accountbalancehistory%28foraccountid,since,ismonitoring%29.md)
  Returns the account balance history since a time specified by the provided financial history token.
### Searching for a specific order
- [func containsOrder(matching: FullyQualifiedOrderIdentifier, updatedDate: Date?) async throws -> FinanceStore.ContainsOrderResult](./financestore/containsorder%28matching,updateddate%29.md)
  Checks whether the finance store contains an order.
### Saving or updating orders
- [func saveOrder(signedArchive: Data) async throws -> FinanceStore.SaveOrderResult](./financestore/saveorder%28signedarchive%29.md)
  Adds an order to the store or updates an existing order.
### Monitoring transactions
- [func transactionHistory(forAccountID: UUID, since: FinanceStore.HistoryToken?, isMonitoring: Bool) -> FinanceStore.History<Transaction>](./financestore/transactionhistory%28foraccountid,since,ismonitoring%29.md)
  Returns the transactions for the specified account ID, optional starting time, and monitoring indicator for long running transaction queries.
- [func transactions(query: TransactionQuery) async throws -> [Transaction]](./financestore/transactions%28query%29.md)
  Returns transactions that match the provided transaction query.
### Enumerations
- [FinanceStore.ContainsOrderResult](./financestore/containsorderresult.md)
  Result type for queries against the finance store’s orders.
- [FinanceStore.DataType](./financestore/datatype.md)
  Values that describe the kinds of data in the finance store.
- [FinanceStore.SaveOrderResult](./financestore/saveorderresult.md)
  Result type for the finance store’s save order method.
- [FinanceStore.BackgroundDataType](./financestore/backgrounddatatype.md)
  Types of data in the finance store supported by background delivery.
- [FinanceStore.UpdateFrequency](./financestore/updatefrequency.md)
  Frequencies of background delivery updates.
### Structures
- [FinanceStore.Changes](./financestore/changes.md)
  A structure that records changes to the finance store.
- [FinanceStore.History](./financestore/history.md)
  A structure the framework uses to collect and iterate over finance store model objects.
- [FinanceStore.HistoryToken](./financestore/historytoken.md)
  A structure that describes the starting point to use for financial data queries.
### Instance Methods
- [func disableAllBackgroundDelivery()](./financestore/disableallbackgrounddelivery%28%29.md)
  Disables background delivery for all data types.
- [func disableBackgroundDelivery(for: [FinanceStore.BackgroundDataType])](./financestore/disablebackgrounddelivery%28for%29.md)
  Disables background delivery for the specified types.
- [func enableBackgroundDelivery(for: [FinanceStore.BackgroundDataType], frequency: FinanceStore.UpdateFrequency)](./financestore/enablebackgrounddelivery%28for,frequency%29.md)
  Enables background delivery for the specified types and frequency.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore)*