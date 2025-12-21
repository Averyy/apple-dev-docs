# transactions(query:)

**Framework**: FinanceKit  
**Kind**: method

Returns transactions that match the provided transaction query.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
func transactions(query: TransactionQuery) async throws -> [Transaction]
```

#### Return Value

An array of [`Transaction`](transaction.md) records that match the provided `query`.

## Parameters

- `query`: A   that describes the kinds of transactions to look for.

## See Also

- [func transactionHistory(forAccountID: UUID, since: FinanceStore.HistoryToken?, isMonitoring: Bool) -> FinanceStore.History<Transaction>](financestore/transactionhistory(foraccountid:since:ismonitoring:).md)
  Returns the transactions for the specified account ID, optional starting time, and monitoring indicator for long running transaction queries.
- [struct AccountQuery](accountquery.md)
  A structure that defines an account query.
- [struct AccountCreditInformation](accountcreditinformation.md)
  A structure that describes the credit information associated with an account.
- [struct CurrencyAmount](currencyamount.md)
  A structure that describes a monetary amount and its currency.
- [struct Transaction](transaction.md)
  A structure that represents a transaction relating to a specific financial account.
- [struct TransactionQuery](transactionquery.md)
  A structure that describes the parameters to use for a transaction query.
- [enum TransactionType](transactiontype.md)
  Values that describe kinds of transactions.
- [enum TransactionStatus](transactionstatus.md)
  Values that describe the status of a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/transactions(query:))*