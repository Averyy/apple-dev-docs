# INSearchForPhotosIntentResponseCode.ready

**Framework**: Intents  
**Kind**: case  
**Role**: Case

You’re ready to handle the intent.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
case ready
```

```c
INSearchForPhotosIntentResponseCodeReady
```

## Discussion

During the confirmation phase of an intent, use this code to signal that your app is ready and able to act on the intent.

## See Also

### Constants
- [INSearchForPhotosIntentResponseCode.unspecified](./unspecified.md)
  Your app doesn’t provide a specific status.
- [INSearchForPhotosIntentResponseCode.continueInApp](./continueinapp.md)
  Your extension is ready to transfer control to the app in order to display the search results.
- [INSearchForPhotosIntentResponseCode.failure](./failure.md)
  You were unable to perform the search.
- [INSearchForPhotosIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to search their photos.
- [INSearchForPhotosIntentResponseCode.failureAppConfigurationRequired](./failureappconfigurationrequired.md)
  The user must perform additional configuration steps before searching for photos is possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforphotosintentresponsecode/ready)*