# replacementSemanticSegmentationMatte(ofType:for:)

**Framework**: AVFoundation  
**Kind**: method

Replaces or removes the semantic segmentation matte of the specified type from the flattened file data representation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
optional func replacementSemanticSegmentationMatte(ofType semanticSegmentationMatteType: AVSemanticSegmentationMatte.MatteType, for photo: AVCapturePhoto) -> AVSemanticSegmentationMatte?
```

#### Return Value

An instance of [`AVSemanticSegmentationMatte`](avsemanticsegmentationmatte.md). To preserve the existing matte, return `photo.```AVCapturePhoto/semanticSegmentationMatte(for:)``. To strip the existing one, return `nil`. To replace, provide a replacement [`AVSemanticSegmentationMatte`](avsemanticsegmentationmatte.md) instance.

#### Discussion

This callback is optional. If your delegate doesn’t implement this callback, the existing semantic segmentation matte of the specified type in the in-memory [`AVCapturePhoto`](avcapturephoto.md) container is written to the file data representation.

## Parameters

- `semanticSegmentationMatteType`: The type of semantic segmentation matte to be replaced or stripped.
- `photo`: The calling instance of  .

## See Also

- [func replacementMetadata(for: AVCapturePhoto) -> [String : Any]?](avcapturephotofiledatarepresentationcustomizer/replacementmetadata(for:).md)
  A callback in which you can provide replacement metadata or direct [`AVCapturePhoto`](avcapturephoto.md) to strip existing metadata from the flattened file.
- [func replacementEmbeddedThumbnailPixelBuffer(withPhotoFormat: AutoreleasingUnsafeMutablePointer<NSDictionary?>, for: AVCapturePhoto) -> Unmanaged<CVPixelBuffer>?](avcapturephotofiledatarepresentationcustomizer/replacementembeddedthumbnailpixelbuffer(withphotoformat:for:).md)
  A callback in which you can provide a replacement embedded thumbnail image with compression settings, or strip the existing embedded thumbnail image from the flattened file.
- [func replacementDepthData(for: AVCapturePhoto) -> AVDepthData?](avcapturephotofiledatarepresentationcustomizer/replacementdepthdata(for:).md)
  A callback in which you can provide replacement depth data or strip existing depth data from the file.
- [func replacementPortraitEffectsMatte(for: AVCapturePhoto) -> AVPortraitEffectsMatte?](avcapturephotofiledatarepresentationcustomizer/replacementportraiteffectsmatte(for:).md)
  A callback in which you can provide a replacement portrait effects matte, or strip the existing portrait effects matte from the file.
- [func replacementAppleProRAWCompressionSettings(for: AVCapturePhoto, defaultSettings: [String : Any], maximumBitDepth: Int) -> [String : Any]](avcapturephotofiledatarepresentationcustomizer/replacementappleprorawcompressionsettings(for:defaultsettings:maximumbitdepth:).md)
  Replaces the compression settings the system uses when writing Apple ProRAW data to a Linear DNG file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotofiledatarepresentationcustomizer/replacementsemanticsegmentationmatte(oftype:for:))*