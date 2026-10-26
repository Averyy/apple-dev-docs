# INPayBillIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the state of the response.

**Availability**:
- iOS 10.3+ - Deprecated in 15.0
- iPadOS 10.3+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
enum INPayBillIntentResponseCode
```

```c
enum INPayBillIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INPayBillIntentResponseCode.unspecified](./inpaybillintentresponsecode/unspecified.md)
  The response didn’t specify a response code.
- [INPayBillIntentResponseCode.ready](./inpaybillintentresponsecode/ready.md)
  You’re ready to handle the intent.
- [INPayBillIntentResponseCode.inProgress](./inpaybillintentresponsecode/inprogress.md)
  You’ve received the payment details and are in the process of scheduling the transaction.
- [INPayBillIntentResponseCode.success](./inpaybillintentresponsecode/success.md)
  You successfully scheduled the transaction.
- [INPayBillIntentResponseCode.failure](./inpaybillintentresponsecode/failure.md)
  You were unable to schedule the transaction.
- [INPayBillIntentResponseCode.failureRequiringAppLaunch](./inpaybillintentresponsecode/failurerequiringapplaunch.md)
  The user must launch your app to schedule the transaction.
- [INPayBillIntentResponseCode.failureCredentialsUnverified](./inpaybillintentresponsecode/failurecredentialsunverified.md)
  The transaction failed because you were unable to verify the credentials of the user or the payee.
- [INPayBillIntentResponseCode.failureInsufficientFunds](./inpaybillintentresponsecode/failureinsufficientfunds.md)
  The transaction failed because the user’s account didn’t contain sufficient funds.
### Initializers
- [init?(rawValue: Int)](./inpaybillintentresponsecode/init%28rawvalue%29.md)

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
- [var code: INPayBillIntentResponseCode](./inpaybillintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaybillintentresponsecode)*