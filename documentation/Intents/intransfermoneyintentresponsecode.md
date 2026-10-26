# INTransferMoneyIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the state of the response.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
enum INTransferMoneyIntentResponseCode
```

```c
enum INTransferMoneyIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INTransferMoneyIntentResponseCode.unspecified](./intransfermoneyintentresponsecode/unspecified.md)
  The response didn’t specify a response code.
- [INTransferMoneyIntentResponseCode.ready](./intransfermoneyintentresponsecode/ready.md)
  You’re ready to handle the intent.
- [INTransferMoneyIntentResponseCode.inProgress](./intransfermoneyintentresponsecode/inprogress.md)
  You’ve received the transaction details but haven’t yet scheduled the transaction.
- [INTransferMoneyIntentResponseCode.success](./intransfermoneyintentresponsecode/success.md)
  You successfully scheduled the transaction.
- [INTransferMoneyIntentResponseCode.failure](./intransfermoneyintentresponsecode/failure.md)
  You were unable to schedule the transaction.
- [INTransferMoneyIntentResponseCode.failureRequiringAppLaunch](./intransfermoneyintentresponsecode/failurerequiringapplaunch.md)
  The user must launch your app to schedule the transaction.
- [INTransferMoneyIntentResponseCode.failureCredentialsUnverified](./intransfermoneyintentresponsecode/failurecredentialsunverified.md)
  The transaction failed because you were unable to verify the user’s credentials.
- [INTransferMoneyIntentResponseCode.failureInsufficientFunds](./intransfermoneyintentresponsecode/failureinsufficientfunds.md)
  The transaction failed because the user’s account didn’t contain sufficient funds.
### Initializers
- [init?(rawValue: Int)](./intransfermoneyintentresponsecode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Response Code
- [var code: INTransferMoneyIntentResponseCode](./intransfermoneyintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intransfermoneyintentresponsecode)*