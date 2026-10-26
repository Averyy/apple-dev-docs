# INCancelWorkoutIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The interface that handles requests to cancel a workout.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
protocol INCancelWorkoutIntentHandling : NSObjectProtocol
```

```objc
@protocol INCancelWorkoutIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INCancelWorkoutIntentHandling`](./incancelworkoutintenthandling.md) protocol to resolve, confirm, and handle requests to cancel a workout using your app. Adopt this protocol in an object of your Intents extension capable of validating the workout name.

You don’t actually cancel the workout from your Intents extension. When your [`handle(intent:completion:)`](./incancelworkoutintenthandling/handle%28intent,completion%29.md) returns, SiriKit launches your app and passes it an [`NSUserActivity`](../Foundation/nsuseractivity.md) object that contains the cancel workout intent object and your response. Your app uses the information in those objects to handle the cancellation.

## Topics

### Resolving the Intent Parameters
- [func resolveWorkoutName(for: INCancelWorkoutIntent, with: (INSpeakableStringResolutionResult) -> Void)](./incancelworkoutintenthandling/resolveworkoutname%28for,with%29.md)
  Resolves the workout name that the user wants to cancel.
### Confirming the Response
- [func confirm(intent: INCancelWorkoutIntent, completion: (INCancelWorkoutIntentResponse) -> Void)](./incancelworkoutintenthandling/confirm%28intent,completion%29.md)
  Confirms that your app is able to cancel the workout.
### Handling the Intent
- [func handle(intent: INCancelWorkoutIntent, completion: (INCancelWorkoutIntentResponse) -> Void)](./incancelworkoutintenthandling/handle%28intent,completion%29.md)
  Handles the canceling of the workout.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INWorkoutsDomainHandling](./inworkoutsdomainhandling.md)

## See Also

### Cancel a Workout
- [class INCancelWorkoutIntent](./incancelworkoutintent.md)
  A request to cancel an active workout.
- [class INCancelWorkoutIntentResponse](./incancelworkoutintentresponse.md)
  Your app’s response to a cancel workout intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incancelworkoutintenthandling)*