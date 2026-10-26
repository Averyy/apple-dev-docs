# INResumeWorkoutIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to resume a paused workout.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INResumeWorkoutIntent
```

```objc
@interface INResumeWorkoutIntent : INIntent
```

#### Overview

SiriKit creates an [`INResumeWorkoutIntent`](./inresumeworkoutintent.md) object when the user asks to resume a currently paused workout. Resuming a workout resumes gathering workout data and counting that data toward the user’s current workout goal. Use this intent object to validate the workout parameters.

To handle this intent, the handler object in your Intents extension must adopt the [`INResumeWorkoutIntentHandling`](./inresumeworkoutintenthandling.md) protocol. Your handler should confirm the request and create an [`INResumeWorkoutIntentResponse`](./inresumeworkoutintentresponse.md) object that indicates it’s possible to resume the workout. For the successful handling of the intent, SiriKit launches your app and passes it an [`NSUserActivity`](../Foundation/nsuseractivity.md) object your app must then use to resume the workout.

##### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents, Siri Suggestions |
| Always requires unlocked device | Yes |

## Topics

### Creating the Intent Object
- [init(workoutName: INSpeakableString?)](./inresumeworkoutintent/init%28workoutname%29.md)
  Initializes an intent object with the specified workout name.
### Specifying Workout Details
- [var workoutName: INSpeakableString?](./inresumeworkoutintent/workoutname.md)
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

### Resume a Workout
- [protocol INResumeWorkoutIntentHandling](./inresumeworkoutintenthandling.md)
  The interface that handles requests to resume a workout.
- [class INResumeWorkoutIntentResponse](./inresumeworkoutintentresponse.md)
  Your app’s response to a resume workout intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inresumeworkoutintent)*