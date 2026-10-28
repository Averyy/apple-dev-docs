# previewCGImageRepresentation()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Extracts and returns the captured photo’s preview image as a Core Graphics image object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
func previewCGImageRepresentation() -> CGImage?
```

```objc
- (CGImageRef) previewCGImageRepresentation;
```

## Return Value

A Core Graphics image representation of the captured photo, or `nil` if either the image cannot be converted or a preview image was not requested as part of the photo capture.

## See Also

### Packaging data for file output
- [func fileDataRepresentation(with: any AVCapturePhotoFileDataRepresentationCustomizer) -> Data?](./filedatarepresentation%28with%29.md)
  Gets a customized representation of the photo data.
- [protocol AVCapturePhotoFileDataRepresentationCustomizer](../avcapturephotofiledatarepresentationcustomizer.md)
  A protocol that defines the methods to implement to customize the packaging of photo data.
- [func fileDataRepresentation() -> Data?](./filedatarepresentation%28%29.md)
  Generates and returns a flat data representation of the photo and its attachments.
- [func cgImageRepresentation() -> CGImage?](./cgimagerepresentation%28%29.md)
  Extracts and returns the captured photo’s primary image as a Core Graphics image object.
- [func fileDataRepresentation(withReplacementMetadata: [String : Any]?, replacementEmbeddedThumbnailPhotoFormat: [String : Any]?, replacementEmbeddedThumbnailPixelBuffer: CVPixelBuffer?, replacementDepthData: AVDepthData?) -> Data?](./filedatarepresentation%28withreplacementmetadata,replacementembeddedthumbnailphotoformat,replacementembeddedthumbnailpixelbuffer,replacementdepthdata%29.md)
  Generates and returns a flat data representation of the photo using the specified replacements for some or all of its attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephoto/previewcgimagerepresentation())*