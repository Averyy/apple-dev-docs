# INUpdateMediaAffinityIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request to update the user’s affinity for a media item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INUpdateMediaAffinityIntent
```

```objc
@interface INUpdateMediaAffinityIntent : INIntent
```

## Mentions

- [Improving Siri Media Interactions and App Selection](../SiriKit/improving-siri-media-interactions-and-app-selection.md)

#### Overview

Siri creates an [`INUpdateMediaAffinityIntent`](./inupdatemediaaffinityintent.md) object when the user expresses a preference for or disinterest in a media item. The intent object contains the media to update.

To handle this intent, the handler object in your Intents extension must adopt the [`INUpdateMediaAffinityIntentHandling`](./inupdatemediaaffinityintenthandling.md) protocol. Your handler should confirm the request and create an [`INUpdateMediaAffinityIntentResponse`](./inupdatemediaaffinityintentresponse.md) object with the media to update.

##### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Siri Intents (audio only) |
| Always requires unlocked device | No |

## Topics

### Initializing the Intent Object
- [init(mediaItems: [INMediaItem]?, mediaSearch: INMediaSearch?, affinityType: INMediaAffinityType)](./inupdatemediaaffinityintent/init%28mediaitems,mediasearch,affinitytype%29.md)
  Creates an intent that describes the media items, their location, and the affinity to update.
### Getting the Media Information
- [var affinityType: INMediaAffinityType](./inupdatemediaaffinityintent/affinitytype.md)
  The user’s affinity for the media item.
- [enum INMediaAffinityType](./inmediaaffinitytype.md)
  Constants that describe a user’s affinity for a media item.
- [var mediaItems: [INMediaItem]?](./inupdatemediaaffinityintent/mediaitems.md)
  The media items to update.
- [var mediaSearch: INMediaSearch?](./inupdatemediaaffinityintent/mediasearch.md)
  The type of item to search for.

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

### Update Media Affinity
- [protocol INUpdateMediaAffinityIntentHandling](./inupdatemediaaffinityintenthandling.md)
  The interface that handles requests to update the user’s preference for a media item.
- [class INUpdateMediaAffinityIntentResponse](./inupdatemediaaffinityintentresponse.md)
  An intents handler’s response to an update media affinity intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inupdatemediaaffinityintent)*