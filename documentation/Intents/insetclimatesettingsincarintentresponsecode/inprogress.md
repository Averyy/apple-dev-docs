# INSetClimateSettingsInCarIntentResponseCode.inProgress

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You’re in the process of handling the intent.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
case inProgress
```

```c
INSetClimateSettingsInCarIntentResponseCodeInProgress
```

## Discussion

Use this code during the handling phase to indicate that you received the climate control settings and initiated the changes, but you haven’t yet received confirmation of the completed changes.

## See Also

### Constants
- [INSetClimateSettingsInCarIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a resonse code.
- [INSetClimateSettingsInCarIntentResponseCode.ready](./ready.md)
  You’re ready to handle the intent.
- [INSetClimateSettingsInCarIntentResponseCode.success](./success.md)
  You successfully handled the intent.
- [INSetClimateSettingsInCarIntentResponseCode.failure](./failure.md)
  You were unable to change the climate control settings.
- [INSetClimateSettingsInCarIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to change the climate control settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetclimatesettingsincarintentresponsecode/inprogress)*