# unsupported(forReason:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires the user to confirm the request, because your app is unable to support the current request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func unsupported(forReason reason: INPlayMediaPlaybackSpeedUnsupportedReason) -> Self
```

```objc
+ (instancetype) unsupportedForReason:(INPlayMediaPlaybackSpeedUnsupportedReason) reason;
```

## Return Value

A new [`INPlayMediaPlaybackSpeedResolutionResult`](../inplaymediaplaybackspeedresolutionresult.md) object.

## Discussion

Use this method to create a resolution result object when your app doesn’t support the intent parameter for the specified reason.

## Parameters

- `reason`: The reason that changing the playback speed of the media item isn’t supported.

## See Also

### Creating a Resolution Result
- [init(doubleResolutionResult: INDoubleResolutionResult)](./init%28doubleresolutionresult%29.md)
  Creates an object whose resolution involves successfulling changing the playback speed of a media item.
- [enum INPlayMediaPlaybackSpeedUnsupportedReason](../inplaymediaplaybackspeedunsupportedreason.md)
  Constants that describe why the app can’t change the playback speed of the media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaplaybackspeedresolutionresult/unsupported(forreason:))*