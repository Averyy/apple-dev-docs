# init(sampleBufferDisplayLayer:playbackDelegate:)

**Framework**: AVKit  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithSampleBufferDisplayLayer:(AVSampleBufferDisplayLayer *) sampleBufferDisplayLayer playbackDelegate:(id<AVPictureInPictureSampleBufferPlaybackDelegate>) playbackDelegate;
```

## Parameters

- `sampleBufferDisplayLayer`: The sample buffer display layer to show in Picture in Picture.
- `playbackDelegate`: The playback delegate object that responds to Picture in Picture events.

## See Also

### Creating a content source
- [init(playerLayer: AVPlayerLayer)](./init%28playerlayer%29.md)
  Creates a content source with a player layer.
- [init(activeVideoCallSourceView: UIView, contentViewController: AVPictureInPictureVideoCallViewController)](./init%28activevideocallsourceview,contentviewcontroller%29.md)
  Creates a content source with an active video call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/init(samplebufferdisplaylayer:playbackdelegate:))*