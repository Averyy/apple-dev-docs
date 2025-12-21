# AVCapturePhotoFileDataRepresentationCustomizer

**Framework**: AVFoundation  
**Kind**: protocol

A protocol that defines the methods to implement to customize the packaging of photo data.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
protocol AVCapturePhotoFileDataRepresentationCustomizer : NSObjectProtocol
```

## Mentions

- [Capturing photos in RAW and Apple ProRAW formats](capturing-photos-in-raw-and-apple-proraw-formats.md)

#### Overview

AVCapturePhoto is a wrapper representing a photo in a file container. To flatten the photo to an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object to write to file, call [`fileDataRepresentation()`](avcapturephoto/filedatarepresentation().md). For more complex flattening operations such as replacing or stripping metadata, call [`fileDataRepresentation(with:)`](avcapturephoto/filedatarepresentation(with:).md) and provide a delegate for customized replacement or stripping behavior. This delegate’s methods are called synchronously before the flattening process begins.

## Topics

### Replacing or removing metadata
- [func replacementMetadata(for: AVCapturePhoto) -> [String : Any]?](avcapturephotofiledatarepresentationcustomizer/replacementmetadata(for:).md)
  A callback in which you can provide replacement metadata or direct [`AVCapturePhoto`](avcapturephoto.md) to strip existing metadata from the flattened file.
- [func replacementEmbeddedThumbnailPixelBuffer(withPhotoFormat: AutoreleasingUnsafeMutablePointer<NSDictionary?>, for: AVCapturePhoto) -> Unmanaged<CVPixelBuffer>?](avcapturephotofiledatarepresentationcustomizer/replacementembeddedthumbnailpixelbuffer(withphotoformat:for:).md)
  A callback in which you can provide a replacement embedded thumbnail image with compression settings, or strip the existing embedded thumbnail image from the flattened file.
- [func replacementDepthData(for: AVCapturePhoto) -> AVDepthData?](avcapturephotofiledatarepresentationcustomizer/replacementdepthdata(for:).md)
  A callback in which you can provide replacement depth data or strip existing depth data from the file.
- [func replacementPortraitEffectsMatte(for: AVCapturePhoto) -> AVPortraitEffectsMatte?](avcapturephotofiledatarepresentationcustomizer/replacementportraiteffectsmatte(for:).md)
  A callback in which you can provide a replacement portrait effects matte, or strip the existing portrait effects matte from the file.
- [func replacementSemanticSegmentationMatte(ofType: AVSemanticSegmentationMatte.MatteType, for: AVCapturePhoto) -> AVSemanticSegmentationMatte?](avcapturephotofiledatarepresentationcustomizer/replacementsemanticsegmentationmatte(oftype:for:).md)
  Replaces or removes the semantic segmentation matte of the specified type from the flattened file data representation.
- [func replacementAppleProRAWCompressionSettings(for: AVCapturePhoto, defaultSettings: [String : Any], maximumBitDepth: Int) -> [String : Any]](avcapturephotofiledatarepresentationcustomizer/replacementappleprorawcompressionsettings(for:defaultsettings:maximumbitdepth:).md)
  Replaces the compression settings the system uses when writing Apple ProRAW data to a Linear DNG file.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func fileDataRepresentation(with: any AVCapturePhotoFileDataRepresentationCustomizer) -> Data?](avcapturephoto/filedatarepresentation(with:).md)
  Gets a customized representation of the photo data.
- [func fileDataRepresentation() -> Data?](avcapturephoto/filedatarepresentation.md)
  Generates and returns a flat data representation of the photo and its attachments.
- [func cgImageRepresentation() -> CGImage?](avcapturephoto/cgimagerepresentation.md)
  Extracts and returns the captured photo’s primary image as a Core Graphics image object.
- [func previewCGImageRepresentation() -> CGImage?](avcapturephoto/previewcgimagerepresentation.md)
  Extracts and returns the captured photo’s preview image as a Core Graphics image object.
- [func fileDataRepresentation(withReplacementMetadata: [String : Any]?, replacementEmbeddedThumbnailPhotoFormat: [String : Any]?, replacementEmbeddedThumbnailPixelBuffer: CVPixelBuffer?, replacementDepthData: AVDepthData?) -> Data?](avcapturephoto/filedatarepresentation(withreplacementmetadata:replacementembeddedthumbnailphotoformat:replacementembeddedthumbnailpixelbuffer:replacementdepthdata:).md)
  Generates and returns a flat data representation of the photo using the specified replacements for some or all of its attachments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotofiledatarepresentationcustomizer)*