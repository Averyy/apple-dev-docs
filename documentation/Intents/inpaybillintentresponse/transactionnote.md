# transactionNote

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

Notes to include with the transaction.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

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
- [var billDetails: INBillDetails?](./billdetails.md)
  The details of the bill to pay.
- [var transactionAmount: INPaymentAmount?](./transactionamount.md)
  The amount of money to transfer to the payee.
- [var transactionScheduledDate: INDateComponentsRange?](./transactionscheduleddate.md)
  The date on which the transaction is to occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaybillintentresponse/transactionnote)*