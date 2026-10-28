# transactionAmount

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The amount of money to transfer to the payee.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
@NSCopying
var transactionAmount: INPaymentAmount? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INPaymentAmount * transactionAmount;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INPaymentAmount * transactionAmount;
```

## Discussion

Use this property to specify how much to debit from the user’s account and apply to the bill payment. Always specify the precise amount to transfer and not just a constant indicating that the user wants to pay the current balance or the minimum due. For example, you might create an [`INPaymentAmount`](../inpaymentamount.md) object that indicates the minimum amount is $25. During confirmation or at other appropriate times, Siri may display the precise amount to the user.

## See Also

### Providing the Transaction Details
- [var billDetails: INBillDetails?](./billdetails.md)
  The details of the bill to pay.
- [var transactionScheduledDate: INDateComponentsRange?](./transactionscheduleddate.md)
  The date on which the transaction is to occur.
- [var transactionNote: String?](./transactionnote.md)
  Notes to include with the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaybillintentresponse/transactionamount)*