# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires the user to confirm the value before proceeding.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func confirmationRequired(with playbackQueueLocationToConfirm: INPlaybackQueueLocation) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithPlaybackQueueLocationToConfirm:(INPlaybackQueueLocation) playbackQueueLocationToConfirm;
```

#### Return Value

A new [`INPlaybackQueueLocationResolutionResult`](../inplaybackqueuelocationresolutionresult.md) object.

#### Discussion

Use this method when you can’t resolve the parameter to a media item that’s similar, but not equal to, the one specified in the intent. Don’t use this method to resolve media items your app doesn’t support.

## Parameters

- `playbackQueueLocationToConfirm`: The value that resolves the request, but must be confirmed by the user.

## See Also

### Constants
- [class func success(with: INPlaybackQueueLocation) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves successfully matching the specified parameter.
- [enum INPlaybackQueueLocation](../inplaybackqueuelocation.md)
  Constants that describe the playback queue location for a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaybackqueuelocationresolutionresult/confirmationrequired(with:))*