# init(from:)

**Framework**: AVFoundation  
**Kind**: init

Creates a unique photo settings object, copying all settings values from the specified photo settings object.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
convenience init(from photoSettings: AVCapturePhotoSettings)
```

#### Return Value

A new photo settings object.

#### Discussion

It is illegal to reuse a [`AVCapturePhotoSettings`](avcapturephotosettings.md) instance for multiple captures. Calling the [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method throws an exception if the [`uniqueID`](avcapturephotosettings/uniqueid.md) value of the `settings` parameter matches that of any previously used settings object.

To reuse a specific combination of settings, use this initializer to create a new [`AVCapturePhotoSettings`](avcapturephotosettings.md) instance from an existing photo settings object. The newly created instance has a new, unique value for its [`uniqueID`](avcapturephotosettings/uniqueid.md) property, but copies the values for all other properties from the `photoSettings` parameter.

## Parameters

- `photoSettings`: The photo settings object from which to copy settings.

## See Also

- [convenience init(format: [String : Any]?)](avcapturephotosettings/init(format:).md)
  Creates a photo settings object with the specified output format.
- [convenience init(rawPixelFormatType: OSType)](avcapturephotosettings/init(rawpixelformattype:).md)
  Creates a photo settings object for RAW-format-only capture with the specified pixel format.
- [convenience init(rawPixelFormatType: OSType, processedFormat: [String : Any]?)](avcapturephotosettings/init(rawpixelformattype:processedformat:).md)
  Creates a photo settings object for capture in both RAW format and a processed format.
- [convenience init(rawPixelFormatType: OSType, rawFileType: AVFileType?, processedFormat: [String : Any]?, processedFileType: AVFileType?)](avcapturephotosettings/init(rawpixelformattype:rawfiletype:processedformat:processedfiletype:).md)
  Creates a photo settings object for capture in both RAW format and a processed format with the specified output file types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/init(from:))*