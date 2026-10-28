# INCancelWorkoutIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to cancel an active workout.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INCancelWorkoutIntent
```

```objc
@interface INCancelWorkoutIntent : INIntent
```

## Overview

SiriKit creates an [`INCancelWorkoutIntent`](./incancelworkoutintent.md) object when the user asks to cancel a currently running workout. Canceling a workout stops the workout and doesn’t record any progress toward the workout goals. Use this intent object to get the workout parameters.

To handle this intent, the handler object in your Intents extension must adopt the [`INCancelWorkoutIntentHandling`](./incancelworkoutintenthandling.md) protocol. Your handler should confirm the request and create an [`INCancelWorkoutIntentResponse`](./incancelworkoutintentresponse.md) object to indicate it’s possible to cancel the workout. For the successful handling of the intent, SiriKit launches your app and passes it an [`NSUserActivity`](../Foundation/nsuseractivity.md) object that your app must then use to cancel the workout.

### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents, Siri Suggestions |
| Always requires unlocked device | Yes |

## Topics

### Creating the Intent Object
- [init(workoutName: INSpeakableString?)](./incancelworkoutintent/init%28workoutname%29.md)
  Initializes an intent object with the specified workout name.
### Specifying Workout Details
- [var workoutName: INSpeakableString?](./incancelworkoutintent/workoutname.md)
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

### Cancel a Workout
- [protocol INCancelWorkoutIntentHandling](./incancelworkoutintenthandling.md)
  The interface that handles requests to cancel a workout.
- [class INCancelWorkoutIntentResponse](./incancelworkoutintentresponse.md)
  Your app’s response to a cancel workout intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incancelworkoutintent)*