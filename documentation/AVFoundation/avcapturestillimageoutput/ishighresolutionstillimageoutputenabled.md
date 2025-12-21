# isHighResolutionStillImageOutputEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the receiver should emit still images at the highest resolution supported by its source `AVCaptureDevice` objects `activeFormat` property.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 14.0+
- macOS 10.14+

## Declaration

```swift
var isHighResolutionStillImageOutputEnabled: Bool { get set }
```

#### Discussion

By default, `AVCaptureStillImageOutput` emits images with the same dimensions as its source [`AVCaptureDevice`](avcapturedevice.md) instance’s `activeFormat.formatDescription`.  However, if you set this property to [`true`](https://developer.apple.com/documentation/Swift/true), the receiver emits still images at the capture device’s [`highResolutionStillImageDimensions`](avcapturedevice/format/highresolutionstillimagedimensions.md) value.

> **Note**:  If you enable video stabilization by setting `preferredVideoStabilizationMode` to [`true`](https://developer.apple.com/documentation/Swift/true) for any output, the high resolution still images emitted by `AVCaptureStillImageOutput` may be smaller by 10% or more.

## See Also

- [var availableImageDataCVPixelFormatTypes: [NSNumber]](avcapturestillimageoutput/availableimagedatacvpixelformattypes.md)
  The supported image pixel formats that can be specified as output settings.
- [var availableImageDataCodecTypes: [AVVideoCodecType]](avcapturestillimageoutput/availableimagedatacodectypes.md)
  The supported image codec formats that can be specified as output settings.
- [var outputSettings: [String : Any]](avcapturestillimageoutput/outputsettings.md)
  The compression settings for the output.
- [Video settings](video-settings.md)
  Configure video processing settings using standard key and value constants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/ishighresolutionstillimageoutputenabled)*