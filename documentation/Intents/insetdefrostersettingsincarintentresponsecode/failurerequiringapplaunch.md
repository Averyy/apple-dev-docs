# INSetDefrosterSettingsInCarIntentResponseCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user must launch your app to change the defroster setting.

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
INSetDefrosterSettingsInCarIntentResponseCodeFailureRequiringAppLaunch
```

#### Discussion

Use this response code when you can’t handle the request through Siri for a reason not covered by any other response code. Don’t use it for general errors or to force the user to launch your app.

## See Also

### Constants
- [INSetDefrosterSettingsInCarIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a resonse code.
- [INSetDefrosterSettingsInCarIntentResponseCode.ready](./ready.md)
  You’re ready to handle the intent.
- [INSetDefrosterSettingsInCarIntentResponseCode.inProgress](./inprogress.md)
  You’re in the process of handling the intent.
- [INSetDefrosterSettingsInCarIntentResponseCode.success](./success.md)
  You successfully handled the intent.
- [INSetDefrosterSettingsInCarIntentResponseCode.failure](./failure.md)
  You were unable to change the defroster settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetdefrostersettingsincarintentresponsecode/failurerequiringapplaunch)*