# CurrencyAmount

**Framework**: FinanceKit  
**Kind**: struct

A structure that describes a monetary amount and its currency.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct CurrencyAmount
```

## Topics

### Operators
- [static func == (CurrencyAmount, CurrencyAmount) -> Bool](currencyamount/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [let amount: Decimal](currencyamount/amount.md)
  The numeric value of the amount.
- [let currencyCode: String](currencyamount/currencycode.md)
  The currency of the amount.
- [var hashValue: Int](currencyamount/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](currencyamount/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](currencyamount/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
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
- [struct Transaction](transaction.md)
  A structure that represents a transaction relating to a specific financial account.
- [struct TransactionQuery](transactionquery.md)
  A structure that describes the parameters to use for a transaction query.
- [enum TransactionType](transactiontype.md)
  Values that describe kinds of transactions.
- [enum TransactionStatus](transactionstatus.md)
  Values that describe the status of a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/currencyamount)*