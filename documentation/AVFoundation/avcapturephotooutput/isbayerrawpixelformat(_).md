# isBayerRAWPixelFormat(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns a Boolean value that indicates whether the pixel format is a Bayer RAW format.

**Availability**:
- iOS 14.3+
- iPadOS 14.3+
- Mac Catalyst 14.3+
- tvOS 17.0+

## Declaration

```swift
class func isBayerRAWPixelFormat(_ pixelFormat: OSType) -> Bool
```

```objc
+ (BOOL) isBayerRAWPixelFormat:(OSType) pixelFormat;
```

## Mentions

- [Capturing photos in RAW and Apple ProRAW formats](../capturing-photos-in-raw-and-apple-proraw-formats.md)

## Return Value

[`true`](../../Swift/true.md) if the pixel format is a Bayer RAW format, otherwise [`false`](../../Swift/false.md).

## Parameters

- `pixelFormat`: The pixel format to query.

## See Also

### Determining supported pixel formats
- [var availablePhotoPixelFormatTypes: [OSType]](./availablephotopixelformattypes-3ydgm.md)
  The pixel formats the capture output supports for photo capture.
- [var availableRawPhotoPixelFormatTypes: [OSType]](./availablerawphotopixelformattypes-9t9k5.md)
  The pixel formats the capture output supports for RAW photo capture.
- [func supportedPhotoPixelFormatTypes(for: AVFileType) -> [OSType]](./supportedphotopixelformattypes%28for%29.md)
  Returns the list of uncompressed pixel formats supported for photo data in the specified file type.
- [func supportedRawPhotoPixelFormatTypes(for: AVFileType) -> [OSType]](./supportedrawphotopixelformattypes%28for%29.md)
  Returns the list of Bayer RAW pixel formats supported for photo data in the specified file type.
- [class func isAppleProRAWPixelFormat(OSType) -> Bool](./isappleprorawpixelformat%28_%29.md)
  Returns a Boolean value that indicates whether the pixel format is an Apple ProRAW format.
- [availablePhotoPixelFormatTypes](./availablephotopixelformattypes-6eyb.md)
  The pixel formats the capture output supports for photo capture.
- [availableRawPhotoPixelFormatTypes](./availablerawphotopixelformattypes-5fatm.md)
  The pixel formats the capture output supports for RAW photo capture.
- [- supportedPhotoPixelFormatTypesForFileType:](./supportedphotopixelformattypesforfiletype_.md)
  Returns the list of uncompressed pixel formats supported for photo data in the specified file type.
- [- supportedRawPhotoPixelFormatTypesForFileType:](./supportedrawphotopixelformattypesforfiletype_.md)
  Returns the list of Bayer RAW pixel formats supported for photo data in the specified file type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isbayerrawpixelformat(_:))*