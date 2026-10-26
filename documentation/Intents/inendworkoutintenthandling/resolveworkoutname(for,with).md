# resolveWorkoutName(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the workout name that the user wants to end.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
optional func resolveWorkoutName(for intent: INEndWorkoutIntent, with completion: @escaping @Sendable (INSpeakableStringResolutionResult) -> Void)
```

```swift
optional func resolveWorkoutName(for intent: INEndWorkoutIntent) async -> INSpeakableStringResolutionResult
```

```objc
- (void) resolveWorkoutNameForEndWorkout:(INEndWorkoutIntent *) intent withCompletion:(void (^)(INSpeakableStringResolutionResult *resolutionResult)) completion;
```

#### Discussion

This method validates the user-supplied workout name. If you don’t implement this method, SiriKit assumes that you are able to end the requested workout with the specified name.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block while implementing this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For a successful resolution, create a resolution result that includes the workout name that you plan to end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inendworkoutintenthandling/resolveworkoutname(for:with:))*