# resolveWorkoutName(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the name of the workout that the user wants to pause.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
optional func resolveWorkoutName(for intent: INPauseWorkoutIntent, with completion: @escaping @Sendable (INSpeakableStringResolutionResult) -> Void)
```

```swift
optional func resolveWorkoutName(for intent: INPauseWorkoutIntent) async -> INSpeakableStringResolutionResult
```

```objc
- (void) resolveWorkoutNameForPauseWorkout:(INPauseWorkoutIntent *) intent withCompletion:(void (^)(INSpeakableStringResolutionResult *resolutionResult)) completion;
```

## Discussion

This method validates the user-supplied workout name. If you don’t implement this method, SiriKit assumes that you’re able to pause the requested workout with the specified name.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block while implmenting this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object that contains the details of your proposed resolution. For a successful resolution, create a resolution result that includes name of the workout that you plan to pause.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpauseworkoutintenthandling/resolveworkoutname(for:with:))*