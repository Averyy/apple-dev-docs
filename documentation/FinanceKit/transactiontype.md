# TransactionType

**Framework**: FinanceKit  
**Kind**: enum  
**Role**: Enumeration

Values that describe kinds of transactions.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
enum TransactionType
```

## Topics

### Enumeration Cases
- [TransactionType.adjustment](./transactiontype/adjustment.md)
  A credit or debit adjustment transaction.
- [TransactionType.atm](./transactiontype/atm.md)
  An ATM  transaction.
- [TransactionType.billPayment](./transactiontype/billpayment.md)
  A bill payment, usually carried out through an eBill or eCheck system.
- [TransactionType.check](./transactiontype/check.md)
  A check  payment.
- [TransactionType.deposit](./transactiontype/deposit.md)
  A deposit of money by a payer into a payee’s bank account.
- [TransactionType.directDebit](./transactiontype/directdebit.md)
  A payment to a third party on agreed dates, typically in order to pay bills.
- [TransactionType.directDeposit](./transactiontype/directdeposit.md)
  A deposit of money by a payer directly into a payee’s bank account.
- [TransactionType.dividend](./transactiontype/dividend.md)
  A distribution of a company’s earnings to its shareholders.
- [TransactionType.fee](./transactiontype/fee.md)
  A fee or charge levied by the account provider.
- [TransactionType.interest](./transactiontype/interest.md)
  A credit or debit due to interest earned or incurred.
- [TransactionType.loan](./transactiontype/loan.md)
  A loan drawdown or repayment.
- [TransactionType.pointOfSale](./transactiontype/pointofsale.md)
  A Point of Sales transaction.
- [TransactionType.refund](./transactiontype/refund.md)
  A refund.
- [TransactionType.standingOrder](./transactiontype/standingorder.md)
  A regular payment of a fixed amount that’s paid on a specified date.
- [TransactionType.transfer](./transactiontype/transfer.md)
  A transfer between accounts.
- [TransactionType.unknown](./transactiontype/unknown.md)
  The transaction’s category doesn’t map to a known value.
- [TransactionType.withdrawal](./transactiontype/withdrawal.md)
  An automatic or recurring withdrawal of funds by another party.

## Relationships

### Conforms To
- [CaseIterable](../Swift/caseiterable.md)
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Transactions
- [func transactionHistory(forAccountID: UUID, since: FinanceStore.HistoryToken?, isMonitoring: Bool) -> FinanceStore.History<Transaction>](./financestore/transactionhistory%28foraccountid,since,ismonitoring%29.md)
  Returns the transactions for the specified account ID, optional starting time, and monitoring indicator for long running transaction queries.
- [func transactions(query: TransactionQuery) async throws -> [Transaction]](./financestore/transactions%28query%29.md)
  Returns transactions that match the provided transaction query.
- [struct AccountQuery](./accountquery.md)
  A structure that defines an account query.
- [struct AccountCreditInformation](./accountcreditinformation.md)
  A structure that describes the credit information associated with an account.
- [struct CurrencyAmount](./currencyamount.md)
  A structure that describes a monetary amount and its currency.
- [struct Transaction](./transaction.md)
  A structure that represents a transaction relating to a specific financial account.
- [struct TransactionQuery](./transactionquery.md)
  A structure that describes the parameters to use for a transaction query.
- [enum TransactionStatus](./transactionstatus.md)
  Values that describe the status of a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/transactiontype)*