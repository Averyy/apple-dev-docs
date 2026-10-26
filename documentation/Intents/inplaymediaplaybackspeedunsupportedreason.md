# INPlayMediaPlaybackSpeedUnsupportedReason

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants that describe why the app can’t change the playback speed of the media item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum INPlayMediaPlaybackSpeedUnsupportedReason
```

```c
enum INPlayMediaPlaybackSpeedUnsupportedReason : NSInteger;
```

## Topics

### Constants
- [INPlayMediaPlaybackSpeedUnsupportedReason.belowMinimum](./inplaymediaplaybackspeedunsupportedreason/belowminimum.md)
  A reasson that indicates the requested playback speed is below the minimum supported playback speed.
- [INPlayMediaPlaybackSpeedUnsupportedReason.aboveMaximum](./inplaymediaplaybackspeedunsupportedreason/abovemaximum.md)
  A reason that indicates the requested playback speed is above the maximum supported playback speed.
### Initializers
- [init?(rawValue: Int)](./inplaymediaplaybackspeedunsupportedreason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating a Resolution Result
- [init(doubleResolutionResult: INDoubleResolutionResult)](./inplaymediaplaybackspeedresolutionresult/init%28doubleresolutionresult%29.md)
  Creates an object whose resolution involves successfulling changing the playback speed of a media item.
- [class func unsupported(forReason: INPlayMediaPlaybackSpeedUnsupportedReason) -> Self](./inplaymediaplaybackspeedresolutionresult/unsupported%28forreason%29.md)
  Creates an object whose resolution requires the user to confirm the request, because your app is unable to support the current request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inplaymediaplaybackspeedunsupportedreason)*