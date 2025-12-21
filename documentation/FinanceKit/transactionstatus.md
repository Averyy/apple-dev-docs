# TransactionStatus

**Framework**: FinanceKit  
**Kind**: enum

Values that describe the status of a transaction.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
enum TransactionStatus
```

## Topics

### Enumeration Cases
- [TransactionStatus.authorized](transactionstatus/authorized.md)
  The transaction is in an authorized state.
- [TransactionStatus.booked](transactionstatus/booked.md)
  The transaction is in a booked state.
- [TransactionStatus.memo](transactionstatus/memo.md)
  A memo that provides information about the transaction.
- [TransactionStatus.pending](transactionstatus/pending.md)
  The transaction is in a pending state.
- [TransactionStatus.rejected](transactionstatus/rejected.md)
  The transaction is in a rejected state.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [struct TransactionQuery](transactionquery.md)
  A structure that describes the parameters to use for a transaction query.
- [enum TransactionType](transactiontype.md)
  Values that describe kinds of transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/transactionstatus)*