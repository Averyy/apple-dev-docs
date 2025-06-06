# videoFrameRateRangeForReactionEffectsInProgress

**Framework**: AVFoundation  
**Kind**: property

Indicates the minimum and maximum frame rates available when a reaction effect runs.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
var videoFrameRateRangeForReactionEffectsInProgress: AVFrameRateRange? { get }
```

#### Discussion

Unlike other video effects, enabling reaction effects doesn’t limit the stream’s frame rate because most of the time the system isn’t rendering the effect. The frame rate only ramps down when the system renders a reaction on the stream.

## See Also

- [var reactionEffectsSupported: Bool](avcapturedevice/format/reactioneffectssupported.md)
  A Boolean value that indicates whether the device supports reaction effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videoframeraterangeforreactioneffectsinprogress)*