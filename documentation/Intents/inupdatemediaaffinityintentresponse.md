# INUpdateMediaAffinityIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An intents handler’s response to an update media affinity intent.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INUpdateMediaAffinityIntentResponse
```

```objc
@interface INUpdateMediaAffinityIntentResponse : INIntentResponse
```

#### Overview

Use an [`INUpdateMediaAffinityIntentResponse`](./inupdatemediaaffinityintentresponse.md) object to specify the results from trying to update the user’s affinity for a media item. After performing the add action using the criteria specified in the [`INUpdateMediaAffinityIntent`](./inupdatemediaaffinityintent.md) object, create an instance of this class with the results of the action. Siri communicates the response status to the user at appropriate times.

You create an [`INUpdateMediaAffinityIntentResponse`](./inupdatemediaaffinityintentresponse.md) object in the [`confirm(intent:completion:)`](./inupdatemediaaffinityintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./inupdatemediaaffinityintenthandling/handle%28intent,completion%29.md) methods of your add media handler object. For more information about implementing your handler object, see [`INUpdateMediaAffinityIntentHandling`](./inupdatemediaaffinityintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INUpdateMediaAffinityIntentResponseCode, userActivity: NSUserActivity?)](./inupdatemediaaffinityintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Providing the Response Code
- [var code: INUpdateMediaAffinityIntentResponseCode](./inupdatemediaaffinityintentresponse/code.md)
  The code that indicates whether the app successfully updated the user’s affinity for the media.
- [enum INUpdateMediaAffinityIntentResponseCode](./inupdatemediaaffinityintentresponsecode.md)
  Codes returned by an intents handler in response to an update media affinity request.

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

### Update Media Affinity
- [protocol INUpdateMediaAffinityIntentHandling](./inupdatemediaaffinityintenthandling.md)
  The interface that handles requests to update the user’s preference for a media item.
- [class INUpdateMediaAffinityIntent](./inupdatemediaaffinityintent.md)
  A request to update the user’s affinity for a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inupdatemediaaffinityintentresponse)*