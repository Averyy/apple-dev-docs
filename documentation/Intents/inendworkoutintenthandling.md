# INEndWorkoutIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

An interface that handles requests to complete a workout.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
protocol INEndWorkoutIntentHandling : NSObjectProtocol
```

```objc
@protocol INEndWorkoutIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INEndWorkoutIntentHandling`](./inendworkoutintenthandling.md) protocol to resolve, confirm, and handle requests to end a workout using your app. Adopt this protocol in an object of your Intents extension capable of validating the workout name.

You don’t actually end the workout from your Intents extension. When your [`handle(intent:completion:)`](./inendworkoutintenthandling/handle%28intent,completion%29.md) returns, SiriKit launches your app and passes it an [`NSUserActivity`](../Foundation/nsuseractivity.md) object that contains the end workout intent object and your response. Your app uses the information in those objects to end the workout.

## Topics

### Resolving the Intent Parameters
- [func resolveWorkoutName(for: INEndWorkoutIntent, with: (INSpeakableStringResolutionResult) -> Void)](./inendworkoutintenthandling/resolveworkoutname%28for,with%29.md)
  Resolves the workout name that the user wants to end.
### Confirming the Response
- [func confirm(intent: INEndWorkoutIntent, completion: (INEndWorkoutIntentResponse) -> Void)](./inendworkoutintenthandling/confirm%28intent,completion%29.md)
  Confirms your app can end the workout.
### Handling the Intent
- [func handle(intent: INEndWorkoutIntent, completion: (INEndWorkoutIntentResponse) -> Void)](./inendworkoutintenthandling/handle%28intent,completion%29.md)
  Handles ending the workout.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INWorkoutsDomainHandling](./inworkoutsdomainhandling.md)

## See Also

### End a Workout
- [class INEndWorkoutIntent](./inendworkoutintent.md)
  A request to end the current workout that also validates workout parameters and saves the results.
- [class INEndWorkoutIntentResponse](./inendworkoutintentresponse.md)
  Your app’s response to an end workout intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inendworkoutintenthandling)*