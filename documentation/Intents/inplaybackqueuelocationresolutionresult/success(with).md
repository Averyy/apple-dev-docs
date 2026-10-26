# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves successfully matching the specified parameter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func success(with resolvedPlaybackQueueLocation: INPlaybackQueueLocation) -> Self
```

```objc
+ (instancetype) successWithResolvedPlaybackQueueLocation:(INPlaybackQueueLocation) resolvedPlaybackQueueLocation;
```

#### Return Value

A new [`INPlaybackQueueLocationResolutionResult`](../inplaybackqueuelocationresolutionresult.md) object.

#### Discussion

Use this method to create a result object when you’re able to change the playback queue location for a media item.

## Parameters

- `resolvedPlaybackQueueLocation`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Constants
- [class func confirmationRequired(with: INPlaybackQueueLocation) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires the user to confirm the value before proceeding.
- [enum INPlaybackQueueLocation](../inplaybackqueuelocation.md)
  Constants that describe the playback queue location for a media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaybackqueuelocationresolutionresult/success(with:))*