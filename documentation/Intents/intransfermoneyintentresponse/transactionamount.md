# transactionAmount

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The amount of money to transfer between accounts.

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

#### Discussion

Use this property to specify the precise amount to transfer between the user’s accounts. During confirmation or at other appropriate times, Siri may display this value to the user.

## See Also

### Providing the Transaction Details
- [var transactionScheduledDate: INDateComponentsRange?](./transactionscheduleddate.md)
  The date on which the transfer is to occur.
- [var transactionNote: String?](./transactionnote.md)
  Notes to include with the transaction.
- [var transferFee: INCurrencyAmount?](./transferfee.md)
  The fee charged for performing the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intransfermoneyintentresponse/transactionamount)*