# init(sampleBufferDisplayLayer:playbackDelegate:)

**Framework**: AVKit  
**Kind**: init

Creates a content source with a sample buffer display layer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
init(sampleBufferDisplayLayer: AVSampleBufferDisplayLayer, playbackDelegate: any AVPictureInPictureSampleBufferPlaybackDelegate)
```

## Parameters

- `sampleBufferDisplayLayer`: The sample buffer display layer to show in Picture in Picture.
- `playbackDelegate`: The playback delegate object that responds to Picture in Picture events.

## See Also

- [init(playerLayer: AVPlayerLayer)](avpictureinpicturecontroller/contentsource-swift.class/init(playerlayer:).md)
  Creates a content source with a player layer.
- [init(activeVideoCallSourceView: UIView, contentViewController: AVPictureInPictureVideoCallViewController)](avpictureinpicturecontroller/contentsource-swift.class/init(activevideocallsourceview:contentviewcontroller:).md)
  Creates a content source with an active video call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/init(samplebufferdisplaylayer:playbackdelegate:))*