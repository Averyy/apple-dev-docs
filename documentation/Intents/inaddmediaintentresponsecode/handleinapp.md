# INAddMediaIntentResponseCode.handleInApp

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The system should launch the app in the background to handle the intent.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case handleInApp
```

```c
INAddMediaIntentResponseCodeHandleInApp
```

#### Discussion

Because the lifespan of an app extension is short, adding media should happen in your app, not in the Intents app extension. To handle adding media in your app while in the background, return [`INAddMediaIntentResponseCode.handleInApp`](./handleinapp.md) as the response [`code`](../inaddmediaintentresponse/code.md).

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
- [INAddMediaIntentResponseCode.failure](./failure.md)
  The app was unable to add the media.
- [INAddMediaIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user must launch the app to add media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediaintentresponsecode/handleinapp)*