# availablePhotoPixelFormatTypes

**Framework**: AVFoundation  
**Kind**: property

The pixel formats the capture output supports for photo capture.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 17.0+

## Declaration

```swift
@nonobjc
var availablePhotoPixelFormatTypes: [OSType] { get }
```

#### Discussion

To capture a photo in an uncompressed format, such as 420f, 420v, or BGRA, use the [`init(format:)`](avcapturephotosettings/init(format:).md) initializer to create your photo settings object. In that initializer’s `format` dictionary, pass the key [`kCVPixelBufferPixelFormatTypeKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferPixelFormatTypeKey), whose value must be one of the pixel format identifiers listed in this array.

> **Note**:  Read this property only after adding the photo capture output to an [`AVCaptureSession`](avcapturesession.md) object containing a video source. If the photo capture output isn’t connected to a session with a video source, this array is empty.

This property supports key-value observing.

## See Also

- [var availableRawPhotoPixelFormatTypes: [OSType]](avcapturephotooutput/availablerawphotopixelformattypes-9t9k5.md)
  The pixel formats the capture output supports for RAW photo capture.
- [func supportedPhotoPixelFormatTypes(for: AVFileType) -> [OSType]](avcapturephotooutput/supportedphotopixelformattypes(for:).md)
  Returns the list of uncompressed pixel formats supported for photo data in the specified file type.
- [func supportedRawPhotoPixelFormatTypes(for: AVFileType) -> [OSType]](avcapturephotooutput/supportedrawphotopixelformattypes(for:).md)
  Returns the list of Bayer RAW pixel formats supported for photo data in the specified file type.
- [class func isAppleProRAWPixelFormat(OSType) -> Bool](avcapturephotooutput/isappleprorawpixelformat(_:).md)
  Returns a Boolean value that indicates whether the pixel format is an Apple ProRAW format.
- [class func isBayerRAWPixelFormat(OSType) -> Bool](avcapturephotooutput/isbayerrawpixelformat(_:).md)
  Returns a Boolean value that indicates whether the pixel format is a Bayer RAW format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/availablephotopixelformattypes-3ydgm)*