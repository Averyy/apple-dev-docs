# isMultiCamSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether a multi-camera capture session supports this format.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isMultiCamSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isMultiCamSupported) BOOL multiCamSupported;
```

## Discussion

When performing single-camera capture using [`AVCaptureSession`](../../avcapturesession.md), you may set any of the device’s formats as its [`activeFormat`](../activeformat.md). However, when using [`AVCaptureMultiCamSession`](../../avcapturemulticamsession.md), you may only set the device’s format to one in which [`isMultiCamSupported`](./ismulticamsupported.md) is [`true`](../../../Swift/true.md). Only this limited subset of capture formats can run sustainably in a multi-camera capture scenario.

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
- [var isVideoHDRSupported: Bool](./isvideohdrsupported.md)
  A Boolean value that indicates whether the format supports high dynamic range streaming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/ismulticamsupported)*