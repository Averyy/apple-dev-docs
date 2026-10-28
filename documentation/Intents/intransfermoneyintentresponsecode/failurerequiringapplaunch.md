# INTransferMoneyIntentResponseCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user must launch your app to schedule the transaction.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
case failureRequiringAppLaunch
```

```c
INTransferMoneyIntentResponseCodeFailureRequiringAppLaunch
```

## Discussion

Use this response code when you require additional information that you can only obtain from your app. Don’t use this code for general errors or to force the user to launch your app.

## See Also

### Constants
- [INTransferMoneyIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a response code.
- [INTransferMoneyIntentResponseCode.ready](./ready.md)
  You’re ready to handle the intent.
- [INTransferMoneyIntentResponseCode.inProgress](./inprogress.md)
  You’ve received the transaction details but haven’t yet scheduled the transaction.
- [INTransferMoneyIntentResponseCode.success](./success.md)
  You successfully scheduled the transaction.
- [INTransferMoneyIntentResponseCode.failure](./failure.md)
  You were unable to schedule the transaction.
- [INTransferMoneyIntentResponseCode.failureCredentialsUnverified](./failurecredentialsunverified.md)
  The transaction failed because you were unable to verify the user’s credentials.
- [INTransferMoneyIntentResponseCode.failureInsufficientFunds](./failureinsufficientfunds.md)
  The transaction failed because the user’s account didn’t contain sufficient funds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intransfermoneyintentresponsecode/failurerequiringapplaunch)*