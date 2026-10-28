# INPayBillIntentResponseCode.success

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You successfully scheduled the transaction.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
case success
```

```c
INPayBillIntentResponseCodeSuccess
```

## Discussion

Use this code after scheduling the transaction successfully. Returning this code doesn’t requirea transfer of funds. It only means that you’ve recorded the transaction are making the payment on the date specified in the intent object.

## See Also

### Constants
- [INPayBillIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a response code.
- [INPayBillIntentResponseCode.ready](./ready.md)
  You’re ready to handle the intent.
- [INPayBillIntentResponseCode.inProgress](./inprogress.md)
  You’ve received the payment details and are in the process of scheduling the transaction.
- [INPayBillIntentResponseCode.failure](./failure.md)
  You were unable to schedule the transaction.
- [INPayBillIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to schedule the transaction.
- [INPayBillIntentResponseCode.failureCredentialsUnverified](./failurecredentialsunverified.md)
  The transaction failed because you were unable to verify the credentials of the user or the payee.
- [INPayBillIntentResponseCode.failureInsufficientFunds](./failureinsufficientfunds.md)
  The transaction failed because the user’s account didn’t contain sufficient funds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaybillintentresponsecode/success)*