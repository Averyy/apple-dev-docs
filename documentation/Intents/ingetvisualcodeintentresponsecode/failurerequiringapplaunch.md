# INGetVisualCodeIntentResponseCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user must launch your app to request the visual code.

**Availability**:
- iOS 11.0+ - Deprecated in 15.0
- iPadOS 11.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 4.0+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
case failureRequiringAppLaunch
```

```c
INGetVisualCodeIntentResponseCodeFailureRequiringAppLaunch
```

## Discussion

Use this response code when you can’t generate the visual code until the user provides additional information in your app. Don’t use this code for general errors or to force the user to launch your app.

## See Also

### Constants
- [INGetVisualCodeIntentResponseCode.unspecified](./unspecified.md)
  The response didnt specify a code.
- [INGetVisualCodeIntentResponseCode.ready](./ready.md)
  You’re ready to handle the intent.
- [INGetVisualCodeIntentResponseCode.continueInApp](./continueinapp.md)
  You must launch the app to display the visual code.
- [INGetVisualCodeIntentResponseCode.inProgress](./inprogress.md)
  You’re in the process of generating the code but aren’t yet finished.
- [INGetVisualCodeIntentResponseCode.success](./success.md)
  You successfully generated the visual code.
- [INGetVisualCodeIntentResponseCode.failure](./failure.md)
  You were unable to generate the visual code.
- [INGetVisualCodeIntentResponseCode.failureAppConfigurationRequired](./failureappconfigurationrequired.md)
  Your app wasn’t configured to display visual codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetvisualcodeintentresponsecode/failurerequiringapplaunch)*