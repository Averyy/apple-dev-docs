# availableImageDataCVPixelFormatTypes

**Framework**: AVFoundation  
**Kind**: property

The supported image pixel formats that can be specified as output settings.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
var availableImageDataCVPixelFormatTypes: [NSNumber] { get }
```

#### Discussion

The value of this property is an array of `NSNumber` objects that you can use as values for the [`kCVPixelBufferPixelFormatTypeKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferPixelFormatTypeKey) in the [`outputSettings`](avcapturestillimageoutput/outputsettings.md) property.

## See Also

- [var isHighResolutionStillImageOutputEnabled: Bool](avcapturestillimageoutput/ishighresolutionstillimageoutputenabled.md)
  A Boolean value that indicates whether the receiver should emit still images at the highest resolution supported by its source `AVCaptureDevice` objects `activeFormat` property.
- [var availableImageDataCodecTypes: [AVVideoCodecType]](avcapturestillimageoutput/availableimagedatacodectypes.md)
  The supported image codec formats that can be specified as output settings.
- [var outputSettings: [String : Any]](avcapturestillimageoutput/outputsettings.md)
  The compression settings for the output.
- [Video settings](video-settings.md)
  Configure video processing settings using standard key and value constants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/availableimagedatacvpixelformattypes)*