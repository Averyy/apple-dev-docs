# confirm(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Confirms that you can pause the current workout.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
optional func confirm(intent: INPauseWorkoutIntent, completion: @escaping @Sendable (INPauseWorkoutIntentResponse) -> Void)
```

```swift
optional func confirm(intent: INPauseWorkoutIntent) async -> INPauseWorkoutIntentResponse
```

```objc
- (void) confirmPauseWorkout:(INPauseWorkoutIntent *) intent completion:(void (^)(INPauseWorkoutIntentResponse *response)) completion;
```

## Discussion

This method validates that your app is able to pause the user’s current workout. For example, verify that a workout is currently in progress and you can pause it.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use the information in this object to get user-specified information.
- `completion`: The handler block to execute with your response. You must execute this handler while implementing this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INPauseWorkoutIntentResponse`](../inpauseworkoutintentresponse.md) object that contains the status of whether your app is able to pause the workout. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpauseworkoutintenthandling/confirm(intent:completion:))*