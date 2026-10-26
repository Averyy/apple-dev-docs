# INPlayMediaPlaybackSpeedResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result that determines the playback speed of a media item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INPlayMediaPlaybackSpeedResolutionResult
```

```objc
@interface INPlayMediaPlaybackSpeedResolutionResult : INDoubleResolutionResult
```

#### Overview

You return an [`INPlayMediaPlaybackSpeedResolutionResult`](./inplaymediaplaybackspeedresolutionresult.md) object when resolving parameters containing an [`INMediaItemResolutionResult`](./inmediaitemresolutionresult.md) value. Use the creation method that best reflects your ability to resolve the parameter successfully.

For additional resolution operators, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result
- [init(doubleResolutionResult: INDoubleResolutionResult)](./inplaymediaplaybackspeedresolutionresult/init%28doubleresolutionresult%29.md)
  Creates an object whose resolution involves successfulling changing the playback speed of a media item.
- [class func unsupported(forReason: INPlayMediaPlaybackSpeedUnsupportedReason) -> Self](./inplaymediaplaybackspeedresolutionresult/unsupported%28forreason%29.md)
  Creates an object whose resolution requires the user to confirm the request, because your app is unable to support the current request.
- [enum INPlayMediaPlaybackSpeedUnsupportedReason](./inplaymediaplaybackspeedunsupportedreason.md)
  Constants that describe why the app can’t change the playback speed of the media item.

## Relationships

### Inherits From
- [INDoubleResolutionResult](./indoubleresolutionresult.md)
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
- [class INPlaybackRepeatModeResolutionResult](./inplaybackrepeatmoderesolutionresult.md)
  A resolution result for the playback repeat modes of a media item.
- [class INPlaybackQueueLocationResolutionResult](./inplaybackqueuelocationresolutionresult.md)
  A resolution result for the requested playback queue location.
- [class INSearchForMediaMediaItemResolutionResult](./insearchformediamediaitemresolutionresult.md)
  A resolution result for the media item for which to search.
- [class INUpdateMediaAffinityMediaItemResolutionResult](./inupdatemediaaffinitymediaitemresolutionresult.md)
  A resolution result for updating the user’s affinity for a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaplaybackspeedresolutionresult)*