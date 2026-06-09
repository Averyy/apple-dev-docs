# maxSupportedBufferedFrameCount

**Framework**: AVFoundation  
**Kind**: property

The maximum value supported for maxBufferedFrameCount.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
class var maxSupportedBufferedFrameCount: Int { get }
```

#### Discussion

This class property returns the system-imposed limit for buffered frame count to ensure optimal performance and memory usage in broadcast workflows. The limit is determined based on system capabilities.

## See Also

- [var maxBufferedFrameCount: Int](avcapturebroadcastvideooutput/maxbufferedframecount.md)
  This represents the maximum count of buffered frames. By default the value is 0, which means late frames are immediately dropped to maintain minimal latency.
- [var videoSettings: [String : Any]?](avcapturebroadcastvideooutput/videosettings.md)
  The current video output settings for the broadcast video output.
- [var maxBufferedFrameCount: Int](avcapturebroadcastvideooutput/maxbufferedframecount.md)
  This represents the maximum count of buffered frames. By default the value is 0, which means late frames are immediately dropped to maintain minimal latency.
- [func resetFrameBuffer()](avcapturebroadcastvideooutput/resetframebuffer.md)
  Tells the broadcast video output to reset the frame buffer and drop all currently buffered frames.
- [var droppedFrameReplacementPolicy: AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy](avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.property.md)
  The strategy used to replace dropped video frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/maxsupportedbufferedframecount)*