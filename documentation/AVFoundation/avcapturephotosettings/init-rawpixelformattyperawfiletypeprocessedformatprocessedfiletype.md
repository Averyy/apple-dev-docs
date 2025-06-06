# init(rawPixelFormatType:rawFileType:processedFormat:processedFileType:)

**Framework**: AVFoundation  
**Kind**: init

Creates a photo settings object for capture in both RAW format and a processed format with the specified output file types.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
convenience init(rawPixelFormatType: OSType, rawFileType: AVFileType?, processedFormat: [String : Any]?, processedFileType: AVFileType?)
```

#### Return Value

A new photo settings object.

#### Discussion

Use this initializer to capture an image in both RAW format and a processed format (such as JPEG). For RAW-only capture, use the [`init(rawPixelFormatType:)`](avcapturephotosettings/init(rawpixelformattype:).md) initializer instead.

Requesting both formats adds requirements for other photo settings: see the [`format`](avcapturephotosettings/format.md) property for processed format requirements and the [`rawPhotoPixelFormatType`](avcapturephotosettings/rawphotopixelformattype.md) property for RAW format requirements. The capture output validates these requirements when you call the [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method. If your settings and delegate do not meet these requirements, that method raises an exception.

## Parameters

- `rawPixelFormatType`: The Bayer RAW pixel format type to use for capture. This value must be one of the format identifiers listed in the   array of your photo capture output.
- `rawFileType`: If you have no preferred file format, pass   and the photo output will automatically choose a default file format appropriate to the   parameter.
- `processedFormat`: To capture a photo in a compressed format, such as JPEG, set the key   in the   dictionary. The corresponding value must be one of the codec identifiers listed in the   array of your photo capture output. For a compressed format, you can also specify a compression level with the key  .
- `processedFileType`: If you have no preferred file format, pass   and the photo output will automatically choose a default file format appropriate to the   parameter.

## See Also

- [convenience init(format: [String : Any]?)](avcapturephotosettings/init(format:).md)
  Creates a photo settings object with the specified output format.
- [convenience init(rawPixelFormatType: OSType)](avcapturephotosettings/init(rawpixelformattype:).md)
  Creates a photo settings object for RAW-format-only capture with the specified pixel format.
- [convenience init(rawPixelFormatType: OSType, processedFormat: [String : Any]?)](avcapturephotosettings/init(rawpixelformattype:processedformat:).md)
  Creates a photo settings object for capture in both RAW format and a processed format.
- [convenience init(from: AVCapturePhotoSettings)](avcapturephotosettings/init(from:).md)
  Creates a unique photo settings object, copying all settings values from the specified photo settings object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/init(rawpixelformattype:rawfiletype:processedformat:processedfiletype:))*