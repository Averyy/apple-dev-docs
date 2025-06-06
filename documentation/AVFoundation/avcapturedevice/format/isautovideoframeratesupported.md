# isAutoVideoFrameRateSupported

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that Indicates whether the format supports performing automatic video frame rate adjustments.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
var isAutoVideoFrameRateSupported: Bool { get }
```

#### Discussion

This property determines whether you can enable a capture device’s [`isAutoVideoFrameRateEnabled`](avcapturedevice/isautovideoframerateenabled.md) property.

## See Also

- [var videoSupportedFrameRateRanges: [AVFrameRateRange]](avcapturedevice/format/videosupportedframerateranges.md)
  A list of frame rate ranges that a format supports.
- [class AVFrameRateRange](avframeraterange.md)
  An immutable type that represents a range of valid frame rates.
- [var isVideoBinned: Bool](avcapturedevice/format/isvideobinned.md)
  A Boolean value that indicates whether the format produces video data in a binned format.
- [var isVideoHDRSupported: Bool](avcapturedevice/format/isvideohdrsupported.md)
  A Boolean value that indicates whether the format supports high dynamic range streaming.
- [var isMultiCamSupported: Bool](avcapturedevice/format/ismulticamsupported.md)
  A Boolean value that indicates whether a multi-camera capture session supports this format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/isautovideoframeratesupported)*