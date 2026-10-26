# INStartPhotoPlaybackIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the status of the response.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
enum INStartPhotoPlaybackIntentResponseCode
```

```c
enum INStartPhotoPlaybackIntentResponseCode : NSInteger;
```

## Topics

### Constants
- [INStartPhotoPlaybackIntentResponseCode.unspecified](./instartphotoplaybackintentresponsecode/unspecified.md)
  The status wasn’t specified.
- [INStartPhotoPlaybackIntentResponseCode.ready](./instartphotoplaybackintentresponsecode/ready.md)
  You’re ready to handle the intent.
- [INStartPhotoPlaybackIntentResponseCode.continueInApp](./instartphotoplaybackintentresponsecode/continueinapp.md)
  Your extension is ready to transfer control to the app so that the slideshow can begin.
- [INStartPhotoPlaybackIntentResponseCode.failure](./instartphotoplaybackintentresponsecode/failure.md)
  You were unable to start the slideshow.
- [INStartPhotoPlaybackIntentResponseCode.failureRequiringAppLaunch](./instartphotoplaybackintentresponsecode/failurerequiringapplaunch.md)
  The user must launch your app to start the slideshow.
- [INStartPhotoPlaybackIntentResponseCode.failureAppConfigurationRequired](./instartphotoplaybackintentresponsecode/failureappconfigurationrequired.md)
  The user must perform additional configuration steps before playing slideshows is possible.
### Initializers
- [init?(rawValue: Int)](./instartphotoplaybackintentresponsecode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Response Code
- [var code: INStartPhotoPlaybackIntentResponseCode](./instartphotoplaybackintentresponse/code.md)
  The code indicating whether you successfully handled the intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartphotoplaybackintentresponsecode)*