# uniqueID

**Framework**: AVFoundation  
**Kind**: property

A unique identifier for this photo settings instance.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
var uniqueID: Int64 { get }
```

## Mentions

- [Tracking photo capture progress](tracking-photo-capture-progress.md)

#### Discussion

Creating a [`AVCapturePhotoSettings`](avcapturephotosettings.md) instance automatically assigns a unique value to this property.

Use this property to track a photo capture request. After you call the [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method, the photo capture output calls your delegate object to provide information about the progress and results of the capture. Each delegate method includes a [`AVCaptureResolvedPhotoSettings`](avcaptureresolvedphotosettings.md) whose [`uniqueID`](avcapturephotosettings/uniqueid.md) property matches the [`uniqueID`](avcapturephotosettings/uniqueid.md) value of the [`AVCapturePhotoSettings`](avcapturephotosettings.md) object you used to request capture.

It is illegal to reuse a [`AVCapturePhotoSettings`](avcapturephotosettings.md) instance for multiple captures. Calling the [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method throws an exception ([`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException)) if the `settings` object’s [`uniqueID`](avcapturephotosettings/uniqueid.md) value matches that of any previously used settings object.

## See Also

- [var format: [String : Any]?](avcapturephotosettings/format.md)
  A dictionary describing the processed format (for example, JPEG) to deliver captured photos in.
- [var processedFileType: AVFileType?](avcapturephotosettings/processedfiletype.md)
  The container file format for eventual output of the processed image.
- [var rawFileType: AVFileType?](avcapturephotosettings/rawfiletype.md)
  The container file format for eventual output of the RAW image.
- [var rawPhotoPixelFormatType: OSType](avcapturephotosettings/rawphotopixelformattype.md)
  An identifier for the Bayer RAW pixel format to deliver captured RAW photos in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/uniqueid)*