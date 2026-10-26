# INEndWorkoutIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to an end workout intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INEndWorkoutIntentResponse
```

```objc
@interface INEndWorkoutIntentResponse : INIntentResponse
```

#### Overview

Use an [`INEndWorkoutIntentResponse`](./inendworkoutintentresponse.md) object to specify whether your app is able to end a workout. The response object contains only the status code that indicates whether to launch your app or whether there was a problem.

You create an [`INEndWorkoutIntentResponse`](./inendworkoutintentresponse.md) object in the [`handle(intent:completion:)`](./inendworkoutintenthandling/handle%28intent,completion%29.md) and [`confirm(intent:completion:)`](./inendworkoutintenthandling/confirm%28intent,completion%29.md) methods of your end workout handler object. For more information about implementing your handler object, see [`INEndWorkoutIntentHandling`](./inendworkoutintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INEndWorkoutIntentResponseCode, userActivity: NSUserActivity?)](./inendworkoutintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INEndWorkoutIntentResponseCode](./inendworkoutintentresponse/code.md)
  The code that indicates whether you successfully handled the intent.
- [enum INEndWorkoutIntentResponseCode](./inendworkoutintentresponsecode.md)
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

### End a Workout
- [protocol INEndWorkoutIntentHandling](./inendworkoutintenthandling.md)
  An interface that handles requests to complete a workout.
- [class INEndWorkoutIntent](./inendworkoutintent.md)
  A request to end the current workout that also validates workout parameters and saves the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inendworkoutintentresponse)*