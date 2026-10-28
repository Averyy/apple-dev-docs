# videoSupportedFrameRateRanges

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A list of frame rate ranges that a format supports.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var videoSupportedFrameRateRanges: [AVFrameRateRange] { get }
```

```objc
@property (nonatomic, readonly) NSArray<AVFrameRateRange *> * videoSupportedFrameRateRanges;
```

## Discussion

The value is an array of [`AVFrameRateRange`](../../avframeraterange.md) objects, one for each of the format’s supported video frame rate ranges.

## See Also

### Determining video capture support
- [var isAutoVideoFrameRateSupported: Bool](./isautovideoframeratesupported.md)
  A Boolean value that Indicates whether the format supports performing automatic video frame rate adjustments.
- [class AVFrameRateRange](../../avframeraterange.md)
  An immutable type that represents a range of valid frame rates.
- [var isVideoBinned: Bool](./isvideobinned.md)
  A Boolean value that indicates whether the format produces video data in a binned format.
- [var isVideoHDRSupported: Bool](./isvideohdrsupported.md)
  A Boolean value that indicates whether the format supports high dynamic range streaming.
- [var isMultiCamSupported: Bool](./ismulticamsupported.md)
  A Boolean value that indicates whether a multi-camera capture session supports this format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videosupportedframerateranges)*