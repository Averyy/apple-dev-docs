# INPauseWorkoutIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to pause the current workout that also stops the gathering of workout data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INPauseWorkoutIntent
```

```objc
@interface INPauseWorkoutIntent : INIntent
```

## Overview

SiriKit creates an [`INPauseWorkoutIntent`](./inpauseworkoutintent.md) object when the user asks to pause a currently running workout. Pausing a workout stops the gathering of workout data without clearing the current workout progress information. Use this intent object to validate workout parameters.

To handle this intent, the handler object in your Intents extension must adopt the [`INPauseWorkoutIntentHandling`](./inpauseworkoutintenthandling.md) protocol. Your handler should confirm the request and create an [`INPauseWorkoutIntentResponse`](./inpauseworkoutintentresponse.md) object that indicates it’s possible to pause the workout. SiriKit launches your app and passes it an [`NSUserActivity`](../Foundation/nsuseractivity.md) object that your app must then use to pause the workout.

### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents, Siri Suggestions |
| Always requires unlocked device | Yes |

## Topics

### Creating the Intent Object
- [init(workoutName: INSpeakableString?)](./inpauseworkoutintent/init%28workoutname%29.md)
  Initializes an intent object with the specified workout name.
### Specifying Workout Details
- [var workoutName: INSpeakableString?](./inpauseworkoutintent/workoutname.md)
  The name of the workout to pause.

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

### Pause a Workout
- [protocol INPauseWorkoutIntentHandling](./inpauseworkoutintenthandling.md)
  An interface that handles requests to pause a workout.
- [class INPauseWorkoutIntentResponse](./inpauseworkoutintentresponse.md)
  Your app’s response to a pause workout intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpauseworkoutintent)*