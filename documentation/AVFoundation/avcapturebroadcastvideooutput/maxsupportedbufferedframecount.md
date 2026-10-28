# maxSupportedBufferedFrameCount

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Type Property

The maximum value supported for maxBufferedFrameCount.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
class var maxSupportedBufferedFrameCount: Int { get }
```

```objc
@property (class, nonatomic, readonly) NSInteger maxSupportedBufferedFrameCount;
```

## Discussion

This class property returns the system-imposed limit for buffered frame count to ensure optimal performance and memory usage in broadcast workflows. The limit is determined based on system capabilities.

## See Also

### Related Documentation
- [var maxBufferedFrameCount: Int](./maxbufferedframecount.md)
  This represents the maximum count of buffered frames. By default the value is 0, which means late frames are immediately dropped to maintain minimal latency.
### Managing Video Output
- [var videoSettings: [String : Any]?](./videosettings.md)
  The current video output settings for the broadcast video output.
- [var maxBufferedFrameCount: Int](./maxbufferedframecount.md)
  This represents the maximum count of buffered frames. By default the value is 0, which means late frames are immediately dropped to maintain minimal latency.
- [func resetFrameBuffer()](./resetframebuffer%28%29.md)
  Tells the broadcast video output to reset the frame buffer and drop all currently buffered frames.
- [var droppedFrameReplacementPolicy: AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy](./droppedframereplacementpolicy-swift.property.md)
  The strategy used to replace dropped video frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/maxsupportedbufferedframecount)*