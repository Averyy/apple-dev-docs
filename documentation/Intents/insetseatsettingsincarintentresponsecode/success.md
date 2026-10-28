# INSetSeatSettingsInCarIntentResponseCode.success

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You successfully handled the intent.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
case success
```

```c
INSetSeatSettingsInCarIntentResponseCodeSuccess
```

## Discussion

Use this code if your app successfully changed the seat settings to the new values.

## See Also

### Constants
- [INSetSeatSettingsInCarIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a resonse code.
- [INSetSeatSettingsInCarIntentResponseCode.ready](./ready.md)
  You’re ready to handle the intent.
- [INSetSeatSettingsInCarIntentResponseCode.inProgress](./inprogress.md)
  You’re in the process of handling the intent.
- [INSetSeatSettingsInCarIntentResponseCode.failure](./failure.md)
  You were unable to change the seat settings.
- [INSetSeatSettingsInCarIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to change the seat settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetseatsettingsincarintentresponsecode/success)*