# INAddMediaIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to add a media item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INAddMediaIntent
```

```objc
@interface INAddMediaIntent : INIntent
```

## Mentions

- [Improving Siri Media Interactions and App Selection](../SiriKit/improving-siri-media-interactions-and-app-selection.md)

#### Overview

Siri creates an [`INAddMediaIntent`](./inaddmediaintent.md) object when the user asks to add a media item. The intents object contains the media to add.

To handle this intent, the handler object in your Intents extension must adopt the [`INAddMediaIntentHandling`](./inaddmediaintenthandling.md) protocol. Your handler should confirm the request and create an [`INAddMediaIntentResponse`](./inaddmediaintentresponse.md) object that contains the media to add.

##### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents (audio only) |
| Always requires unlocked device | No |

## Topics

### Creating an Add Media Intent
- [init(mediaItems: [INMediaItem]?, mediaSearch: INMediaSearch?, mediaDestination: INMediaDestination?)](./inaddmediaintent/init%28mediaitems,mediasearch,mediadestination%29.md)
  Creates an intent that describes the media items to add and where to add them.
### Accessing the Media
- [var mediaItems: [INMediaItem]?](./inaddmediaintent/mediaitems.md)
  The media content to add.
- [var mediaSearch: INMediaSearch?](./inaddmediaintent/mediasearch.md)
  The location to search for the media item to add.
- [var mediaDestination: INMediaDestination?](./inaddmediaintent/mediadestination.md)
  The location for the media to add.
- [enum INMediaDestination](./inmediadestination-swift.enum.md)
  An object that describes the destination for a media item.
- [class INMediaDestinationReference](./inmediadestinationreference.md)
  An object that describes the destination for a media item.

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

### Add Media
- [protocol INAddMediaIntentHandling](./inaddmediaintenthandling.md)
  The handler interface that adds media.
- [class INAddMediaIntentResponse](./inaddmediaintentresponse.md)
  An intents handler’s response to an add media intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediaintent)*