# INPlayMediaMediaItemResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for the media item to play.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INPlayMediaMediaItemResolutionResult
```

```objc
@interface INPlayMediaMediaItemResolutionResult : INMediaItemResolutionResult
```

#### Overview

You return an [`INPlayMediaMediaItemResolutionResult`](./inplaymediamediaitemresolutionresult.md) object when resolving parameters containing an [`INMediaItemResolutionResult`](./inmediaitemresolutionresult.md) value. Use the creation method that best reflects your ability to resolve the parameter successfully.

For additional resolution operators, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Providing Successful Results
- [init(mediaItemResolutionResult: INMediaItemResolutionResult)](./inplaymediamediaitemresolutionresult/init%28mediaitemresolutionresult%29.md)
  Creates a result that involves successfully playing a media item.
- [class func successes(with: [INMediaItem]) -> [INPlayMediaMediaItemResolutionResult]](./inplaymediamediaitemresolutionresult/successes%28with%29.md)
  Creates an array of resolution results based on a set of media items you provide.
### Reporting a Problem
- [class func unsupported(forReason: INPlayMediaMediaItemUnsupportedReason) -> Self](./inplaymediamediaitemresolutionresult/unsupported%28forreason%29.md)
  Creates a result that requires the user to confirm the request, because your app is unable to support the current request.
- [enum INPlayMediaMediaItemUnsupportedReason](./inplaymediamediaitemunsupportedreason.md)
  Reasons the app can’t play the media item.

## Relationships

### Inherits From
- [INMediaItemResolutionResult](./inmediaitemresolutionresult.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediamediaitemresolutionresult)*