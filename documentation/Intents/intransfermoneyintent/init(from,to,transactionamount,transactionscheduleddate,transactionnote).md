# init(from:to:transactionAmount:transactionScheduledDate:transactionNote:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the intent object with the specified transaction details.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
init(from fromAccount: INPaymentAccount?, to toAccount: INPaymentAccount?, transactionAmount: INPaymentAmount?, transactionScheduledDate: INDateComponentsRange?, transactionNote: String?)
```

```objc
- (instancetype) initWithFromAccount:(INPaymentAccount *) fromAccount toAccount:(INPaymentAccount *) toAccount transactionAmount:(INPaymentAmount *) transactionAmount transactionScheduledDate:(INDateComponentsRange *) transactionScheduledDate transactionNote:(NSString *) transactionNote;
```

#### Return Value

An initialized intent object or `nil` if the object could not be created.

#### Discussion

Normally, you don’t create instances of this class yourself. Instead, SiriKit creates instances when the user asks to transfer money between accounts. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `fromAccount`: The account containing the funds to transfer.
- `toAccount`: The account to receive the funds.
- `transactionAmount`: The amount of money to transfer between the accounts. When transferring money between accounts, you typically specify a fixed amount of money to transfer.
- `transactionScheduledDate`: The date on which to transfer the money.
- `transactionNote`: An optional note to include with the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intransfermoneyintent/init(from:to:transactionamount:transactionscheduleddate:transactionnote:))*