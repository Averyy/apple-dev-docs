# INAddMediaIntentResponseCode.failure

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The app was unable to add the media.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case failure
```

```c
INAddMediaIntentResponseCodeFailure
```

#### Discussion

Use this code for both transient and unrecoverable errors that would prevent your app from adding the media.

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
- [INAddMediaIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch the app to add media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediaintentresponsecode/failure)*