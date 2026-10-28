# resolveWorkoutName(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the workout name that the user wants to resume.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
optional func resolveWorkoutName(for intent: INResumeWorkoutIntent, with completion: @escaping @Sendable (INSpeakableStringResolutionResult) -> Void)
```

```swift
optional func resolveWorkoutName(for intent: INResumeWorkoutIntent) async -> INSpeakableStringResolutionResult
```

```objc
- (void) resolveWorkoutNameForResumeWorkout:(INResumeWorkoutIntent *) intent withCompletion:(void (^)(INSpeakableStringResolutionResult *resolutionResult)) completion;
```

## Discussion

This method validates the workout name supplied by the user. If you don’t implement this method, SiriKit assumes that you’re able to resume the requested workout with the specified name.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block while implementing this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object that contains the details of your proposed resolution. For a successful resolution, create a resolution result that includes the workout name you plan to resume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inresumeworkoutintenthandling/resolveworkoutname(for:with:))*