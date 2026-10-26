# init(rawPixelFormatType:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a photo settings object for RAW-format-only capture with the specified pixel format.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
convenience init(rawPixelFormatType: OSType)
```

```objc
+ (instancetype) photoSettingsWithRawPixelFormatType:(OSType) rawPixelFormatType;
```

#### Return Value

A new photo settings object.

#### Discussion

Use this initializer for RAW-only capture. To capture an image in both RAW format and a processed format (such as JPEG), use the [`init(rawPixelFormatType:processedFormat:)`](./init%28rawpixelformattype,processedformat%29.md) initializer instead.

Requesting RAW format capture adds requirements for other photo settings: for details, see the [`rawPhotoPixelFormatType`](./rawphotopixelformattype.md) property. The capture output validates these requirements when you call the [`capturePhoto(with:delegate:)`](../avcapturephotooutput/capturephoto%28with,delegate%29.md) method. If your settings and delegate don’t meet these requirements, that method raises an exception.

## Parameters

- `rawPixelFormatType`: The Bayer RAW pixel format type to use for capture. This value must be one of the format identifiers listed in the [`availableRawPhotoPixelFormatTypes`](../avcapturephotooutput/availablerawphotopixelformattypes-5fatm.md) array of your photo capture output.

## See Also

### Creating photo settings
- [convenience init(format: [String : Any]?)](./init%28format%29.md)
  Creates a photo settings object with the specified output format.
- [convenience init(rawPixelFormatType: OSType, processedFormat: [String : Any]?)](./init%28rawpixelformattype,processedformat%29.md)
  Creates a photo settings object for capture in both RAW format and a processed format.
- [convenience init(rawPixelFormatType: OSType, rawFileType: AVFileType?, processedFormat: [String : Any]?, processedFileType: AVFileType?)](./init%28rawpixelformattype,rawfiletype,processedformat,processedfiletype%29.md)
  Creates a photo settings object for capture in both RAW format and a processed format with the specified output file types.
- [convenience init(from: AVCapturePhotoSettings)](./init%28from%29.md)
  Creates a unique photo settings object, copying all settings values from the specified photo settings object.
- [+ photoSettings](./photosettings.md)
  Creates a photo settings object with default settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/init(rawpixelformattype:))*