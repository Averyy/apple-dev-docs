# init(doubleResolutionResult:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates an object whose resolution involves successfulling changing the playback speed of a media item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(doubleResolutionResult: INDoubleResolutionResult)
```

```objc
- (instancetype) initWithDoubleResolutionResult:(INDoubleResolutionResult *) doubleResolutionResult;
```

## Return Value

A new [`INPlayMediaPlaybackSpeedResolutionResult`](../inplaymediaplaybackspeedresolutionresult.md) object.

## Discussion

Use this method to create a result object when you’re able to change the playback speed of a media item.

## Parameters

- `doubleResolutionResult`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result
- [class func unsupported(forReason: INPlayMediaPlaybackSpeedUnsupportedReason) -> Self](./unsupported%28forreason%29.md)
  Creates an object whose resolution requires the user to confirm the request, because your app is unable to support the current request.
- [enum INPlayMediaPlaybackSpeedUnsupportedReason](../inplaymediaplaybackspeedunsupportedreason.md)
  Constants that describe why the app can’t change the playback speed of the media item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaplaybackspeedresolutionresult/init(doubleresolutionresult:))*