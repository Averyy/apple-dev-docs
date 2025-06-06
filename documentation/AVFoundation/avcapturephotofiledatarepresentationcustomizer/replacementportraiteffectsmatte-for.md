# replacementPortraitEffectsMatte(for:)

**Framework**: AVFoundation  
**Kind**: method

A callback in which you can provide a replacement portrait effects matte, or strip the existing portrait effects matte from the file.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
optional func replacementPortraitEffectsMatte(for photo: AVCapturePhoto) -> AVPortraitEffectsMatte?
```

#### Return Value

An instance of [`AVPortraitEffectsMatte`](avportraiteffectsmatte.md).  To preserve the existing portrait effects matte, return `photo.portraitEffectsMatte`. To strip the existing portrait effects matte, return `nil`.  To replace the portrait effects matte, provide a replacement [`AVPortraitEffectsMatte`](avportraiteffectsmatte.md) instance.

#### Discussion

This callback is optional. If your delegate doesn’t implement this callback, the existing metadata in the in-memory [`AVCapturePhoto`](avcapturephoto.md) container is written directly to the file data representation.

## Parameters

- `photo`: The calling instance of   whose file metadata you’re modifying.

## See Also

- [func replacementMetadata(for: AVCapturePhoto) -> [String : Any]?](avcapturephotofiledatarepresentationcustomizer/replacementmetadata(for:).md)
  A callback in which you can provide replacement metadata or direct [`AVCapturePhoto`](avcapturephoto.md) to strip existing metadata from the flattened file.
- [func replacementEmbeddedThumbnailPixelBuffer(withPhotoFormat: AutoreleasingUnsafeMutablePointer<NSDictionary?>, for: AVCapturePhoto) -> Unmanaged<CVPixelBuffer>?](avcapturephotofiledatarepresentationcustomizer/replacementembeddedthumbnailpixelbuffer(withphotoformat:for:).md)
  A callback in which you can provide a replacement embedded thumbnail image with compression settings, or strip the existing embedded thumbnail image from the flattened file.
- [func replacementDepthData(for: AVCapturePhoto) -> AVDepthData?](avcapturephotofiledatarepresentationcustomizer/replacementdepthdata(for:).md)
  A callback in which you can provide replacement depth data or strip existing depth data from the file.
- [func replacementSemanticSegmentationMatte(ofType: AVSemanticSegmentationMatte.MatteType, for: AVCapturePhoto) -> AVSemanticSegmentationMatte?](avcapturephotofiledatarepresentationcustomizer/replacementsemanticsegmentationmatte(oftype:for:).md)
  Replaces or removes the semantic segmentation matte of the specified type from the flattened file data representation.
- [func replacementAppleProRAWCompressionSettings(for: AVCapturePhoto, defaultSettings: [String : Any], maximumBitDepth: Int) -> [String : Any]](avcapturephotofiledatarepresentationcustomizer/replacementappleprorawcompressionsettings(for:defaultsettings:maximumbitdepth:).md)
  Replaces the compression settings the system uses when writing Apple ProRAW data to a Linear DNG file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotofiledatarepresentationcustomizer/replacementportraiteffectsmatte(for:))*