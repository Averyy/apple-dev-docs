# highResolutionStillImageDimensions

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The highest resolution still image the system can produce for this format.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0
- iPadOS 8.0+ - Deprecated in 16.0
- Mac Catalyst 14.0+ - Deprecated in 16.0

> **Deprecated**: Use [`supportedMaxPhotoDimensions`](../../avcapturedeviceformat/supportedmaxphotodimensions.md) instead.

## Declaration

```swift
var highResolutionStillImageDimensions: CMVideoDimensions { get }
```

```objc
@property (nonatomic, readonly) CMVideoDimensions highResolutionStillImageDimensions;
```

#### Discussion

Normally, the [`AVCaptureStillImageOutput`](../../avcapturestillimageoutput.md) class emits images with the same dimensions as the source [`AVCaptureDevice`](../../avcapturedevice.md) instance’s [`activeFormat`](../activeformat.md). However, if you set `highResolutionStillImageOutputEnabled` to [`true`](../../../Swift/true.md), [`AVCaptureStillImageOutput`](../../avcapturestillimageoutput.md) emits still images with its source [`AVCaptureDevice`](../../avcapturedevice.md) instance’s `activeFormat.highResolutionStillImageDimensions` dimensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/highresolutionstillimagedimensions)*