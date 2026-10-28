# INSaveProfileInCarIntentResponseCode.failure

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You were unable to save the information to the designated profile.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
case failure
```

```c
INSaveProfileInCarIntentResponseCodeFailure
```

## Discussion

Use this code for both transient and unrecoverable errors that prevented you from saving the settings.

## See Also

### Constants
- [INSaveProfileInCarIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a resonse code.
- [INSaveProfileInCarIntentResponseCode.ready](./ready.md)
  You’re ready to handle the intent.
- [INSaveProfileInCarIntentResponseCode.inProgress](./inprogress.md)
  You’re in the process of handling the intent.
- [INSaveProfileInCarIntentResponseCode.success](./success.md)
  You successfully handled the intent.
- [INSaveProfileInCarIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to save information to a profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insaveprofileincarintentresponsecode/failure)*