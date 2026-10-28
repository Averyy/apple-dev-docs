# INEndWorkoutIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to end the current workout that also validates workout parameters and saves the results.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INEndWorkoutIntent
```

```objc
@interface INEndWorkoutIntent : INIntent
```

## Overview

SiriKit creates an [`INEndWorkoutIntent`](./inendworkoutintent.md) object when the user asks to finish an in-progress workout. Finishing a workout stops it and records any progress made toward the workout’s goals. Use this intent object to validate the workout parameters.

To handle this intent, the handler object in your Intents extension must adopt the [`INEndWorkoutIntentHandling`](./inendworkoutintenthandling.md) protocol. Your handler should confirm the request and create an [`INEndWorkoutIntentResponse`](./inendworkoutintentresponse.md) object that indicates it’s possible to end the workout. For the successful handling of the intent, SiriKit launches your app and passes it an [`NSUserActivity`](../Foundation/nsuseractivity.md) object your app must then use to end the workout.

### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents, Siri Suggestions |
| Always requires unlocked device | Yes |

## Topics

### Creating the Intent Object
- [init(workoutName: INSpeakableString?)](./inendworkoutintent/init%28workoutname%29.md)
  Initializes an intent object with the specified workout name.
### Specifying Workout Details
- [var workoutName: INSpeakableString?](./inendworkoutintent/workoutname.md)
  The name of the workout.

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

### End a Workout
- [protocol INEndWorkoutIntentHandling](./inendworkoutintenthandling.md)
  An interface that handles requests to complete a workout.
- [class INEndWorkoutIntentResponse](./inendworkoutintentresponse.md)
  Your app’s response to an end workout intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inendworkoutintent)*