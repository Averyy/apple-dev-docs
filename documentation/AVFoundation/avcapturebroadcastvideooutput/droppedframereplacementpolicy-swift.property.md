# droppedFrameReplacementPolicy

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The strategy used to replace dropped video frames.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
var droppedFrameReplacementPolicy: AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy { get set }
```

```objc
@property (nonatomic) AVCaptureBroadcastVideoOutputDroppedFrameReplacementPolicy droppedFrameReplacementPolicy;
```

## Discussion

This property determines how the broadcast video output handles dropped frames. The default value is `AVCaptureBroadcastVideoOutputDroppedFrameReplacementPolicyRepeatPreviousFrame`.

## See Also

### Related Documentation
- [AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy](./droppedframereplacementpolicy-swift.enum.md)
  Constants indicating the replacement policy when a video frame is dropped.
### Managing Video Output
- [var videoSettings: [String : Any]?](./videosettings.md)
  The current video output settings for the broadcast video output.
- [var maxBufferedFrameCount: Int](./maxbufferedframecount.md)
  This represents the maximum count of buffered frames. By default the value is 0, which means late frames are immediately dropped to maintain minimal latency.
- [class var maxSupportedBufferedFrameCount: Int](./maxsupportedbufferedframecount.md)
  The maximum value supported for maxBufferedFrameCount.
- [func resetFrameBuffer()](./resetframebuffer%28%29.md)
  Tells the broadcast video output to reset the frame buffer and drop all currently buffered frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.property)*