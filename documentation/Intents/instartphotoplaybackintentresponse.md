# INStartPhotoPlaybackIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a start photo playback intent.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.2+ - Deprecated in 8.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INStartPhotoPlaybackIntentResponse
```

```objc
@interface INStartPhotoPlaybackIntentResponse : INIntentResponse
```

## Overview

Use an [`INStartPhotoPlaybackIntentResponse`](./instartphotoplaybackintentresponse.md) object to specify the status of searching the user’s photos and the readiness of your app to begin playing those photos in a slideshow. After performing a search using the criteria specified in the [`INStartPhotoPlaybackIntent`](./instartphotoplaybackintent.md) object, create an instance of this class with the results. Siri communicates the status from your response to the user at appropriate times.

You create an [`INStartPhotoPlaybackIntentResponse`](./instartphotoplaybackintentresponse.md) object in the [`confirm(intent:completion:)`](./instartphotoplaybackintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./instartphotoplaybackintenthandling/handle%28intent,completion%29.md) methods of your start photo playback handler object. For more information about implementing your handler object, see [`INStartPhotoPlaybackIntentHandling`](./instartphotoplaybackintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INStartPhotoPlaybackIntentResponseCode, userActivity: NSUserActivity?)](./instartphotoplaybackintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INStartPhotoPlaybackIntentResponseCode](./instartphotoplaybackintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INStartPhotoPlaybackIntentResponseCode](./instartphotoplaybackintentresponsecode.md)
  Constants indicating the status of the response.
### Accessing the Response Details
- [var searchResultsCount: Int?](./instartphotoplaybackintentresponse/searchresultscount-5r7e7.md)
  The number of photos that match the search parameters.
- [searchResultsCount](./instartphotoplaybackintentresponse/searchresultscount-6ns8y.md)
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

### Photo Playback
- [protocol INStartPhotoPlaybackIntentHandling](./instartphotoplaybackintenthandling.md)
  The handler interface for searching the user’s photos and the playback of the results.
- [class INStartPhotoPlaybackIntent](./instartphotoplaybackintent.md)
  A request to search for photos and initiate a slideshow with the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/instartphotoplaybackintentresponse)*