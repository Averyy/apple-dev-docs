# INPlaybackQueueLocationResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for the requested playback queue location.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INPlaybackQueueLocationResolutionResult
```

```objc
@interface INPlaybackQueueLocationResolutionResult : INIntentResolutionResult
```

## Overview

You return an [`INPlaybackQueueLocationResolutionResult`](./inplaybackqueuelocationresolutionresult.md) object when resolving parameters containing an [`INPlaybackQueueLocation`](./inplaybackqueuelocation.md) value. Use the creation method that best reflects your ability to resolve the parameter successfully.

For additional resolution operators, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Constants
- [class func success(with: INPlaybackQueueLocation) -> Self](./inplaybackqueuelocationresolutionresult/success%28with%29.md)
  Creates an object whose resolution involves successfully matching the specified parameter.
- [class func confirmationRequired(with: INPlaybackQueueLocation) -> Self](./inplaybackqueuelocationresolutionresult/confirmationrequired%28with%29.md)
  Creates an object whose resolution requires the user to confirm the value before proceeding.
- [enum INPlaybackQueueLocation](./inplaybackqueuelocation.md)
  Constants that describe the playback queue location for a media item.

## Relationships

### Inherits From
- [INIntentResolutionResult](./inintentresolutionresult.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Resolution Results
- [class INAddMediaMediaDestinationResolutionResult](./inaddmediamediadestinationresolutionresult.md)
  A resolution result for the types of destinations when adding media.
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
- [class INSearchForMediaMediaItemResolutionResult](./insearchformediamediaitemresolutionresult.md)
  A resolution result for the media item for which to search.
- [class INUpdateMediaAffinityMediaItemResolutionResult](./inupdatemediaaffinitymediaitemresolutionresult.md)
  A resolution result for updating the user’s affinity for a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaybackqueuelocationresolutionresult)*