# INPauseWorkoutIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

An interface that handles requests to pause a workout.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
protocol INPauseWorkoutIntentHandling : NSObjectProtocol
```

```objc
@protocol INPauseWorkoutIntentHandling <NSObject>
```

## Overview

Use the methods of the [`INPauseWorkoutIntentHandling`](./inpauseworkoutintenthandling.md) protocol to resolve, confirm, and handle requests to pause a workout that’s using your app. Adopt this protocol in an object of your Intents extension that’s capable of validating the workout name.

You don’t actually pause the workout from your Intents extension. When the [`handle(intent:completion:)`](./inpauseworkoutintenthandling/handle%28intent,completion%29.md) returns, SiriKit launches your app and passes it to an [`NSUserActivity`](../Foundation/nsuseractivity.md) object that contains the intent object and your response. Your app uses the information in those objects to pause the workout.

## Topics

### Resolving the Intent Parameters
- [func resolveWorkoutName(for: INPauseWorkoutIntent, with: (INSpeakableStringResolutionResult) -> Void)](./inpauseworkoutintenthandling/resolveworkoutname%28for,with%29.md)
  Resolves the name of the workout that the user wants to pause.
### Confirming the Intent
- [func confirm(intent: INPauseWorkoutIntent, completion: (INPauseWorkoutIntentResponse) -> Void)](./inpauseworkoutintenthandling/confirm%28intent,completion%29.md)
  Confirms that you can pause the current workout.
### Handling the Intent
- [func handle(intent: INPauseWorkoutIntent, completion: (INPauseWorkoutIntentResponse) -> Void)](./inpauseworkoutintenthandling/handle%28intent,completion%29.md)
  Handle pausing the workout.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INWorkoutsDomainHandling](./inworkoutsdomainhandling.md)

## See Also

### Pause a Workout
- [class INPauseWorkoutIntent](./inpauseworkoutintent.md)
  A request to pause the current workout that also stops the gathering of workout data.
- [class INPauseWorkoutIntentResponse](./inpauseworkoutintentresponse.md)
  Your app’s response to a pause workout intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpauseworkoutintenthandling)*