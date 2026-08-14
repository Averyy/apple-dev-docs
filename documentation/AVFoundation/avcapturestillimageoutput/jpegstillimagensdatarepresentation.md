# jpegStillImageNSDataRepresentation(_:)

**Framework**: AVFoundation  
**Kind**: method

Returns an `NSData` representation of a still image data and metadata attachments in a JPEG sample buffer.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+

## Declaration

```swift
class func jpegStillImageNSDataRepresentation(_ jpegSampleBuffer: CMSampleBuffer) -> Data?
```

#### Return Value

An `NSData` representation of `jpegSampleBuffer`.

#### Discussion

This method merges the image data and `Exif` metadata sample buffer attachments without recompressing the image.

The returned `NSData` object is suitable for writing to disk.

## Parameters

- `jpegSampleBuffer`: The sample buffer carrying JPEG image data, optionally with `Exif` metadata sample buffer attachments. This method throws an [`invalidArgumentException`](https://developer.apple.com/documentation/foundation/nsexceptionname/invalidargumentexception) if `jpegSampleBuffer` is `NULL` or not in the JPEG format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/jpegstillimagensdatarepresentation(_:))*