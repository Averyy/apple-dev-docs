# currentVideoFrameRate

**Framework**: AVFoundation  
**Kind**: property

The current frame rate of the video track as it plays.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
var currentVideoFrameRate: Float { get }
```

#### Discussion

If the media type of the [`assetTrack`](avplayeritemtrack/assettrack.md) is [`video`](avmediatype/video.md), the property indicates the current frame rate of the track as it plays, in frames per second. If the item isn’t playing, or if the media type of the track isn’t video, the value of this property is `0.0`.

This property isn’t key-value observable.

## See Also

- [var videoFieldMode: String?](avplayeritemtrack/videofieldmode.md)
  A mode that specifies the handling of video frames that contain multiple fields.
- [let AVPlayerItemTrackVideoFieldModeDeinterlaceFields: String](avplayeritemtrackvideofieldmodedeinterlacefields.md)
  A video field mode that requests deinterlacing of video fields.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemtrack/currentvideoframerate)*