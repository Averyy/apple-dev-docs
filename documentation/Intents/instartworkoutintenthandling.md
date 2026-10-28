# INStartWorkoutIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

An interface that handles requests to start a workout.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
protocol INStartWorkoutIntentHandling : NSObjectProtocol
```

```objc
@protocol INStartWorkoutIntentHandling <NSObject>
```

## Overview

Use the methods of the [`INStartWorkoutIntentHandling`](./instartworkoutintenthandling.md) protocol to resolve, confirm, and handle requests to start a workout using your app. Adopt this protocol in an object of your Intents extension capable of validating the workout name or goals.

You don’t actually start a workout from your Intents extension. When your [`handle(intent:completion:)`](./instartworkoutintenthandling/handle%28intent,completion%29.md) returns, Siri launches your app and passes it an [`NSUserActivity`](../Foundation/nsuseractivity.md) object that contains the [`INStartWorkoutIntent`](./instartworkoutintent.md) object and your response. Your app uses the information in those objects to start the workout.

## Topics

### Resolving the Intent Parameters
- [func resolveWorkoutName(for: INStartWorkoutIntent, with: (INSpeakableStringResolutionResult) -> Void)](./instartworkoutintenthandling/resolveworkoutname%28for,with%29.md)
  Resolves the workout name selected by the user.
- [func resolveGoalValue(for: INStartWorkoutIntent, with: (INDoubleResolutionResult) -> Void)](./instartworkoutintenthandling/resolvegoalvalue%28for,with%29.md)
  Resolves the numerical goal of a user’s workout.
- [func resolveWorkoutGoalUnitType(for: INStartWorkoutIntent, with: (INWorkoutGoalUnitTypeResolutionResult) -> Void)](./instartworkoutintenthandling/resolveworkoutgoalunittype%28for,with%29.md)
  Resolves the units for the user’s workout goal.
- [func resolveWorkoutLocationType(for: INStartWorkoutIntent, with: (INWorkoutLocationTypeResolutionResult) -> Void)](./instartworkoutintenthandling/resolveworkoutlocationtype%28for,with%29.md)
  Resolves the location type of a user’s workout.
- [func resolveIsOpenEnded(for: INStartWorkoutIntent, with: (INBooleanResolutionResult) -> Void)](./instartworkoutintenthandling/resolveisopenended%28for,with%29.md)
  Resolves whether the user’s workout is open ended.
### Confirming the Response
- [func confirm(intent: INStartWorkoutIntent, completion: (INStartWorkoutIntentResponse) -> Void)](./instartworkoutintenthandling/confirm%28intent,completion%29.md)
  Validates that your app is able to start the workout.
### Handling the Intent
- [func handle(intent: INStartWorkoutIntent, completion: (INStartWorkoutIntentResponse) -> Void)](./instartworkoutintenthandling/handle%28intent,completion%29.md)
  Handles starting the workout.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INWorkoutsDomainHandling](./inworkoutsdomainhandling.md)

## See Also

### Start a Workout
- [class INStartWorkoutIntent](./instartworkoutintent.md)
  A request to start a workout for the user.
- [class INStartWorkoutIntentResponse](./instartworkoutintentresponse.md)
  Your app’s response to a start workout intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartworkoutintenthandling)*