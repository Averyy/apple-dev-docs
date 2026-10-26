# INSetAudioSourceInCarIntentResponseCode.ready

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You’re ready to handle the intent.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
case ready
```

```c
INSetAudioSourceInCarIntentResponseCodeReady
```

#### Discussion

During the confirmation phase of an intent, use this code to signal that your app is ready and able to act on the intent.

## See Also

### Constants
- [INSetAudioSourceInCarIntentResponseCode.unspecified](./unspecified.md)
  A response code indicating that the status isn’t specified.
- [INSetAudioSourceInCarIntentResponseCode.inProgress](./inprogress.md)
  You’re in the process of handling the intent.
- [INSetAudioSourceInCarIntentResponseCode.success](./success.md)
  You successfully handled the intent.
- [INSetAudioSourceInCarIntentResponseCode.failure](./failure.md)
  You were unable to change the audio source.
- [INSetAudioSourceInCarIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to change the audio source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetaudiosourceincarintentresponsecode/ready)*