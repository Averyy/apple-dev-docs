# INPauseWorkoutIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a pause workout intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INPauseWorkoutIntentResponse
```

```objc
@interface INPauseWorkoutIntentResponse : INIntentResponse
```

## Overview

Use an [`INPauseWorkoutIntentResponse`](./inpauseworkoutintentresponse.md) object to specify whether your app is able to pause a workout. The response object contains only the status code that indicates whether to launch your app or whether there was a problem.

You create an [`INPauseWorkoutIntentResponse`](./inpauseworkoutintentresponse.md) object in the [`handle(intent:completion:)`](./inpauseworkoutintenthandling/handle%28intent,completion%29.md) and [`confirm(intent:completion:)`](./inpauseworkoutintenthandling/confirm%28intent,completion%29.md) methods of your pause workout handler object. For more information about implementing your handler object, see [`INPauseWorkoutIntentHandling`](./inpauseworkoutintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INPauseWorkoutIntentResponseCode, userActivity: NSUserActivity?)](./inpauseworkoutintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INPauseWorkoutIntentResponseCode](./inpauseworkoutintentresponse/code.md)
  The code that indicates whether you successfully handled the intent.
- [enum INPauseWorkoutIntentResponseCode](./inpauseworkoutintentresponsecode.md)
  Constants that indicate the response state.

## Relationships

### Inherits From
- [INIntentResponse](./inintentresponse.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Pause a Workout
- [protocol INPauseWorkoutIntentHandling](./inpauseworkoutintenthandling.md)
  An interface that handles requests to pause a workout.
- [class INPauseWorkoutIntent](./inpauseworkoutintent.md)
  A request to pause the current workout that also stops the gathering of workout data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpauseworkoutintentresponse)*