# PaymentCardTransactionRequest

**Framework**: ProximityReader  
**Kind**: struct

A request for a contactless purchase or refund that includes the purchase amount and currency information.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 17.0+

## Declaration

```swift
struct PaymentCardTransactionRequest
```

## Mentions

- [Adding support for Tap to Pay on iPhone to your app](adding-support-for-tap-to-pay-on-iphone-to-your-app.md)

#### Overview

Create a `PaymentCardTransactionRequest` to specify the amount of a purchase or refund. After you create this object, pass it to the [`readPaymentCard(_:)`](paymentcardreadersession/readpaymentcard(_:)-8jol5.md) or [`readPaymentCard(_:vasRequest:stopOnVASResult:)`](paymentcardreadersession/readpaymentcard(_:vasrequest:stoponvasresult:).md) method of [`PaymentCardReaderSession`](paymentcardreadersession.md) to read the card associated with the transaction.

## Topics

### Creating a transaction request
- [init(amount: Decimal, currencyCode: String, for: PaymentCardTransactionRequest.TransactionType)](paymentcardtransactionrequest/init(amount:currencycode:for:).md)
  Creates a new transaction request for the specified amount in the designated currency.
### Getting the transaction details
- [let amount: Decimal](paymentcardtransactionrequest/amount.md)
  The amount of the purchase or refund in the specified currency.
- [let currencyCode: String](paymentcardtransactionrequest/currencycode.md)
  The ISO 4217 code that indicates the currency type.
- [let type: PaymentCardTransactionRequest.TransactionType](paymentcardtransactionrequest/type.md)
  The type of transaction, either a purchase or a refund.
- [PaymentCardTransactionRequest.TransactionType](paymentcardtransactionrequest/transactiontype.md)
  The type of transaction to perform.
- [var transactionDescription: PaymentCardTransactionRequest.TransactionAmountDescription?](paymentcardtransactionrequest/transactiondescription.md)
  An optional description of the current transaction meant to provide more context, such as a recurring payment being setup or a surcharge applied.
- [PaymentCardTransactionRequest.TransactionAmountDescription](paymentcardtransactionrequest/transactionamountdescription.md)
  Values that provide additional information about the transaction amount.
### Setting the preferred Application Identifier (AID) list
- [var preferredAIDList: [Data]](paymentcardtransactionrequest/preferredaidlist.md)
  The preferred Application Identifier (AID) or Registered Application Provider Identifier (RID).
### Setting the user interface language
- [var userInterfaceLanguage: Locale.Language?](paymentcardtransactionrequest/userinterfacelanguage.md)
  The language the framework uses when localizing the user interface.
### Instance Properties
- [var useISOCurrencySymbol: Bool](paymentcardtransactionrequest/useisocurrencysymbol.md)
  A boolean value that sets the system UI’s currency symbol to ISO 4217 three-letter code.
### Enumerations
- [PaymentCardTransactionRequest.PaymentCycle](paymentcardtransactionrequest/paymentcycle.md)
  Values that specify the frequency of payments

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct PaymentCardVerificationRequest](paymentcardverificationrequest.md)
  A request to verify details for a contactless payment card.
- [struct PaymentCardReadResult](paymentcardreadresult.md)
  The result of a payment card read operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardtransactionrequest)*