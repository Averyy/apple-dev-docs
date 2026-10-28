# INSetProfileInCarIntentResponseCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user must launch your app to restore information from a profile.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
case failureRequiringAppLaunch
```

```c
INSetProfileInCarIntentResponseCodeFailureRequiringAppLaunch
```

## Discussion

Use this response code when you can’t handle the request through Siri for a reason not covered by any other response code. Don’t use it for general errors or to force the user to launch your app.

## See Also

### Constants
- [INSetProfileInCarIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a response code.
- [INSetProfileInCarIntentResponseCode.ready](./ready.md)
  You’re ready to handle the intent.
- [INSetProfileInCarIntentResponseCode.inProgress](./inprogress.md)
  You’re in the process of handling the intent.
- [INSetProfileInCarIntentResponseCode.success](./success.md)
  You successfully handled the intent.
- [INSetProfileInCarIntentResponseCode.failure](./failure.md)
  You were unable to restore the information from the designated profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetprofileincarintentresponsecode/failurerequiringapplaunch)*