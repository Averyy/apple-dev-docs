# transferFee

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The fee charged for performing the transaction.

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
var transferFee: INCurrencyAmount? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) INCurrencyAmount * transferFee;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) INCurrencyAmount * transferFee;
```

#### Discussion

If there’s a fee for performing the transfer, put the fee amount in this property.

## See Also

### Providing the Transaction Details
- [var transactionAmount: INPaymentAmount?](./transactionamount.md)
  The amount of money to transfer between accounts.
- [var transactionScheduledDate: INDateComponentsRange?](./transactionscheduleddate.md)
  The date on which the transfer is to occur.
- [var transactionNote: String?](./transactionnote.md)
  Notes to include with the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intransfermoneyintentresponse/transferfee)*