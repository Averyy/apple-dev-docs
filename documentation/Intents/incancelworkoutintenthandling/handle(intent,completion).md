# handle(intent:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Handles the canceling of the workout.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
func handle(intent: INCancelWorkoutIntent, completion: @escaping @Sendable (INCancelWorkoutIntentResponse) -> Void)
```

```swift
func handle(intent: INCancelWorkoutIntent) async -> INCancelWorkoutIntentResponse
```

```objc
- (void) handleCancelWorkout:(INCancelWorkoutIntent *) intent completion:(void (^)(INCancelWorkoutIntentResponse *response)) completion;
```

## Discussion

This method transfers control of starting the workout over to your app. When your response object contains the [`INCancelWorkoutIntentResponseCode.continueInApp`](../incancelworkoutintentresponsecode/continueinapp.md) code, SiriKit automatically launches your app and passes it the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object from your response object.

## Parameters

- `intent`: The intent object that contains details about the user’s request. The object’s information has already been resolved and confirmed by the user.
- `completion`: The handler block to execute with your response. You must execute this handler while implementing this method. This handler has no return value and takes the following parameter:

  - **response**: The [`INCancelWorkoutIntentResponse`](../incancelworkoutintentresponse.md) object you create to report the status of the request. This parameter must not be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incancelworkoutintenthandling/handle(intent:completion:))*