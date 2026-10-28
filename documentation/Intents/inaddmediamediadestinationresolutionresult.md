# INAddMediaMediaDestinationResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for the types of destinations when adding media.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INAddMediaMediaDestinationResolutionResult
```

```objc
@interface INAddMediaMediaDestinationResolutionResult : INMediaDestinationResolutionResult
```

## Overview

You return an [`INAddMediaMediaDestinationResolutionResult`](./inaddmediamediadestinationresolutionresult.md) object when resolving parameters containing an [`INMediaDestinationResolutionResult`](./inmediadestinationresolutionresult.md) value. Use the creation method that best reflects your ability to resolve the parameter successfully.

For additional resolution operators, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result
- [init(mediaDestinationResolutionResult: INMediaDestinationResolutionResult)](./inaddmediamediadestinationresolutionresult/init%28mediadestinationresolutionresult%29.md)
  Creates an object whose resolution involves successfully adding a media item to a particular destination.
- [class func unsupported(forReason: INAddMediaMediaDestinationUnsupportedReason) -> Self](./inaddmediamediadestinationresolutionresult/unsupported%28forreason%29.md)
  Creates an object whose resolution requires the user to confirm the media destination.
- [enum INAddMediaMediaDestinationUnsupportedReason](./inaddmediamediadestinationunsupportedreason.md)
  Reasons describing why the destination is not supported.

## Relationships

### Inherits From
- [INMediaDestinationResolutionResult](./inmediadestinationresolutionresult.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Resolution Results
- [class INAddMediaMediaItemResolutionResult](./inaddmediamediaitemresolutionresult.md)
  A resolution result for the media item to add.
- [class INMediaDestinationResolutionResult](./inmediadestinationresolutionresult.md)
  A resolution result for the media destination types.
- [class INMediaItemResolutionResult](./inmediaitemresolutionresult.md)
  A resolution result for media item types.
- [class INMediaAffinityTypeResolutionResult](./inmediaaffinitytyperesolutionresult.md)
  A resolution result for the user’s affinity for a media item.
- [class INPlayMediaMediaItemResolutionResult](./inplaymediamediaitemresolutionresult.md)
  A resolution result for the media item to play.
- [class INPlayMediaPlaybackSpeedResolutionResult](./inplaymediaplaybackspeedresolutionresult.md)
  A resolution result that determines the playback speed of a media item.
- [class INPlaybackRepeatModeResolutionResult](./inplaybackrepeatmoderesolutionresult.md)
  A resolution result for the playback repeat modes of a media item.
- [class INPlaybackQueueLocationResolutionResult](./inplaybackqueuelocationresolutionresult.md)
  A resolution result for the requested playback queue location.
- [class INSearchForMediaMediaItemResolutionResult](./insearchformediamediaitemresolutionresult.md)
  A resolution result for the media item for which to search.
- [class INUpdateMediaAffinityMediaItemResolutionResult](./inupdatemediaaffinitymediaitemresolutionresult.md)
  A resolution result for updating the user’s affinity for a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddmediamediadestinationresolutionresult)*