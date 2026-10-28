# INSearchForMediaIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to search for a media item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INSearchForMediaIntent
```

```objc
@interface INSearchForMediaIntent : INIntent
```

## Mentions

- [Improving Siri Media Interactions and App Selection](../SiriKit/improving-siri-media-interactions-and-app-selection.md)

## Overview

The system creates an [`INSearchForMediaIntent`](./insearchformediaintent.md) object when the user asks Siri to search for a media item, or searches for a musician or band in Spotlight.

To handle this intent, provide a handler that conforms to the [`INSearchForMediaIntentHandling`](./insearchformediaintenthandling.md) protocol. Your handler should confirm the request and create an [`INSearchForMediaIntentResponse`](./insearchformediaintentresponse.md) object with the media to search for.

### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents (audio only) |
| Always requires unlocked device | No |

## Topics

### Initializing the Intent Object
- [init(mediaItems: [INMediaItem]?, mediaSearch: INMediaSearch?)](./insearchformediaintent/init%28mediaitems,mediasearch%29.md)
  Creates an intent that describes the media items for which to search and where to search for them.
### Searching for Media
- [var mediaItems: [INMediaItem]?](./insearchformediaintent/mediaitems.md)
  The media items for which to search.
- [var mediaSearch: INMediaSearch?](./insearchformediaintent/mediasearch.md)
  The location to search for the media item.

## Relationships

### Inherits From
- [INIntent](./inintent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INIntentSetImageKeyPath](./inintentsetimagekeypath.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Search for Media
- [protocol INSearchForMediaIntentHandling](./insearchformediaintenthandling.md)
  The interface that handles media search requests.
- [class INSearchForMediaIntentResponse](./insearchformediaintentresponse.md)
  An intents handler’s response to a search media intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insearchformediaintent)*