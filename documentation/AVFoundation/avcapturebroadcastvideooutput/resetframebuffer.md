# resetFrameBuffer()

**Framework**: AVFoundation  
**Kind**: method

Tells the broadcast video output to reset the frame buffer and drop all currently buffered frames.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
func resetFrameBuffer()
```

#### Discussion

This method can be called when buffered video frames should be dropped. This will force all those frames to be dropped and reset the buffered frame count to 0.

Use this method in scenarios where you need to clear pending frames, such as:

- **Pausing or stopping broadcast**: Drop pending frames that should not be transmitted
- **Reducing accumulated latency**: If buffering has built up significant delay, reset to return to real-time output

## See Also

- [var maxBufferedFrameCount: Int](avcapturebroadcastvideooutput/maxbufferedframecount.md)
  This represents the maximum count of buffered frames. By default the value is 0, which means late frames are immediately dropped to maintain minimal latency.
- [var videoSettings: [String : Any]?](avcapturebroadcastvideooutput/videosettings.md)
  The current video output settings for the broadcast video output.
- [var maxBufferedFrameCount: Int](avcapturebroadcastvideooutput/maxbufferedframecount.md)
  This represents the maximum count of buffered frames. By default the value is 0, which means late frames are immediately dropped to maintain minimal latency.
- [class var maxSupportedBufferedFrameCount: Int](avcapturebroadcastvideooutput/maxsupportedbufferedframecount.md)
  The maximum value supported for maxBufferedFrameCount.
- [var droppedFrameReplacementPolicy: AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy](avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.property.md)
  The strategy used to replace dropped video frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/resetframebuffer())*