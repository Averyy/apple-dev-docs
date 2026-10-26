# transactionNote

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

Notes to include with the transaction.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var transactionNote: String? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readwrite, nullable) NSString * transactionNote;
```

*macOS*

```objc
@property (atomic, copy, readwrite, nullable) NSString * transactionNote;
```

#### Discussion

Use this property to specify any notes to include with the transaction. If the intent object contained transaction notes, you typically copy those notes over into this property.

## See Also

### Providing the Transaction Details
- [var transactionAmount: INPaymentAmount?](./transactionamount.md)
  The amount of money to transfer between accounts.
- [var transactionScheduledDate: INDateComponentsRange?](./transactionscheduleddate.md)
  The date on which the transfer is to occur.
- [var transferFee: INCurrencyAmount?](./transferfee.md)
  The fee charged for performing the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intransfermoneyintentresponse/transactionnote)*