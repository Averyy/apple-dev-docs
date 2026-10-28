# INTransferMoneyIntentResponseCode.inProgress

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You’ve received the transaction details but haven’t yet scheduled the transaction.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
case inProgress
```

```c
INTransferMoneyIntentResponseCodeInProgress
```

## Discussion

Use this code during the handling phase to indicate that you received the transaction details, but haven’tt yet scheduled it. You might use this code when scheduling the transaction requires communicating with your server and you’ve not yet received a confirmation from that server.

When handling an intent, you might want to first configure a timer to fire if your server doesn’t return within a few seconds. Use your timer’s handler block to provide the in-progress response back to Siri.

## See Also

### Constants
- [INTransferMoneyIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a response code.
- [INTransferMoneyIntentResponseCode.ready](./ready.md)
  You’re ready to handle the intent.
- [INTransferMoneyIntentResponseCode.success](./success.md)
  You successfully scheduled the transaction.
- [INTransferMoneyIntentResponseCode.failure](./failure.md)
  You were unable to schedule the transaction.
- [INTransferMoneyIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to schedule the transaction.
- [INTransferMoneyIntentResponseCode.failureCredentialsUnverified](./failurecredentialsunverified.md)
  The transaction failed because you were unable to verify the user’s credentials.
- [INTransferMoneyIntentResponseCode.failureInsufficientFunds](./failureinsufficientfunds.md)
  The transaction failed because the user’s account didn’t contain sufficient funds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intransfermoneyintentresponsecode/inprogress)*