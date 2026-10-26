# INResumeWorkoutIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a resume workout intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INResumeWorkoutIntentResponse
```

```objc
@interface INResumeWorkoutIntentResponse : INIntentResponse
```

#### Overview

Use an [`INResumeWorkoutIntentResponse`](./inresumeworkoutintentresponse.md) object to specify whether your app is able to resume a workout. The response object contains only the status code that indicates whether to launch your app or whether there was a problem.

You create an [`INResumeWorkoutIntentResponse`](./inresumeworkoutintentresponse.md) object in the [`handle(intent:completion:)`](./inresumeworkoutintenthandling/handle%28intent,completion%29.md) and [`confirm(intent:completion:)`](./inresumeworkoutintenthandling/confirm%28intent,completion%29.md) methods of your resume workout handler object. For more information about implementing your handler object, see [`INResumeWorkoutIntentHandling`](./inresumeworkoutintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INResumeWorkoutIntentResponseCode, userActivity: NSUserActivity?)](./inresumeworkoutintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INResumeWorkoutIntentResponseCode](./inresumeworkoutintentresponse/code.md)
  The code that indicates whether you successfully handled the intent.
- [enum INResumeWorkoutIntentResponseCode](./inresumeworkoutintentresponsecode.md)
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

### Resume a Workout
- [protocol INResumeWorkoutIntentHandling](./inresumeworkoutintenthandling.md)
  The interface that handles requests to resume a workout.
- [class INResumeWorkoutIntent](./inresumeworkoutintent.md)
  A request to resume a paused workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inresumeworkoutintentresponse)*