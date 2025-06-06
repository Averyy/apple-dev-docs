# format

**Framework**: AVFoundation  
**Kind**: property

A dictionary describing the processed format (for example, JPEG) to deliver captured photos in.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
var format: [String : Any]? { get }
```

#### Discussion

This property is read-only—you specify a processed format when creating a settings object with the [`photoSettings`](avcapturephotosettings/photosettings.md), [`init(format:)`](avcapturephotosettings/init(format:).md), or [`init(rawPixelFormatType:processedFormat:)`](avcapturephotosettings/init(rawpixelformattype:processedformat:).md) initializer.

When capturing images in processed formats, the following requirements apply:

- This dictionary must contain a value for either the [`kCVPixelBufferPixelFormatTypeKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferPixelFormatTypeKey) (to request an uncompressed format) or [`AVVideoCodecKey`](avvideocodeckey.md) (to request a compressed format such as JPEG) key, but not both.
- If this dictionary has the [`kCVPixelBufferPixelFormatTypeKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferPixelFormatTypeKey) key, the value for that key must be listed in the photo output’s [`availablePhotoPixelFormatTypes`](avcapturephotooutput/availablephotopixelformattypes-6eyb.md) array.

If this dictionary has the [`AVVideoCodecKey`](avvideocodeckey.md) key, the value for that key must be listed in the photo output’s [`availablePhotoCodecTypes`](avcapturephotooutput/availablephotocodectypes.md) array.

- Your delegate method must implement the [`photoOutput(_:didFinishProcessingPhoto:previewPhoto:resolvedSettings:bracketSettings:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingphoto:previewphoto:resolvedsettings:bracketsettings:error:).md) method.

The capture output validates these requirements when you call the [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method. If your settings and delegate do not meet these requirements, that method raises an exception.

## See Also

- [var uniqueID: Int64](avcapturephotosettings/uniqueid.md)
  A unique identifier for this photo settings instance.
- [var processedFileType: AVFileType?](avcapturephotosettings/processedfiletype.md)
  The container file format for eventual output of the processed image.
- [var rawFileType: AVFileType?](avcapturephotosettings/rawfiletype.md)
  The container file format for eventual output of the RAW image.
- [var rawPhotoPixelFormatType: OSType](avcapturephotosettings/rawphotopixelformattype.md)
  An identifier for the Bayer RAW pixel format to deliver captured RAW photos in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/format)*