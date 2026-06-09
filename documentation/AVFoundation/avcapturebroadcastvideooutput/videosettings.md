# videoSettings

**Framework**: AVFoundation  
**Kind**: property

The current video output settings for the broadcast video output.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
var videoSettings: [String : Any]? { get }
```

#### Discussion

This read-only property reports the actual video format and output settings currently being used for broadcast video output. The value is a dictionary containing metadata descriptors conforming to SMPTE ST 377 (Material Exchange Format) using Universal Labels (ULs) for professional broadcast interoperability.

The settings reflect the format negotiated between the camera capture pipeline and the connected broadcast video destination, taking into account:

- Camera native capture format capabilities
- Connected broadcast video destination capabilities
- System performance constraints
- Display transport bandwidth limitations

This property will return `nil` when no broadcast video destination is connected or when the output pipeline is not active.

> ❗ **Important**: The reported settings reflect the actual negotiated format and may differ from the camera’s native capture format due to broadcast hardware constraints.

## See Also

- [var maxBufferedFrameCount: Int](avcapturebroadcastvideooutput/maxbufferedframecount.md)
  This represents the maximum count of buffered frames. By default the value is 0, which means late frames are immediately dropped to maintain minimal latency.
- [class var maxSupportedBufferedFrameCount: Int](avcapturebroadcastvideooutput/maxsupportedbufferedframecount.md)
  The maximum value supported for maxBufferedFrameCount.
- [func resetFrameBuffer()](avcapturebroadcastvideooutput/resetframebuffer.md)
  Tells the broadcast video output to reset the frame buffer and drop all currently buffered frames.
- [var droppedFrameReplacementPolicy: AVCaptureBroadcastVideoOutput.DroppedFrameReplacementPolicy](avcapturebroadcastvideooutput/droppedframereplacementpolicy-swift.property.md)
  The strategy used to replace dropped video frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturebroadcastvideooutput/videosettings)*