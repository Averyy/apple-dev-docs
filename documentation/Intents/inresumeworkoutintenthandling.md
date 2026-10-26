# INResumeWorkoutIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

The interface that handles requests to resume a workout.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
protocol INResumeWorkoutIntentHandling : NSObjectProtocol
```

```objc
@protocol INResumeWorkoutIntentHandling <NSObject>
```

#### Overview

Use the methods of the [`INResumeWorkoutIntentHandling`](./inresumeworkoutintenthandling.md) protocol to resolve, confirm, and handle requests to resume a paused workout that’s using your app. Adopt this protocol in an object of your Intents extension that’s capable of validating the workout name.

You don’t actually resume the workout from your Intents extension. When your [`handle(intent:completion:)`](./inresumeworkoutintenthandling/handle%28intent,completion%29.md) returns, Siri launches your app and passes it an [`NSUserActivity`](../Foundation/nsuseractivity.md) object that contains the intent object and your response. Your app uses the information in those objects to resume the workout.

## Topics

### Resolving the Intent Parameters
- [func resolveWorkoutName(for: INResumeWorkoutIntent, with: (INSpeakableStringResolutionResult) -> Void)](./inresumeworkoutintenthandling/resolveworkoutname%28for,with%29.md)
  Resolves the workout name that the user wants to resume.
### Confirming the Response
- [func confirm(intent: INResumeWorkoutIntent, completion: (INResumeWorkoutIntentResponse) -> Void)](./inresumeworkoutintenthandling/confirm%28intent,completion%29.md)
  Confirms that your app is able to resume the workout.
### Handling the Intent
- [func handle(intent: INResumeWorkoutIntent, completion: (INResumeWorkoutIntentResponse) -> Void)](./inresumeworkoutintenthandling/handle%28intent,completion%29.md)
  Handles resuming the workout.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INWorkoutsDomainHandling](./inworkoutsdomainhandling.md)

## See Also

### Resume a Workout
- [class INResumeWorkoutIntent](./inresumeworkoutintent.md)
  A request to resume a paused workout.
- [class INResumeWorkoutIntentResponse](./inresumeworkoutintentresponse.md)
  Your app’s response to a resume workout intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inresumeworkoutintenthandling)*