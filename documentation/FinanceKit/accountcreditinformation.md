# AccountCreditInformation

**Framework**: FinanceKit  
**Kind**: struct

A structure that describes the credit information associated with an account.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct AccountCreditInformation
```

#### Overview

Credit information includes credit limits, payment dates, and minimum payment dates and amounts for current and upcoming payments.

## Topics

### Instance Properties
- [let creditLimit: CurrencyAmount?](accountcreditinformation/creditlimit.md)
  The credit limit of the account.
- [let minimumNextPaymentAmount: CurrencyAmount?](accountcreditinformation/minimumnextpaymentamount.md)
  Minimum amount of the next non-overdue payment.
- [let nextPaymentDueDate: Date?](accountcreditinformation/nextpaymentduedate.md)
  Date of the next payment.
- [let overduePaymentAmount: CurrencyAmount?](accountcreditinformation/overduepaymentamount.md)
  The amount by which the account is overdue for the current period.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/accountcreditinformation)*