# isVideoHDRSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the format supports high dynamic range streaming.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isVideoHDRSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isVideoHDRSupported) BOOL videoHDRSupported;
```

## See Also

### Determining video capture support
- [var isAutoVideoFrameRateSupported: Bool](./isautovideoframeratesupported.md)
  A Boolean value that Indicates whether the format supports performing automatic video frame rate adjustments.
- [var videoSupportedFrameRateRanges: [AVFrameRateRange]](./videosupportedframerateranges.md)
  A list of frame rate ranges that a format supports.
- [class AVFrameRateRange](../../avframeraterange.md)
  An immutable type that represents a range of valid frame rates.
- [var isVideoBinned: Bool](./isvideobinned.md)
  A Boolean value that indicates whether the format produces video data in a binned format.
- [var isMultiCamSupported: Bool](./ismulticamsupported.md)
  A Boolean value that indicates whether a multi-camera capture session supports this format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/isvideohdrsupported)*