# INSearchForPhotosIntentResponseCode.continueInApp

**Framework**: Intents  
**Kind**: case  
**Role**: Case

Your extension is ready to transfer control to the app in order to display the search results.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
case continueInApp
```

```c
INSearchForPhotosIntentResponseCodeContinueInApp
```

#### Discussion

Upon returning this code, Siri launches your app and passes it the NSUserActivity object you provided at initialization time. (If you didn’t provide a user activity object, Siri creates one for you). Siri adds an INInteraction object with the intent and your response to the user activity object before delivering it. Your app should use the information in the user activity object to display the search results.

## See Also

### Constants
- [INSearchForPhotosIntentResponseCode.unspecified](./unspecified.md)
  Your app doesn’t provide a specific status.
- [INSearchForPhotosIntentResponseCode.ready](./ready.md)
  You’re ready to handle the intent.
- [INSearchForPhotosIntentResponseCode.failure](./failure.md)
  You were unable to perform the search.
- [INSearchForPhotosIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch your app to search their photos.
- [INSearchForPhotosIntentResponseCode.failureAppConfigurationRequired](./failureappconfigurationrequired.md)
  The user must perform additional configuration steps before searching for photos is possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforphotosintentresponsecode/continueinapp)*