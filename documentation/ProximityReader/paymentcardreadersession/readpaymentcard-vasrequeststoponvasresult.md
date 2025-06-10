# readPaymentCard(_:vasRequest:stopOnVASResult:)

**Framework**: ProximityReader  
**Kind**: method

Presents a sheet to read both contactless payments and loyalty cards for a purchase or refund, and returns the relevant card data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 17.0+

## Declaration

```swift
func readPaymentCard(_ request: PaymentCardTransactionRequest, vasRequest: VASRequest, stopOnVASResult: Bool) async throws -> (PaymentCardReadResult?, VASReadResult?)
```

## Mentions

- [Accepting loyalty passes from Wallet](accepting-loyalty-passes-from-wallet.md)

#### Return Value

Either [`PaymentCardReadResult`](paymentcardreadresult.md), [`VASReadResult`](vasreadresult.md), or both when the read operation was successful.

#### Discussion

Call this method to read either a contactless payment card or a loyalty card. This method displays a system sheet with instructions on what the person needs to do. The system UI remains onscreen until the system reads the person’s card, you cancel the operation, or an error occurs. If it reads a card successfully, the method returns the card information as a result.

When the `stopOnVasResult` parameter is `true`:

- If the customer taps their loyalty card while the UI is present, the system closes the sheet and returns [`VASReadResult`](vasreadresult.md) as a result.
- If the customer taps their payment card while the UI is present, the system closes the sheet and returns [`PaymentCardReadResult`](paymentcardreadresult.md) as a result.

When the `stopOnVasResult` parameter is `false`:

- If the customer taps their Apple Pay Wallet, containing both a relevant loyalty card and a payment card, the system closes the sheet and returns both [`PaymentCardReadResult`](paymentcardreadresult.md) and [`VASReadResult`](vasreadresult.md) as a result.
- If the customer taps their Apple Pay Wallet, containing only a relevant loyalty card, the system closes the sheet and returns [`VASReadResult`](vasreadresult.md) as a result.
- If the customer taps their payment card, the system closes the sheet and returns [`PaymentCardReadResult`](paymentcardreadresult.md) as a result.

> **Note**: This method throws a [`PaymentCardReaderSession.ReadError`](paymentcardreadersession/readerror.md) if a person dismisses the sheet or the sheet fails to appear.

## Parameters

- `request`: The transaction object you provide with the payment amount and currency details.
- `vasRequest`: The object that you use to specify the loyalty card request details,   such as the list of supported merchants.
- `stopOnVASResult`: A Boolean that indicates what type of result to return. See the discussion for details of how this parameter affects the return value.

## See Also

- [func readVAS(VASRequest) async throws -> VASReadResult](paymentcardreadersession/readvas(_:).md)
  Presents a sheet to read a loyalty card for Value Added Services (VAS), and returns the loyalty card data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/paymentcardreadersession/readpaymentcard(_:vasrequest:stoponvasresult:))*