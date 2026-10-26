# INStartWorkoutIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a start workout intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INStartWorkoutIntentResponse
```

```objc
@interface INStartWorkoutIntentResponse : INIntentResponse
```

#### Overview

Use an [`INStartWorkoutIntentResponse`](./instartworkoutintentresponse.md) object to specify whether your app is able to start a workout. The response object contains only the response code that indicates whether to launch your app or whether there was a problem.

You create an [`INStartWorkoutIntentResponse`](./instartworkoutintentresponse.md) object in the [`confirm(intent:completion:)`](./instartworkoutintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./instartworkoutintenthandling/handle%28intent,completion%29.md) methods of your start workout handler object. For more information about implementing your handler object, see [`INStartWorkoutIntentHandling`](./instartworkoutintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INStartWorkoutIntentResponseCode, userActivity: NSUserActivity?)](./instartworkoutintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INStartWorkoutIntentResponseCode](./instartworkoutintentresponse/code.md)
  The code that indicates whether you successfully handled the intent.
- [enum INStartWorkoutIntentResponseCode](./instartworkoutintentresponsecode.md)
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

### Start a Workout
- [protocol INStartWorkoutIntentHandling](./instartworkoutintenthandling.md)
  An interface that handles requests to start a workout.
- [class INStartWorkoutIntent](./instartworkoutintent.md)
  A request to start a workout for the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartworkoutintentresponse)*