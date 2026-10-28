# INStartPhotoPlaybackIntentResponseCode.failureAppConfigurationRequired

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user must perform additional configuration steps before playing slideshows is possible.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
case failureAppConfigurationRequired
```

```c
INStartPhotoPlaybackIntentResponseCodeFailureAppConfigurationRequired
```

## Discussion

Use this response code when your app isn’t configured to play slideshows. For example, you might return this code if the user hasn’t yet added any photos. Don’t use it for general errors or to force the user to launch your app.

## See Also

### Constants
- [INStartPhotoPlaybackIntentResponseCode.unspecified](./unspecified.md)
  The status wasn’t specified.
- [INStartPhotoPlaybackIntentResponseCode.ready](./ready.md)
  You’re ready to handle the intent.
- [INStartPhotoPlaybackIntentResponseCode.continueInApp](./continueinapp.md)
  Your extension is ready to transfer control to the app so that the slideshow can begin.
- [INStartPhotoPlaybackIntentResponseCode.failure](./failure.md)
  You were unable to start the slideshow.
- [INStartPhotoPlaybackIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to start the slideshow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartphotoplaybackintentresponsecode/failureappconfigurationrequired)*