# maxBufferedFrameCount

**Framework**: AVFoundation  
**Kind**: property

This represents the maximum count of buffered frames. By default the value is 0, which means late frames are immediately dropped to maintain minimal latency.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
var maxBufferedFrameCount: Int { get set }
```

#### Discussion

When set to a value greater than 0, the buffer absorbs minor timing jitter in the capture pipeline, reducing the possibility of dropping frames during temporary processing variations. Frames accumulate in the buffer up to the specified limit. Once the buffer reaches [`maxBufferedFrameCount`](avcapturebroadcastvideooutput/maxbufferedframecount.md), the oldest frame is removed to make room for each new incoming frame, maintaining a rolling window of buffered content.

Calling [`resetFrameBuffer()`](avcapturebroadcastvideooutput/resetframebuffer().md) clears all buffered frames and resets the buffer count back to 0, allowing the buffer to fill again from empty.

The maximum supported value can be retrieved using [`maxSupportedBufferedFrameCount`](avcapturebroadcastvideooutput/maxsupportedbufferedframecount.md). Setting a value higher than the maximum supported value will raise an `NSInvalidArgumentException`.

> **Note**: Enabling frame buffering (setting a value > 0) is useful for scenarios where temporary processing delays or timing variations are acceptable, such as when recording or archiving broadcast content. For live broadcast workflows where minimal latency is critical, keep the default value of 0.

## See Also

- [func resetFrameBuffer()](avcapturebroadcastvideooutput/resetframebuffer.md)
  Tells the broadcast video output to reset the frame buffer and drop all currently buffered frames.
- [class var maxSupportedBufferedFrameCount: Int](avcapturebroadcastvideooutput/maxsupportedbufferedframecount.md)
  The maximum value supported for maxBufferedFrameCount.
- [var videoSettings: [String : Any]?](avcapturebroadcastvideooutput/videosettings.md)
  The current video output settings for the broadcast video output.
- [class var maxSupportedBufferedFrameCount: Int](avcapturebroadcastvideooutput/maxsupportedbufferedframecount.md)
  The maximum value supported for maxBufferedFrameCount.
- [func resetFrameBuffer()](avcapturebroadcastvideooutput/resetframebuffer.md)
  Tells the broadcast video output to reset the frame buffer and drop all currently buffered frames.
- [var droppedFrameReplacementPolicy: AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy](avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.property.md)
  The strategy used to replace dropped video frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/maxbufferedframecount)*