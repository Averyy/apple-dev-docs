# INMediaItemResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for media item types.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class INMediaItemResolutionResult
```

```objc
@interface INMediaItemResolutionResult : INIntentResolutionResult
```

#### Overview

You return an [`INMediaItemResolutionResult`](./inmediaitemresolutionresult.md) object when resolving parameters containing an [`INMediaItem`](./inmediaitem.md) value. Use the creation method that best reflects your ability to resolve the parameter successfully.

For additional resolution operators, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func success(with: INMediaItem) -> Self](./inmediaitemresolutionresult/success%28with%29.md)
  Creates a result that contains the media item that matches the user’s request.
- [class func successes(with: [INMediaItem]) -> [INMediaItemResolutionResult]](./inmediaitemresolutionresult/successes%28with%29.md)
  Creates an array of results that contains the media items that match the user’s request.
- [class func confirmationRequired(with: INMediaItem?) -> Self](./inmediaitemresolutionresult/confirmationrequired%28with%29.md)
  Creates an object whose resolution requires the user to confirm the value before proceeding.
- [class func disambiguation(with: [INMediaItem]) -> Self](./inmediaitemresolutionresult/disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.

## Relationships

### Inherits From
- [INIntentResolutionResult](./inintentresolutionresult.md)
### Inherited By
- [INAddMediaMediaItemResolutionResult](./inaddmediamediaitemresolutionresult.md)
- [INPlayMediaMediaItemResolutionResult](./inplaymediamediaitemresolutionresult.md)
- [INSearchForMediaMediaItemResolutionResult](./insearchformediamediaitemresolutionresult.md)
- [INUpdateMediaAffinityMediaItemResolutionResult](./inupdatemediaaffinitymediaitemresolutionresult.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inmediaitemresolutionresult)*