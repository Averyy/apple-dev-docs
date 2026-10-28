# INAddMediaIntentResponseCode.ready

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The app is ready to add media.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case ready
```

```c
INAddMediaIntentResponseCodeReady
```

## Discussion

During the confirmation phase of an intent, use this code to signal that your app is ready and able to act on the intent.

## See Also

### Response Code
- [INAddMediaIntentResponseCode.unspecified](./unspecified.md)
  An unknown state.
- [INAddMediaIntentResponseCode.inProgress](./inprogress.md)
  The app is currently trying to process the add media request.
- [INAddMediaIntentResponseCode.success](./success.md)
  The app successfully added the media.
- [INAddMediaIntentResponseCode.handleInApp](./handleinapp.md)
  The system should launch the app in the background to handle the intent.
- [INAddMediaIntentResponseCode.failure](./failure.md)
  The app was unable to add the media.
- [INAddMediaIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch the app to add media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediaintentresponsecode/ready)*