# INStartWorkoutIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to start a workout for the user.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INStartWorkoutIntent
```

```objc
@interface INStartWorkoutIntent : INIntent
```

## Mentions

- [Confirming the Details of an Intent](../SiriKit/confirming-the-details-of-an-intent.md)

## Overview

SiriKit creates an [`INStartWorkoutIntent`](./instartworkoutintent.md) object when the user asks to start a workout using your app. A start workout intent identifies the user-selected workout type and goals.

To handle this intent, the handler object in your Intents extension must adopt the [`INStartWorkoutIntentHandling`](./instartworkoutintenthandling.md) protocol. Your handler should confirm the request and create an [`INStartWorkoutIntentResponse`](./instartworkoutintentresponse.md) object that indicates it’s possible to start the workout. For the successful handling of the intent, SiriKit launches your app and passes it an [`NSUserActivity`](../Foundation/nsuseractivity.md) object your app must then use to start the workout.

### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents, Siri Suggestions |
| Always requires unlocked device | Yes |

## Topics

### Creating the Intent Object
- [convenience init(workoutName: INSpeakableString?, goalValue: Double?, workoutGoalUnitType: INWorkoutGoalUnitType, workoutLocationType: INWorkoutLocationType, isOpenEnded: Bool?)](./instartworkoutintent/init%28workoutname,goalvalue,workoutgoalunittype,workoutlocationtype,isopenended%29.md)
  Initializes an intent object with the specified workout information.
- [- initWithWorkoutName:goalValue:workoutGoalUnitType:workoutLocationType:isOpenEnded:](./instartworkoutintent/initwithworkoutname_goalvalue_workoutgoalunittype_workoutlocationtype_isopenended_.md)
  Initializes an intent object with the specified workout information.
### Specifying Workout Details
- [var workoutName: INSpeakableString?](./instartworkoutintent/workoutname.md)
  The name of the workout.
- [var goalValue: Double?](./instartworkoutintent/goalvalue-5oazy.md)
  The user-supplied numerical goal of the workout.
- [var workoutGoalUnitType: INWorkoutGoalUnitType](./instartworkoutintent/workoutgoalunittype.md)
  The units associated with the workout goal.
- [var workoutLocationType: INWorkoutLocationType](./instartworkoutintent/workoutlocationtype.md)
  The location of the workout.
- [var isOpenEnded: Bool?](./instartworkoutintent/isopenended-8hecn.md)
  A Boolean value that indicates whether the workout is open ended.
- [goalValue](./instartworkoutintent/goalvalue-1dzvb.md)
  The numerical goal of the workout.
- [isOpenEnded](./instartworkoutintent/isopenended-avvd.md)
  A Boolean value indicating whether the workout is open ended.

## Relationships

### Inherits From
- [INIntent](./inintent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INIntentSetImageKeyPath](./inintentsetimagekeypath.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Start a Workout
- [protocol INStartWorkoutIntentHandling](./instartworkoutintenthandling.md)
  An interface that handles requests to start a workout.
- [class INStartWorkoutIntentResponse](./instartworkoutintentresponse.md)
  Your app’s response to a start workout intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartworkoutintent)*