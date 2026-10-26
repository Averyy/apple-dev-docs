# INUpdateMediaAffinityIntentResponseCode.ready

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The app is ready.

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
INUpdateMediaAffinityIntentResponseCodeReady
```

#### Discussion

During the confirmation phase of an intent, use this code to signal that your app is ready and able to act on the intent.

## See Also

### Response Code
- [INUpdateMediaAffinityIntentResponseCode.unspecified](./unspecified.md)
  An unknown state.
- [INUpdateMediaAffinityIntentResponseCode.inProgress](./inprogress.md)
  The app is currently trying to process the update affinity request.
- [INUpdateMediaAffinityIntentResponseCode.success](./success.md)
  The app successfully updated the user’s affinity for the media.
- [INUpdateMediaAffinityIntentResponseCode.failure](./failure.md)
  The app is unable to update the user’s affinity for the media.
- [INUpdateMediaAffinityIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user needs to launch the app to update the user’s affinity for the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inupdatemediaaffinityintentresponsecode/ready)*