# INUpdateMediaAffinityIntentResponseCode.inProgress

**Framework**: Intents  
**Kind**: case  
**Role**: Case

The app is currently trying to process the update affinity request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
case inProgress
```

```c
INUpdateMediaAffinityIntentResponseCodeInProgress
```

## Discussion

When handling the intent, return this code if it may take more than a few seconds to update the affinity for the media.

## See Also

### Response Code
- [INUpdateMediaAffinityIntentResponseCode.unspecified](./unspecified.md)
  An unknown state.
- [INUpdateMediaAffinityIntentResponseCode.ready](./ready.md)
  The app is ready.
- [INUpdateMediaAffinityIntentResponseCode.success](./success.md)
  The app successfully updated the user’s affinity for the media.
- [INUpdateMediaAffinityIntentResponseCode.failure](./failure.md)
  The app is unable to update the user’s affinity for the media.
- [INUpdateMediaAffinityIntentResponseCode.failureRequiringAppLaunch](./failurerequiringapplaunch.md)
  The user needs to launch the app to update the user’s affinity for the media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inupdatemediaaffinityintentresponsecode/inprogress)*