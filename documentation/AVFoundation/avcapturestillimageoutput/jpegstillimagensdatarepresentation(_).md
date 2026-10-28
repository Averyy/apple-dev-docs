# jpegStillImageNSDataRepresentation(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Returns an `NSData` representation of a still image data and metadata attachments in a JPEG sample buffer.

**Availability**:
- iOS 4.0+ - Deprecated in 10.0
- iPadOS 4.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.7+ - Deprecated in 10.15

> **Deprecated**: Use AVCapturePhotoOutput instead.

## Declaration

```swift
class func jpegStillImageNSDataRepresentation(_ jpegSampleBuffer: CMSampleBuffer) -> Data?
```

```objc
+ (NSData *) jpegStillImageNSDataRepresentation:(CMSampleBufferRef) jpegSampleBuffer;
```

## Return Value

An `NSData` representation of `jpegSampleBuffer`.

## Discussion

This method merges the image data and `Exif` metadata sample buffer attachments without recompressing the image.

The returned `NSData` object is suitable for writing to disk.

## Parameters

- `jpegSampleBuffer`: The sample buffer carrying JPEG image data, optionally with `Exif` metadata sample buffer attachments.

  This method throws an [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md) if `jpegSampleBuffer` is `NULL` or not in the JPEG format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/jpegstillimagensdatarepresentation(_:))*