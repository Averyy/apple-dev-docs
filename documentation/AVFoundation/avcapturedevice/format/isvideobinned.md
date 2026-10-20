# isVideoBinned

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the format produces video data in a binned format.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isVideoBinned: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isVideoBinned) BOOL videoBinned;
```

#### Discussion

Binning is a pixel-combining process which can result in greater low light sensitivity at the cost of reduced resolution.

## See Also

### Determining video capture support
- [var isAutoVideoFrameRateSupported: Bool](./isautovideoframeratesupported.md)
  A Boolean value that Indicates whether the format supports performing automatic video frame rate adjustments.
- [var videoSupportedFrameRateRanges: [AVFrameRateRange]](./videosupportedframerateranges.md)
  A list of frame rate ranges that a format supports.
- [class AVFrameRateRange](../../avframeraterange.md)
  An immutable type that represents a range of valid frame rates.
- [var isVideoHDRSupported: Bool](./isvideohdrsupported.md)
  A Boolean value that indicates whether the format supports high dynamic range streaming.
- [var isMultiCamSupported: Bool](./ismulticamsupported.md)
  A Boolean value that indicates whether a multi-camera capture session supports this format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/isvideobinned)*