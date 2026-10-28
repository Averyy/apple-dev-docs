# availablePhotoPixelFormatTypes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The pixel formats the capture output supports for photo capture.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * availablePhotoPixelFormatTypes;
```

## Mentions

- [Capturing uncompressed image data](../capturing-uncompressed-image-data.md)

## Discussion

To capture a photo in an uncompressed format, such as 420f, 420v, or BGRA, use the [`init(format:)`](../avcapturephotosettings/init%28format%29.md) initializer to create your photo settings object. In that initializer’s `format` dictionary, pass the key [`kCVPixelBufferPixelFormatTypeKey`](../../CoreVideo/kcvpixelbufferpixelformattypekey.md), whose value must be one of the pixel format identifiers listed in this array.

> **Note**:  Read this property only after adding the photo capture output to an [`AVCaptureSession`](../avcapturesession.md) object containing a video source. If the photo capture output isn’t connected to a session with a video source, this array is empty.

This property supports key-value observing.

## See Also

### Determining supported pixel formats
- [availableRawPhotoPixelFormatTypes](./availablerawphotopixelformattypes-5fatm.md)
  The pixel formats the capture output supports for RAW photo capture.
- [- supportedPhotoPixelFormatTypesForFileType:](./supportedphotopixelformattypesforfiletype_.md)
  Returns the list of uncompressed pixel formats supported for photo data in the specified file type.
- [- supportedRawPhotoPixelFormatTypesForFileType:](./supportedrawphotopixelformattypesforfiletype_.md)
  Returns the list of Bayer RAW pixel formats supported for photo data in the specified file type.
- [class func isAppleProRAWPixelFormat(OSType) -> Bool](./isappleprorawpixelformat%28_%29.md)
  Returns a Boolean value that indicates whether the pixel format is an Apple ProRAW format.
- [class func isBayerRAWPixelFormat(OSType) -> Bool](./isbayerrawpixelformat%28_%29.md)
  Returns a Boolean value that indicates whether the pixel format is a Bayer RAW format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/availablephotopixelformattypes-6eyb)*