# INSearchForPhotosIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a search for photos intent.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INSearchForPhotosIntentResponse
```

```objc
@interface INSearchForPhotosIntentResponse : INIntentResponse
```

#### Overview

Use an [`INSearchForPhotosIntentResponse`](./insearchforphotosintentresponse.md) object to specify the results of searching the user’s photos. After performing a search using the criteria specified in the [`INSearchForPhotosIntent`](./insearchforphotosintent.md) object, create an instance of this class with the results of that search. Siri communicates the status from your response to the user at appropriate times.

You create an [`INSearchForPhotosIntentResponse`](./insearchforphotosintentresponse.md) object in the [`confirm(intent:completion:)`](./insearchforphotosintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./insearchforphotosintenthandling/handle%28intent,completion%29.md) methods of your search for photos handler object. For more information about implementing your handler object, see [`INSearchForPhotosIntentHandling`](./insearchforphotosintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INSearchForPhotosIntentResponseCode, userActivity: NSUserActivity?)](./insearchforphotosintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INSearchForPhotosIntentResponseCode](./insearchforphotosintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INSearchForPhotosIntentResponseCode](./insearchforphotosintentresponsecode.md)
  Constants indicating the status of the response.
### Accessing the Response Details
- [var searchResultsCount: Int?](./insearchforphotosintentresponse/searchresultscount-82lnb.md)
  The number of photos that match the search parameters.

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

### Photo Search
- [protocol INSearchForPhotosIntentHandling](./insearchforphotosintenthandling.md)
  The handler interface for searching the user’s photos.
- [class INSearchForPhotosIntent](./insearchforphotosintent.md)
  A request for the list of photos that match the specified criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchforphotosintentresponse)*