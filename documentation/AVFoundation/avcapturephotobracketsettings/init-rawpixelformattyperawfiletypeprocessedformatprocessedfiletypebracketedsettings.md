# init(rawPixelFormatType:rawFileType:processedFormat:processedFileType:bracketedSettings:)

**Framework**: AVFoundation  
**Kind**: init

Creates a photo settings object for capture in both RAW format and a processed format.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
convenience init(rawPixelFormatType: OSType, rawFileType: AVFileType?, processedFormat: [String : Any]?, processedFileType: AVFileType?, bracketedSettings: [AVCaptureBracketedStillImageSettings])
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
- `bracketedSettings`: The number of image settings objects in this array must be greater than zero and less than or equal to the   value of your photo output. All image settings objects in this array must be the same type. Calling this initializer with an invalid number or combination of image settings objects raises an exception ( ).

## See Also

- [convenience init(rawPixelFormatType: OSType, processedFormat: [String : Any]?, bracketedSettings: [AVCaptureBracketedStillImageSettings])](avcapturephotobracketsettings/init(rawpixelformattype:processedformat:bracketedsettings:).md)
  Creates a photo settings object for the specified bracket of captures, in the specified formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotobracketsettings/init(rawpixelformattype:rawfiletype:processedformat:processedfiletype:bracketedsettings:))*