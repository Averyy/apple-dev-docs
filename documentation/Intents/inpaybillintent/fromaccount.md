# fromAccount

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The user account containing the funds for the payment.

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
var fromAccount: INPaymentAccount? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INPaymentAccount * fromAccount;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INPaymentAccount * fromAccount;
```

## Discussion

Use this property to determine which account is the source of funds for the payment.

## See Also

### Getting the Transaction Details
- [var transactionAmount: INPaymentAmount?](./transactionamount.md)
  The amount to transfer from the user to the payee.
- [var transactionNote: String?](./transactionnote.md)
  A note to associate with the payment transaction.
- [var transactionScheduledDate: INDateComponentsRange?](./transactionscheduleddate.md)
  The scheduled date for the payment, as requested by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaybillintent/fromaccount)*