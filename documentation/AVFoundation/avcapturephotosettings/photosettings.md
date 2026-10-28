# photoSettings

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Creates a photo settings object with default settings.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```objc
+ (instancetype) photoSettings;
```

## Return Value

A new photo settings object.

## Discussion

Capturing a photo with default settings delivers a single image in JPEG format.

Requesting capture in a processed format (such as JPEG) adds requirements for other photo settings: for details, see the [`format`](./format.md) property. The capture output validates these requirement when you call the [`capturePhoto(with:delegate:)`](../avcapturephotooutput/capturephoto%28with,delegate%29.md) method. If your settings and delegate don’t meet these requirement, that method raises an exception.

## See Also

### Creating photo settings
- [convenience init(format: [String : Any]?)](./init%28format%29.md)
  Creates a photo settings object with the specified output format.
- [convenience init(rawPixelFormatType: OSType)](./init%28rawpixelformattype%29.md)
  Creates a photo settings object for RAW-format-only capture with the specified pixel format.
- [convenience init(rawPixelFormatType: OSType, processedFormat: [String : Any]?)](./init%28rawpixelformattype,processedformat%29.md)
  Creates a photo settings object for capture in both RAW format and a processed format.
- [convenience init(rawPixelFormatType: OSType, rawFileType: AVFileType?, processedFormat: [String : Any]?, processedFileType: AVFileType?)](./init%28rawpixelformattype,rawfiletype,processedformat,processedfiletype%29.md)
  Creates a photo settings object for capture in both RAW format and a processed format with the specified output file types.
- [convenience init(from: AVCapturePhotoSettings)](./init%28from%29.md)
  Creates a unique photo settings object, copying all settings values from the specified photo settings object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/photosettings)*