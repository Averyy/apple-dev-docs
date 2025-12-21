# fileDataRepresentation(with:)

**Framework**: AVFoundation  
**Kind**: method

Gets a customized representation of the photo data.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
func fileDataRepresentation(with customizer: any AVCapturePhotoFileDataRepresentationCustomizer) -> Data?
```

## Mentions

- [Capturing photos in RAW and Apple ProRAW formats](capturing-photos-in-raw-and-apple-proraw-formats.md)
- [Configuring camera capture to collect a Portrait Effects matte](configuring-camera-capture-to-collect-a-portrait-effects-matte.md)

#### Return Value

A data representation of the photo.

## Parameters

- `customizer`: An object that customizes the returned metadata, image thumbnail, or depth data.

## See Also

- [protocol AVCapturePhotoFileDataRepresentationCustomizer](avcapturephotofiledatarepresentationcustomizer.md)
  A protocol that defines the methods to implement to customize the packaging of photo data.
- [func fileDataRepresentation() -> Data?](avcapturephoto/filedatarepresentation.md)
  Generates and returns a flat data representation of the photo and its attachments.
- [func cgImageRepresentation() -> CGImage?](avcapturephoto/cgimagerepresentation.md)
  Extracts and returns the captured photo’s primary image as a Core Graphics image object.
- [func previewCGImageRepresentation() -> CGImage?](avcapturephoto/previewcgimagerepresentation.md)
  Extracts and returns the captured photo’s preview image as a Core Graphics image object.
- [func fileDataRepresentation(withReplacementMetadata: [String : Any]?, replacementEmbeddedThumbnailPhotoFormat: [String : Any]?, replacementEmbeddedThumbnailPixelBuffer: CVPixelBuffer?, replacementDepthData: AVDepthData?) -> Data?](avcapturephoto/filedatarepresentation(withreplacementmetadata:replacementembeddedthumbnailphotoformat:replacementembeddedthumbnailpixelbuffer:replacementdepthdata:).md)
  Generates and returns a flat data representation of the photo using the specified replacements for some or all of its attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephoto/filedatarepresentation(with:))*