# INSetRadioStationIntentResponseCode.failureNotSubscribed

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You were unable to change the radio station because the user doesn’t have a subscription to the corresponding service.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
case failureNotSubscribed
```

```c
INSetRadioStationIntentResponseCodeFailureNotSubscribed
```

## Discussion

For example, use this code if the user selects a satellite radio station but doesn’t subscribe to the satellite service.

## See Also

### Constants
- [INSetRadioStationIntentResponseCode.unspecified](./unspecified.md)
  The response didn’t specify a resonse code.
- [INSetRadioStationIntentResponseCode.ready](./ready.md)
  You’re ready to handle the intent.
- [INSetRadioStationIntentResponseCode.inProgress](./inprogress.md)
  You’re in the process of handling the intent.
- [INSetRadioStationIntentResponseCode.success](./success.md)
  You successfully handled the intent.
- [INSetRadioStationIntentResponseCode.failure](./failure.md)
  You were unable to change the radio station.
- [INSetRadioStationIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to change the radio station.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetradiostationintentresponsecode/failurenotsubscribed)*