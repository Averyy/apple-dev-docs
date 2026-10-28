# transactionAmount

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The amount to transfer from the user to the payee.

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
var transactionAmount: INPaymentAmount? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) INPaymentAmount * transactionAmount;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) INPaymentAmount * transactionAmount;
```

## Discussion

Use this property to determine how much money to transfer out of the user’s account and apply to the payment. Payment amounts may reflect a specific monetary amount or may indicate that the user should pay all or a portion of the bill. When resolving the transaction amount, always provide as much detail as you can. For example, if the user asked to pay the minimum amount of a credit card bill, your resolution should also contain the precise amount of money to pay.

## See Also

### Getting the Transaction Details
- [var fromAccount: INPaymentAccount?](./fromaccount.md)
  The user account containing the funds for the payment.
- [var transactionNote: String?](./transactionnote.md)
  A note to associate with the payment transaction.
- [var transactionScheduledDate: INDateComponentsRange?](./transactionscheduleddate.md)
  The scheduled date for the payment, as requested by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaybillintent/transactionamount)*