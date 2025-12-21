# fileDataRepresentation()

**Framework**: AVFoundation  
**Kind**: method

Generates and returns a flat data representation of the photo and its attachments.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
func fileDataRepresentation() -> Data?
```

## Mentions

- [Saving captured photos](saving-captured-photos.md)
- [Capturing photos in RAW and Apple ProRAW formats](capturing-photos-in-raw-and-apple-proraw-formats.md)
- [Capturing photos with depth](capturing-photos-with-depth.md)
- [Capturing thumbnail and preview images](capturing-thumbnail-and-preview-images.md)
- [Capturing uncompressed image data](capturing-uncompressed-image-data.md)
- [Configuring camera capture to collect a Portrait Effects matte](configuring-camera-capture-to-collect-a-portrait-effects-matte.md)

#### Return Value

Data appropriate for writing to a file of the type specified when requesting photo capture, or `nil` if the photo and attachment data cannot be flattened.

#### Discussion

When you request a photo capture with the [`AVCapturePhotoOutput`](avcapturephotooutput.md) [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method, the [`AVCapturePhotoSettings`](avcapturephotosettings.md) object you provide specifies image data formats (such as JPEG and HEVC) and container file formats (such as JFIF and HEIF) for the resulting image file. Calling this method formats and packages the image pixel buffer, along with metadata and other attachments created during capture (such as preview photos and depth maps), into data appropriate for writing to a file of that type.

## See Also

- [func fileDataRepresentation(with: any AVCapturePhotoFileDataRepresentationCustomizer) -> Data?](avcapturephoto/filedatarepresentation(with:).md)
  Gets a customized representation of the photo data.
- [protocol AVCapturePhotoFileDataRepresentationCustomizer](avcapturephotofiledatarepresentationcustomizer.md)
  A protocol that defines the methods to implement to customize the packaging of photo data.
- [func cgImageRepresentation() -> CGImage?](avcapturephoto/cgimagerepresentation.md)
  Extracts and returns the captured photo’s primary image as a Core Graphics image object.
- [func previewCGImageRepresentation() -> CGImage?](avcapturephoto/previewcgimagerepresentation.md)
  Extracts and returns the captured photo’s preview image as a Core Graphics image object.
- [func fileDataRepresentation(withReplacementMetadata: [String : Any]?, replacementEmbeddedThumbnailPhotoFormat: [String : Any]?, replacementEmbeddedThumbnailPixelBuffer: CVPixelBuffer?, replacementDepthData: AVDepthData?) -> Data?](avcapturephoto/filedatarepresentation(withreplacementmetadata:replacementembeddedthumbnailphotoformat:replacementembeddedthumbnailpixelbuffer:replacementdepthdata:).md)
  Generates and returns a flat data representation of the photo using the specified replacements for some or all of its attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephoto/filedatarepresentation())*