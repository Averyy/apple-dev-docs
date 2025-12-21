# AVFrameRateRange

**Framework**: AVFoundation  
**Kind**: class

An immutable type that represents a range of valid frame rates.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 14.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class AVFrameRateRange
```

#### Overview

An AVFrameRateRange object is immutable.

An [`AVCaptureDevice.Format`](avcapturedevice/format.md) object wraps a CMFormatDescription and expresses a range of valid video frame rates as an array of `AVFrameRateRange` objects.

An [`AVCaptureDevice`](avcapturedevice.md) object uses `AVCaptureDeviceFormat` to describe the formats it supports and the currently-active format.

## Topics

### Accessing properties
- [var maxFrameDuration: CMTime](avframeraterange/maxframeduration.md)
  The maximum frame duration supported by the range.
- [var maxFrameRate: Float64](avframeraterange/maxframerate.md)
  The maximum frame rate supported by the range.
- [var minFrameDuration: CMTime](avframeraterange/minframeduration.md)
  The minimum frame duration supported by the range.
- [var minFrameRate: Float64](avframeraterange/minframerate.md)
  The minimum frame rate supported by the range.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var isAutoVideoFrameRateSupported: Bool](avcapturedevice/format/isautovideoframeratesupported.md)
  A Boolean value that Indicates whether the format supports performing automatic video frame rate adjustments.
- [var videoSupportedFrameRateRanges: [AVFrameRateRange]](avcapturedevice/format/videosupportedframerateranges.md)
  A list of frame rate ranges that a format supports.
- [var isVideoBinned: Bool](avcapturedevice/format/isvideobinned.md)
  A Boolean value that indicates whether the format produces video data in a binned format.
- [var isVideoHDRSupported: Bool](avcapturedevice/format/isvideohdrsupported.md)
  A Boolean value that indicates whether the format supports high dynamic range streaming.
- [var isMultiCamSupported: Bool](avcapturedevice/format/ismulticamsupported.md)
  A Boolean value that indicates whether a multi-camera capture session supports this format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avframeraterange)*