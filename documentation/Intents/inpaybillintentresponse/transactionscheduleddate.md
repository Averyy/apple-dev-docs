# transactionScheduledDate

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The date on which the transaction is to occur.

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
var transactionScheduledDate: INDateComponentsRange? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INDateComponentsRange * transactionScheduledDate;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INDateComponentsRange * transactionScheduledDate;
```

## Discussion

Use this property to specify the window of time during to transfer funds from the user’s account to the designated payee. The end date of the specified range must always be in the future. Be as specific as you can when specifying the transaction dates to assure the user of on time payment of the bill.

## See Also

### Providing the Transaction Details
- [var billDetails: INBillDetails?](./billdetails.md)
  The details of the bill to pay.
- [var transactionAmount: INPaymentAmount?](./transactionamount.md)
  The amount of money to transfer to the payee.
- [var transactionNote: String?](./transactionnote.md)
  Notes to include with the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaybillintentresponse/transactionscheduleddate)*