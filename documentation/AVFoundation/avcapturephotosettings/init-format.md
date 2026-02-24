# init(format:)

**Framework**: AVFoundation  
**Kind**: init

Creates a photo settings object with the specified output format.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
convenience init(format: [String : Any]?)
```

## Mentions

- [Capturing uncompressed image data](capturing-uncompressed-image-data.md)

#### Return Value

A new photo settings object.

#### Discussion

Requesting capture in a processed format adds requirements for other photo settings: for details, see the [`format`](avcapturephotosettings/format.md) property. The capture output validates these requirements when you call the [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method. If your settings and delegate don’t meet these requirements, that method raises an exception.

## Parameters

- `format`: A dictionary of Core Video pixel buffer attributes or AVFoundation video settings constants (see Video Settings). To capture a photo in an uncompressed format, such as 420f, 420v, or BGRA, set the key [`kCVPixelBufferPixelFormatTypeKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferPixelFormatTypeKey) in the `format` dictionary. The corresponding value must be one of the pixel format identifiers listed in the [`availablePhotoPixelFormatTypes`](avcapturephotooutput/availablephotopixelformattypes-6eyb.md) array of your photo capture output. To capture a photo in a compressed format, such as JPEG, set the key [`AVVideoCodecKey`](avvideocodeckey.md) in the `format` dictionary. The corresponding value must be one of the codec identifiers listed in the [`availablePhotoCodecTypes`](avcapturephotooutput/availablephotocodectypes.md) array of your photo capture output. For a compressed format, you can also specify a compression level with the key [`AVVideoQualityKey`](avvideoqualitykey.md).

## See Also

- [convenience init(rawPixelFormatType: OSType)](avcapturephotosettings/init(rawpixelformattype:).md)
  Creates a photo settings object for RAW-format-only capture with the specified pixel format.
- [convenience init(rawPixelFormatType: OSType, processedFormat: [String : Any]?)](avcapturephotosettings/init(rawpixelformattype:processedformat:).md)
  Creates a photo settings object for capture in both RAW format and a processed format.
- [convenience init(rawPixelFormatType: OSType, rawFileType: AVFileType?, processedFormat: [String : Any]?, processedFileType: AVFileType?)](avcapturephotosettings/init(rawpixelformattype:rawfiletype:processedformat:processedfiletype:).md)
  Creates a photo settings object for capture in both RAW format and a processed format with the specified output file types.
- [convenience init(from: AVCapturePhotoSettings)](avcapturephotosettings/init(from:).md)
  Creates a unique photo settings object, copying all settings values from the specified photo settings object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/init(format:))*