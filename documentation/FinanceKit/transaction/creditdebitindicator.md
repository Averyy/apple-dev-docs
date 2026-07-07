# creditDebitIndicator

**Framework**: FinanceKit  
**Kind**: property

An indicator that describes if the transaction is a credit or a debit.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
let creditDebitIndicator: CreditDebitIndicator
```

## See Also

- [let accountID: UUID](transaction/accountid.md)
  The account ID the transaction belongs to.
- [let foreignCurrencyAmount: CurrencyAmount?](transaction/foreigncurrencyamount.md)
  The total amount of the transaction, if it was carried out in a foreign currency.
- [let foreignCurrencyExchangeRate: Decimal?](transaction/foreigncurrencyexchangerate.md)
  The currency exchange rate, if the transaction was carried out in a foreign currency.
- [let id: UUID](transaction/id.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/transaction/creditdebitindicator)*