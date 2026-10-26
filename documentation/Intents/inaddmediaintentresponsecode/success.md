# INAddMediaIntentResponseCode.success

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The app successfully added the media.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case success
```

```c
INAddMediaIntentResponseCodeSuccess
```

#### Discussion

Use this code when your app has successfully added the media.

## See Also

### Response Code
- [INAddMediaIntentResponseCode.unspecified](./unspecified.md)
  An unknown state.
- [INAddMediaIntentResponseCode.ready](./ready.md)
  The app is ready to add media.
- [INAddMediaIntentResponseCode.inProgress](./inprogress.md)
  The app is currently trying to process the add media request.
- [INAddMediaIntentResponseCode.handleInApp](./handleinapp.md)
  The system should launch the app in the background to handle the intent.
- [INAddMediaIntentResponseCode.failure](./failure.md)
  The app was unable to add the media.
- [INAddMediaIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch the app to add media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediaintentresponsecode/success)*