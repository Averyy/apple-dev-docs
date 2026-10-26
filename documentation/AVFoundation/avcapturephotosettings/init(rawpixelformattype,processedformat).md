# init(rawPixelFormatType:processedFormat:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a photo settings object for capture in both RAW format and a processed format.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
convenience init(rawPixelFormatType: OSType, processedFormat: [String : Any]?)
```

```objc
+ (instancetype) photoSettingsWithRawPixelFormatType:(OSType) rawPixelFormatType processedFormat:(NSDictionary<NSString *,id> *) processedFormat;
```

#### Return Value

A new photo settings object.

#### Discussion

Use this initializer to capture an image in both RAW format and a processed format (such as JPEG). For RAW-only capture, use the [`init(rawPixelFormatType:)`](./init%28rawpixelformattype%29.md) initializer instead.

Requesting both formats adds requirements for other photo settings: see the [`format`](./format.md) property for processed format requirements and the [`rawPhotoPixelFormatType`](./rawphotopixelformattype.md) property for RAW format requirements. The capture output validates these requirements when you call the [`capturePhoto(with:delegate:)`](../avcapturephotooutput/capturephoto%28with,delegate%29.md) method. If your settings and delegate don’t meet these requirements, that method raises an exception.

## Parameters

- `rawPixelFormatType`: The Bayer RAW pixel format type to use for capture. This value must be one of the format identifiers listed in the [`availableRawPhotoPixelFormatTypes`](../avcapturephotooutput/availablerawphotopixelformattypes-5fatm.md) array of your photo capture output.
- `processedFormat`: A dictionary of Core Video pixel buffer attributes or AVFoundation video settings constants (see `Video Settings`).

  To capture a photo in an uncompressed format, such as 420f, 420v, or BGRA, set the key [`kCVPixelBufferPixelFormatTypeKey`](../../CoreVideo/kcvpixelbufferpixelformattypekey.md) in the `format` dictionary. The corresponding value must be one of the pixel format identifiers listed in the [`availablePhotoPixelFormatTypes`](../avcapturephotooutput/availablephotopixelformattypes-6eyb.md) array of your photo capture output.

  To capture a photo in a compressed format, such as JPEG, set the key [`AVVideoCodecKey`](../avvideocodeckey.md) in the `format` dictionary. The corresponding value must be one of the codec identifiers listed in the [`availablePhotoCodecTypes`](../avcapturephotooutput/availablephotocodectypes.md) array of your photo capture output. For a compressed format, you can also specify a compression level with the key [`AVVideoQualityKey`](../avvideoqualitykey.md).

## See Also

### Creating photo settings
- [convenience init(format: [String : Any]?)](./init%28format%29.md)
  Creates a photo settings object with the specified output format.
- [convenience init(rawPixelFormatType: OSType)](./init%28rawpixelformattype%29.md)
  Creates a photo settings object for RAW-format-only capture with the specified pixel format.
- [convenience init(rawPixelFormatType: OSType, rawFileType: AVFileType?, processedFormat: [String : Any]?, processedFileType: AVFileType?)](./init%28rawpixelformattype,rawfiletype,processedformat,processedfiletype%29.md)
  Creates a photo settings object for capture in both RAW format and a processed format with the specified output file types.
- [convenience init(from: AVCapturePhotoSettings)](./init%28from%29.md)
  Creates a unique photo settings object, copying all settings values from the specified photo settings object.
- [+ photoSettings](./photosettings.md)
  Creates a photo settings object with default settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/init(rawpixelformattype:processedformat:))*