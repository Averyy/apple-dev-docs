# INCancelWorkoutIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a cancel workout intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INCancelWorkoutIntentResponse
```

```objc
@interface INCancelWorkoutIntentResponse : INIntentResponse
```

#### Overview

Use an [`INCancelWorkoutIntentResponse`](./incancelworkoutintentresponse.md) object to specify whether your app is able to cancel a workout. The response object contains only the status code that indicates whether to launch your app or whether there was a problem.

You create an [`INCancelWorkoutIntentResponse`](./incancelworkoutintentresponse.md) object in the [`handle(intent:completion:)`](./incancelworkoutintenthandling/handle%28intent,completion%29.md) and [`confirm(intent:completion:)`](./incancelworkoutintenthandling/confirm%28intent,completion%29.md) methods of your cancel workout handler object. For more information about implementing your handler object, see [`INCancelWorkoutIntentHandling`](./incancelworkoutintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INCancelWorkoutIntentResponseCode, userActivity: NSUserActivity?)](./incancelworkoutintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INCancelWorkoutIntentResponseCode](./incancelworkoutintentresponse/code.md)
  The code that indicates whether you successfully handled the intent.
- [enum INCancelWorkoutIntentResponseCode](./incancelworkoutintentresponsecode.md)
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

### Cancel a Workout
- [protocol INCancelWorkoutIntentHandling](./incancelworkoutintenthandling.md)
  The interface that handles requests to cancel a workout.
- [class INCancelWorkoutIntent](./incancelworkoutintent.md)
  A request to cancel an active workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incancelworkoutintentresponse)*