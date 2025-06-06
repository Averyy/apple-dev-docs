# Transaction

**Framework**: FinanceKit  
**Kind**: struct

A structure that represents a transaction relating to a specific financial account.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct Transaction
```

#### Overview

This can include transactions such as a deposit to or a withdrawn from bank account, a credit card transaction.

## Topics

### Operators
- [static func == (Transaction, Transaction) -> Bool](transaction/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](transaction/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [let accountID: UUID](transaction/accountid.md)
  The account ID the transaction belongs to.
- [let creditDebitIndicator: CreditDebitIndicator](transaction/creditdebitindicator.md)
  An indicator that describes if the transaction is a credit or a debit.
- [let foreignCurrencyAmount: CurrencyAmount?](transaction/foreigncurrencyamount.md)
  The total amount of the transaction, if it was carried out in a foreign currency.
- [let foreignCurrencyExchangeRate: Decimal?](transaction/foreigncurrencyexchangerate.md)
  The currency exchange rate, if the transaction was carried out in a foreign currency.
- [let id: UUID](transaction/id-swift.property.md)
  A unique internal ID.
- [let merchantCategoryCode: MerchantCategoryCode?](transaction/merchantcategorycode.md)
  The ISO 18245 category code for the transaction.
- [let merchantName: String?](transaction/merchantname.md)
  The name of the merchant, if present.
- [let originalTransactionDescription: String](transaction/originaltransactiondescription.md)
  The unmodified description of the transaction.
- [let postedDate: Date?](transaction/posteddate.md)
  The date and time that the transaction was posted to the account.
- [let status: TransactionStatus](transaction/status.md)
  The status of the transaction, if available.
- [let transactionAmount: CurrencyAmount](transaction/transactionamount.md)
  The total amount of the transaction.
- [let transactionDate: Date](transaction/transactiondate.md)
  The time the transaction took place, if available.
- [let transactionDescription: String](transaction/transactiondescription.md)
  A description of the transaction.
- [let transactionType: TransactionType](transaction/transactiontype.md)
  The type of the transaction.
### Instance Methods
- [func encode(to: any Encoder) throws](transaction/encode(to:).md)
  Encodes this value into the given encoder.
### Type Aliases
- [Transaction.ID](transaction/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.
### Default Implementations
- [Equatable Implementations](transaction/equatable-implementations.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
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
- [struct TransactionQuery](transactionquery.md)
  A structure that describes the parameters to use for a transaction query.
- [enum TransactionType](transactiontype.md)
  Values that describe kinds of transactions.
- [enum TransactionStatus](transactionstatus.md)
  Values that describe the status of a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/transaction)*