# TransactionQuery

**Framework**: FinanceKit  
**Kind**: struct

A structure that describes the parameters to use for a transaction query.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct TransactionQuery
```

#### Overview

Use a `TransactionQuery` to find and filter transactions in a person’s accounts.

## Topics

### Initializers
- [init(sortDescriptors: [SortDescriptor<Transaction>], predicate: Predicate<Transaction>?, limit: Int?, offset: Int?)](transactionquery/init(sortdescriptors:predicate:limit:offset:).md)
  Creates a new transaction query with the provided sort descriptors, predicate, and limit on the number of records the query should return.
### Type Methods
- [static func predicate(forMerchantCategoryCodes: [MerchantCategoryCode]) -> Predicate<Transaction>](transactionquery/predicate(formerchantcategorycodes:).md)
  A predicate that returns transactions that match any of the provided merchant category codes.
- [static func predicate(forStatuses: [TransactionStatus]) -> Predicate<Transaction>](transactionquery/predicate(forstatuses:).md)
  Returns a predicate that matches any of the provided transaction statuses.
- [static func predicate(forTransactionTypes: [TransactionType]) -> Predicate<Transaction>](transactionquery/predicate(fortransactiontypes:).md)
  Returns a predicate that matches any of the provided transaction types.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [func transactionHistory(forAccountID: UUID, since: FinanceStore.HistoryToken?, isMonitoring: Bool) -> FinanceStore.History<Transaction>](financestore/transactionhistory(foraccountid:since:ismonitoring:).md)
  Returns the transactions for the specified account ID, optional starting time, and monitoring indicator for long running transaction queries.
- [func transactions(query: TransactionQuery) async throws -> [Transaction]](financestore/transactions(query:).md)
  Returns transactions that match the provided transaction query.
- [struct AccountQuery](accountquery.md)
  A structure that defines an account query.
- [struct AccountCreditInformation](accountcreditinformation.md)
  A structure that describes the credit information associated with an account.
- [struct CurrencyAmount](currencyamount.md)
  A structure that describes a monetary amount and its currency.
- [struct Transaction](transaction.md)
  A structure that represents a transaction relating to a specific financial account.
- [enum TransactionType](transactiontype.md)
  Values that describe kinds of transactions.
- [enum TransactionStatus](transactionstatus.md)
  Values that describe the status of a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/transactionquery)*