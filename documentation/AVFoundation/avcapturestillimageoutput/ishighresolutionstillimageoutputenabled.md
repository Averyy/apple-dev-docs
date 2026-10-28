# isHighResolutionStillImageOutputEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver should emit still images at the highest resolution supported by its source `AVCaptureDevice` objects `activeFormat` property.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0
- Mac Catalyst 14.0+ - Deprecated in 13.1
- macOS 10.14+ - Deprecated in 10.15

## Declaration

```swift
var isHighResolutionStillImageOutputEnabled: Bool { get set }
```

```objc
@property (nonatomic, getter=isHighResolutionStillImageOutputEnabled) BOOL highResolutionStillImageOutputEnabled;
```

## Discussion

By default, `AVCaptureStillImageOutput` emits images with the same dimensions as its source [`AVCaptureDevice`](../avcapturedevice.md) instance’s `activeFormat.formatDescription`.  However, if you set this property to [`true`](../../Swift/true.md), the receiver emits still images at the capture device’s [`highResolutionStillImageDimensions`](../avcapturedevice/format/highresolutionstillimagedimensions.md) value.

> **Note**:  If you enable video stabilization by setting `preferredVideoStabilizationMode` to [`true`](../../Swift/true.md) for any output, the high resolution still images emitted by `AVCaptureStillImageOutput` may be smaller by 10% or more.

## See Also

### Configuring image settings
- [var availableImageDataCVPixelFormatTypes: [NSNumber]](./availableimagedatacvpixelformattypes.md)
  The supported image pixel formats that can be specified as output settings.
- [var availableImageDataCodecTypes: [AVVideoCodecType]](./availableimagedatacodectypes.md)
  The supported image codec formats that can be specified as output settings.
- [var outputSettings: [String : Any]](./outputsettings.md)
  The compression settings for the output.
- [Video settings](../video-settings.md)
  Configure video processing settings using standard key and value constants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/ishighresolutionstillimageoutputenabled)*