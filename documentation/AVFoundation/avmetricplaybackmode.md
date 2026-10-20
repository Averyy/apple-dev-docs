# AVMetricPlaybackMode

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

These constants are the possible playback modes returned by the property “mode” on AVMetricPlaybackModeSwitchEvent

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum AVMetricPlaybackMode
```

```c
enum AVMetricPlaybackMode : NSInteger;
```

## Topics

### Creating a playback mode
- [init?(rawValue: Int)](./avmetricplaybackmode/init%28rawvalue%29.md)
### Playback modes
- [AVMetricPlaybackMode.local](./avmetricplaybackmode/local.md)
  Indicates that playback is local.
- [AVMetricPlaybackMode.airPlayVideo](./avmetricplaybackmode/airplayvideo.md)
  Indicates that playback is via AirPlay Video.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Playback mode
- [class AVMetricPlaybackModeSwitchEvent](./avmetricplaybackmodeswitchevent.md)
  Represents a change in playback state, entering one of AVMetricPlaybackMode


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetricplaybackmode)*