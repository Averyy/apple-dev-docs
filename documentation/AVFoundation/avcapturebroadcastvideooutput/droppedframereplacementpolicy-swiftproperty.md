# droppedFrameReplacementPolicy

**Framework**: AVFoundation  
**Kind**: property

The strategy used to replace dropped video frames.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
var droppedFrameReplacementPolicy: AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy { get set }
```

#### Discussion

This property determines how the broadcast video output handles dropped frames. The default value is `AVCaptureBroadcastVideoOutputDroppedFrameReplacementPolicyRepeatPreviousFrame`.

## See Also

- [AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy](avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.enum.md)
  Constants indicating the replacement policy when a video frame is dropped.
- [var videoSettings: [String : Any]?](avcapturebroadcastvideooutput/videosettings.md)
  The current video output settings for the broadcast video output.
- [var maxBufferedFrameCount: Int](avcapturebroadcastvideooutput/maxbufferedframecount.md)
  This represents the maximum count of buffered frames. By default the value is 0, which means late frames are immediately dropped to maintain minimal latency.
- [class var maxSupportedBufferedFrameCount: Int](avcapturebroadcastvideooutput/maxsupportedbufferedframecount.md)
  The maximum value supported for maxBufferedFrameCount.
- [func resetFrameBuffer()](avcapturebroadcastvideooutput/resetframebuffer.md)
  Tells the broadcast video output to reset the frame buffer and drop all currently buffered frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.property)*