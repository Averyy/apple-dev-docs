# transactionType

**Framework**: FinanceKit  
**Kind**: property  
**Role**: Instance Property

The type of the transaction.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
let transactionType: TransactionType
```

#### Discussion

This value describes the specific kind of transaction, such as a purchase, a bill, a funds transfer, and so on. The transaction type may not always be available.

## See Also

### Instance Properties
- [let accountID: UUID](./accountid.md)
  The account ID the transaction belongs to.
- [let creditDebitIndicator: CreditDebitIndicator](./creditdebitindicator.md)
  An indicator that describes if the transaction is a credit or a debit.
- [let foreignCurrencyAmount: CurrencyAmount?](./foreigncurrencyamount.md)
  The total amount of the transaction, if it was carried out in a foreign currency.
- [let foreignCurrencyExchangeRate: Decimal?](./foreigncurrencyexchangerate.md)
  The currency exchange rate, if the transaction was carried out in a foreign currency.
- [let id: UUID](./id.md)
  A unique internal ID.
- [let merchantCategoryCode: MerchantCategoryCode?](./merchantcategorycode.md)
  The ISO 18245 category code for the transaction.
- [let merchantName: String?](./merchantname.md)
  The name of the merchant, if present.
- [let originalTransactionDescription: String](./originaltransactiondescription.md)
  The unmodified description of the transaction.
- [let postedDate: Date?](./posteddate.md)
  The date and time that the transaction was posted to the account.
- [let status: TransactionStatus](./status.md)
  The status of the transaction, if available.
- [let transactionAmount: CurrencyAmount](./transactionamount.md)
  The total amount of the transaction.
- [let transactionDate: Date](./transactiondate.md)
  The time the transaction took place, if available.
- [let transactionDescription: String](./transactiondescription.md)
  A description of the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/transaction/transactiontype)*