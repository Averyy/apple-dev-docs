# INSearchForMediaIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An intents handler’s response to a search media intent.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INSearchForMediaIntentResponse
```

```objc
@interface INSearchForMediaIntentResponse : INIntentResponse
```

## Overview

Use an [`INSearchForMediaIntentResponse`](./insearchformediaintentresponse.md) object to specify the results after searching for the user-specified media. After performing the search action using the criteria specified in the [`INSearchForMediaIntent`](./insearchformediaintent.md) object, create an instance of this class with the results of the action. Siri communicates the status from your response to the user, at appropriate times.

You create an [`INSearchForMediaIntentResponse`](./insearchformediaintentresponse.md) object in the [`confirm(intent:completion:)`](./insearchformediaintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./insearchformediaintenthandling/handle%28intent,completion%29.md) methods of your add media handler object. For more information about implementing your handler object, see [`INSearchForMediaIntentHandling`](./insearchformediaintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INSearchForMediaIntentResponseCode, userActivity: NSUserActivity?)](./insearchformediaintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Providing the Response Code
- [var code: INSearchForMediaIntentResponseCode](./insearchformediaintentresponse/code.md)
  A response code that indicates whether the app successfully searched for the media.
- [enum INSearchForMediaIntentResponseCode](./insearchformediaintentresponsecode.md)
  Codes returned by an intents handler in response to a search request.
### Accessing the Media Item
- [var mediaItems: [INMediaItem]?](./insearchformediaintentresponse/mediaitems.md)
  The media items that were found by the search.

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

### Search for Media
- [protocol INSearchForMediaIntentHandling](./insearchformediaintenthandling.md)
  The interface that handles media search requests.
- [class INSearchForMediaIntent](./insearchformediaintent.md)
  A request to search for a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformediaintentresponse)*