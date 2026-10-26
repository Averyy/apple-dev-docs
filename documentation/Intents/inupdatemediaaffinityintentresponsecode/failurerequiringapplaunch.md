# INUpdateMediaAffinityIntentResponseCode.failureRequiringAppLaunch

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The user needs to launch the app to update the user’s affinity for the media.

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
INUpdateMediaAffinityIntentResponseCodeFailureRequiringAppLaunch
```

#### Discussion

Use this response code when you can’t handle the request with Siri for a reason not covered by any other response code. For example, you might use this code if the user hasn’t set up an account with your app. Don’t use it for general errors or to force the user to launch your app.

## See Also

### Response Code
- [INUpdateMediaAffinityIntentResponseCode.unspecified](./unspecified.md)
  An unknown state.
- [INUpdateMediaAffinityIntentResponseCode.ready](./ready.md)
  The app is ready.
- [INUpdateMediaAffinityIntentResponseCode.inProgress](./inprogress.md)
  The app is currently trying to process the update affinity request.
- [INUpdateMediaAffinityIntentResponseCode.success](./success.md)
  The app successfully updated the user’s affinity for the media.
- [INUpdateMediaAffinityIntentResponseCode.failure](./failure.md)
  The app is unable to update the user’s affinity for the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inupdatemediaaffinityintentresponsecode/failurerequiringapplaunch)*