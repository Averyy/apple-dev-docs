# replacementEmbeddedThumbnailPixelBuffer(withPhotoFormat:for:)

**Framework**: AVFoundation  
**Kind**: method

A callback in which you can provide a replacement embedded thumbnail image with compression settings, or strip the existing embedded thumbnail image from the flattened file.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
optional func replacementEmbeddedThumbnailPixelBuffer(withPhotoFormat replacementEmbeddedThumbnailPhotoFormatOut: AutoreleasingUnsafeMutablePointer<NSDictionary?>, for photo: AVCapturePhoto) -> Unmanaged<CVPixelBuffer>?
```

#### Return Value

A pixel buffer containing a source image to be encoded to the file as the replacement thumbnail image. To preserve the existing embedded thumbnail photo to the flattened data, set `replacementEmbeddedThumbnailPhotoFormatOut` to `photo.embeddedThumbnailPhotoFormat` and return `nil`. To replace the existing embedded thumbnail, pass a replacement photo format dictionary and return a non-`nil` replacement pixel buffer.  To remove the existing embedded thumbnail, set `replacementEmbeddedThumbnailPhotoFormatOut` to `nil` and return `nil`.

#### Discussion

This callback is optional. If your delegate doesn’t implement this callback, the existing metadata in the in-memory [`AVCapturePhoto`](avcapturephoto.md) container is written directly to the file data representation.

## Parameters

- `replacementEmbeddedThumbnailPhotoFormatOut`: A pointer to a dictionary of keys and values from  .  If you pass a non-nil dictionary,   is required, with   and   keys optional.
- `photo`: The calling instance of   whose file metadata you’re modifying.

## See Also

- [func replacementMetadata(for: AVCapturePhoto) -> [String : Any]?](avcapturephotofiledatarepresentationcustomizer/replacementmetadata(for:).md)
  A callback in which you can provide replacement metadata or direct [`AVCapturePhoto`](avcapturephoto.md) to strip existing metadata from the flattened file.
- [func replacementDepthData(for: AVCapturePhoto) -> AVDepthData?](avcapturephotofiledatarepresentationcustomizer/replacementdepthdata(for:).md)
  A callback in which you can provide replacement depth data or strip existing depth data from the file.
- [func replacementPortraitEffectsMatte(for: AVCapturePhoto) -> AVPortraitEffectsMatte?](avcapturephotofiledatarepresentationcustomizer/replacementportraiteffectsmatte(for:).md)
  A callback in which you can provide a replacement portrait effects matte, or strip the existing portrait effects matte from the file.
- [func replacementSemanticSegmentationMatte(ofType: AVSemanticSegmentationMatte.MatteType, for: AVCapturePhoto) -> AVSemanticSegmentationMatte?](avcapturephotofiledatarepresentationcustomizer/replacementsemanticsegmentationmatte(oftype:for:).md)
  Replaces or removes the semantic segmentation matte of the specified type from the flattened file data representation.
- [func replacementAppleProRAWCompressionSettings(for: AVCapturePhoto, defaultSettings: [String : Any], maximumBitDepth: Int) -> [String : Any]](avcapturephotofiledatarepresentationcustomizer/replacementappleprorawcompressionsettings(for:defaultsettings:maximumbitdepth:).md)
  Replaces the compression settings the system uses when writing Apple ProRAW data to a Linear DNG file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotofiledatarepresentationcustomizer/replacementembeddedthumbnailpixelbuffer(withphotoformat:for:))*