# INSetMessageAttributeIntentResponseCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user must launch your app to modify the messages.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
case failureRequiringAppLaunch
```

```c
INSetMessageAttributeIntentResponseCodeFailureRequiringAppLaunch
```

## Discussion

Use this response code when you cannot handle the request through Siri for a reason not covered by any other response code. For example, you might use this code if the user has not set up an account with your app. Do not use it for general errors or to force the user to launch your app.

## See Also

### Response State
- [INSetMessageAttributeIntentResponseCode.unspecified](./unspecified.md)
  An unknown response code.
- [INSetMessageAttributeIntentResponseCode.ready](./ready.md)
  The app is ready to handle the intent.
- [INSetMessageAttributeIntentResponseCode.inProgress](./inprogress.md)
  You are ready to handle the intent.
- [INSetMessageAttributeIntentResponseCode.success](./success.md)
  You successfully handled the intent.
- [INSetMessageAttributeIntentResponseCode.failure](./failure.md)
  You are unable to modify the messages.
- [INSetMessageAttributeIntentResponseCode.failureMessageNotFound](./failuremessagenotfound.md)
  One or more of the specified messages were not found.
- [INSetMessageAttributeIntentResponseCode.failureMessageAttributeNotSet](./failuremessageattributenotset.md)
  The message attributes couldn’t be modified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetmessageattributeintentresponsecode/failurerequiringapplaunch)*