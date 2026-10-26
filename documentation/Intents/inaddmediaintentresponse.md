# INAddMediaIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An intents handler’s response to an add media intent.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INAddMediaIntentResponse
```

```objc
@interface INAddMediaIntentResponse : INIntentResponse
```

#### Overview

Use an [`INAddMediaIntentResponse`](./inaddmediaintentresponse.md) object to specify the results after the user attempts to add the specified media. After performing the add action using the criteria specified in the [`INAddMediaIntent`](./inaddmediaintent.md) object, create an instance of this class with the results of the action. Siri communicates the status from your response to the user at appropriate times.

You create an [`INAddMediaIntentResponse`](./inaddmediaintentresponse.md) object in the [`confirm(intent:completion:)`](./inaddmediaintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./inaddmediaintenthandling/handle%28intent,completion%29.md) methods of your add media handler object. For more information about implementing your handler object, see [`INAddMediaIntentHandling`](./inaddmediaintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INAddMediaIntentResponseCode, userActivity: NSUserActivity?)](./inaddmediaintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Providing the Response Code
- [var code: INAddMediaIntentResponseCode](./inaddmediaintentresponse/code.md)
  A response code that indicates whether the app successfully added the media.
- [enum INAddMediaIntentResponseCode](./inaddmediaintentresponsecode.md)
  Codes returned by an app or Intents app extension when handling or confirming an add media intent.

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

### Add Media
- [protocol INAddMediaIntentHandling](./inaddmediaintenthandling.md)
  The handler interface that adds media.
- [class INAddMediaIntent](./inaddmediaintent.md)
  A request to add a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediaintentresponse)*