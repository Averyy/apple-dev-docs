# transactionHistory(forAccountID:since:isMonitoring:)

**Framework**: FinanceKit  
**Kind**: method

Returns the transactions for the specified account ID, optional starting time, and monitoring indicator for long running transaction queries.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
func transactionHistory(forAccountID accountID: UUID, since token: FinanceStore.HistoryToken? = nil, isMonitoring: Bool = true) -> FinanceStore.History<Transaction>
```

#### Return Value

A [`FinanceStore.History`](financestore/history.md) of transactions that match the provided `accountID`.

#### Discussion

Use this method to search the finance store for transactions in a specific account and receive updates as the framework enters new transactions into the finance store. You can, optionally, specify a starting date and time by providing a `historyToken`.

## Parameters

- `accountID`: An account identifier.
- `token`: An optional   that describes a start time.
- `isMonitoring`: A Boolean value that indicates the method should return records asynchronously as the system updates the FinanceStore.

## See Also

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
- [struct TransactionQuery](transactionquery.md)
  A structure that describes the parameters to use for a transaction query.
- [enum TransactionType](transactiontype.md)
  Values that describe kinds of transactions.
- [enum TransactionStatus](transactionstatus.md)
  Values that describe the status of a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/transactionhistory(foraccountid:since:ismonitoring:))*