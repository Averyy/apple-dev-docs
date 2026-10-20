# availableImageDataCVPixelFormatTypes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The supported image pixel formats that can be specified as output settings.

**Availability**:
- iOS 4.0+ - Deprecated in 10.0
- iPadOS 4.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.7+ - Deprecated in 10.15

> **Deprecated**: Use AVCapturePhotoOutput instead.

## Declaration

```swift
var availableImageDataCVPixelFormatTypes: [NSNumber] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * availableImageDataCVPixelFormatTypes;
```

#### Discussion

The value of this property is an array of `NSNumber` objects that you can use as values for the [`kCVPixelBufferPixelFormatTypeKey`](../../CoreVideo/kcvpixelbufferpixelformattypekey.md) in the [`outputSettings`](./outputsettings.md) property.

## See Also

### Configuring image settings
- [var isHighResolutionStillImageOutputEnabled: Bool](./ishighresolutionstillimageoutputenabled.md)
  A Boolean value that indicates whether the receiver should emit still images at the highest resolution supported by its source `AVCaptureDevice` objects `activeFormat` property.
- [var availableImageDataCodecTypes: [AVVideoCodecType]](./availableimagedatacodectypes.md)
  The supported image codec formats that can be specified as output settings.
- [var outputSettings: [String : Any]](./outputsettings.md)
  The compression settings for the output.
- [Video settings](../video-settings.md)
  Configure video processing settings using standard key and value constants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/availableimagedatacvpixelformattypes)*