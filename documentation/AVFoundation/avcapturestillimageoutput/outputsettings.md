# outputSettings

**Framework**: AVFoundation  
**Kind**: property

The compression settings for the output.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
var outputSettings: [String : Any] { get set }
```

#### Discussion

Use [`availableImageDataCVPixelFormatTypes`](avcapturestillimageoutput/availableimagedatacvpixelformattypes.md) and [`availableImageDataCodecTypes`](avcapturestillimageoutput/availableimagedatacodectypes.md) to determine what codec keys and pixel formats are supported.

In iOS, the only currently supported keys are [`AVVideoCodecKey`](avvideocodeckey.md) and [`kCVPixelBufferPixelFormatTypeKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferPixelFormatTypeKey). These keys are mutually exclusive—only one may be present. The recommended values are [`kCMVideoCodecType_JPEG`](https://developer.apple.com/documentation/CoreMedia/kCMVideoCodecType_JPEG) for [`AVVideoCodecKey`](avvideocodeckey.md) and [`kCVPixelFormatType_420YpCbCr8BiPlanarFullRange`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_420YpCbCr8BiPlanarFullRange) and [`kCVPixelFormatType_32BGRA`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_32BGRA) for [`kCVPixelBufferPixelFormatTypeKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferPixelFormatTypeKey).

In iOS 6.0 and later, the [`AVVideoQualityKey`](avvideoqualitykey.md) is supported, and may only be used when [`AVVideoCodecKey`](avvideocodeckey.md) is set to [`AVVideoCodecJPEG`](avvideocodecjpeg.md).

## See Also

- [var isHighResolutionStillImageOutputEnabled: Bool](avcapturestillimageoutput/ishighresolutionstillimageoutputenabled.md)
  A Boolean value that indicates whether the receiver should emit still images at the highest resolution supported by its source `AVCaptureDevice` objects `activeFormat` property.
- [var availableImageDataCVPixelFormatTypes: [NSNumber]](avcapturestillimageoutput/availableimagedatacvpixelformattypes.md)
  The supported image pixel formats that can be specified as output settings.
- [var availableImageDataCodecTypes: [AVVideoCodecType]](avcapturestillimageoutput/availableimagedatacodectypes.md)
  The supported image codec formats that can be specified as output settings.
- [Video settings](video-settings.md)
  Configure video processing settings using standard key and value constants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/outputsettings)*