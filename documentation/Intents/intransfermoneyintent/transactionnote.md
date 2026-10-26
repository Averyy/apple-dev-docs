# transactionNote

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

An optional note associated with the transaction.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
var transactionNote: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * transactionNote;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * transactionNote;
```

## See Also

### Getting the Transaction Details
- [var transactionAmount: INPaymentAmount?](./transactionamount.md)
  The amount to transfer.
- [var transactionScheduledDate: INDateComponentsRange?](./transactionscheduleddate.md)
  The date on which to transfer the funds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intransfermoneyintent/transactionnote)*