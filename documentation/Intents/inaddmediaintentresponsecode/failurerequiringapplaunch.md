# INAddMediaIntentResponseCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user must launch the app to add media.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case failureRequiringAppLaunch
```

```c
INAddMediaIntentResponseCodeFailureRequiringAppLaunch
```

#### Discussion

Use this response code when you can’t handle the request with Siri for a reason not covered by any other response code. For example, use this code if the user hasn’t set up an account with your app. Don’t use it for general errors or to force the user to launch your app.

## See Also

### Response Code
- [INAddMediaIntentResponseCode.unspecified](./unspecified.md)
  An unknown state.
- [INAddMediaIntentResponseCode.ready](./ready.md)
  The app is ready to add media.
- [INAddMediaIntentResponseCode.inProgress](./inprogress.md)
  The app is currently trying to process the add media request.
- [INAddMediaIntentResponseCode.success](./success.md)
  The app successfully added the media.
- [INAddMediaIntentResponseCode.handleInApp](./handleinapp.md)
  The system should launch the app in the background to handle the intent.
- [INAddMediaIntentResponseCode.failure](./failure.md)
  The app was unable to add the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediaintentresponsecode/failurerequiringapplaunch)*