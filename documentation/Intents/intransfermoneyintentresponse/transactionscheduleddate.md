# transactionScheduledDate

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The date on which the transfer is to occur.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

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

#### Discussion

Use this property to specify the window of time during which to transfer the funds between the accounts. The end date of the specified range must always be in the future. Be as specific as you can when specifying the transaction dates.

## See Also

### Providing the Transaction Details
- [var transactionAmount: INPaymentAmount?](./transactionamount.md)
  The amount of money to transfer between accounts.
- [var transactionNote: String?](./transactionnote.md)
  Notes to include with the transaction.
- [var transferFee: INCurrencyAmount?](./transferfee.md)
  The fee charged for performing the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intransfermoneyintentresponse/transactionscheduleddate)*