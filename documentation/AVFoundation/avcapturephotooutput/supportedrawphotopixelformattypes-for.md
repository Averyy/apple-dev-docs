# supportedRawPhotoPixelFormatTypes(for:)

**Framework**: AVFoundation  
**Kind**: method

Returns the list of Bayer RAW pixel formats supported for photo data in the specified file type.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
@nonobjc
func supportedRawPhotoPixelFormatTypes(for fileType: AVFileType) -> [OSType]
```

#### Return Value

An array of pixel format types supported for encoding in the specified file type.

#### Discussion

When you issue a photo capture request, you can separately specify the format for capturing or encoding image data and the container format for producing output files containing that data. However, each file type supports only a specific set of image data types.

After choosing a file type from the [`availableRawPhotoFileTypes`](avcapturephotooutput/availablerawphotofiletypes.md) array, use this method to find a compatible image data format before creating a photo settings object.

## Parameters

- `fileType`: The file type for which to obtain format information.

## See Also

- [var availablePhotoPixelFormatTypes: [OSType]](avcapturephotooutput/availablephotopixelformattypes-3ydgm.md)
  The pixel formats the capture output supports for photo capture.
- [var availableRawPhotoPixelFormatTypes: [OSType]](avcapturephotooutput/availablerawphotopixelformattypes-9t9k5.md)
  The pixel formats the capture output supports for RAW photo capture.
- [func supportedPhotoPixelFormatTypes(for: AVFileType) -> [OSType]](avcapturephotooutput/supportedphotopixelformattypes(for:).md)
  Returns the list of uncompressed pixel formats supported for photo data in the specified file type.
- [class func isAppleProRAWPixelFormat(OSType) -> Bool](avcapturephotooutput/isappleprorawpixelformat(_:).md)
  Returns a Boolean value that indicates whether the pixel format is an Apple ProRAW format.
- [class func isBayerRAWPixelFormat(OSType) -> Bool](avcapturephotooutput/isbayerrawpixelformat(_:).md)
  Returns a Boolean value that indicates whether the pixel format is a Bayer RAW format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/supportedrawphotopixelformattypes(for:))*