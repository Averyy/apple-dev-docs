# isAppleProRAWPixelFormat(_:)

**Framework**: AVFoundation  
**Kind**: method

Returns a Boolean value that indicates whether the pixel format is an Apple ProRAW format.

**Availability**:
- iOS 14.3+
- iPadOS 14.3+
- Mac Catalyst 14.3+
- tvOS 17.0+

## Declaration

```swift
class func isAppleProRAWPixelFormat(_ pixelFormat: OSType) -> Bool
```

## Mentions

- [Capturing photos in RAW and Apple ProRAW formats](capturing-photos-in-raw-and-apple-proraw-formats.md)

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the pixel format is an Apple ProRAW format, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `pixelFormat`: The pixel format to query.

## See Also

- [var availablePhotoPixelFormatTypes: [OSType]](avcapturephotooutput/availablephotopixelformattypes-3ydgm.md)
  The pixel formats the capture output supports for photo capture.
- [var availableRawPhotoPixelFormatTypes: [OSType]](avcapturephotooutput/availablerawphotopixelformattypes-9t9k5.md)
  The pixel formats the capture output supports for RAW photo capture.
- [func supportedPhotoPixelFormatTypes(for: AVFileType) -> [OSType]](avcapturephotooutput/supportedphotopixelformattypes(for:).md)
  Returns the list of uncompressed pixel formats supported for photo data in the specified file type.
- [func supportedRawPhotoPixelFormatTypes(for: AVFileType) -> [OSType]](avcapturephotooutput/supportedrawphotopixelformattypes(for:).md)
  Returns the list of Bayer RAW pixel formats supported for photo data in the specified file type.
- [class func isBayerRAWPixelFormat(OSType) -> Bool](avcapturephotooutput/isbayerrawpixelformat(_:).md)
  Returns a Boolean value that indicates whether the pixel format is a Bayer RAW format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isappleprorawpixelformat(_:))*