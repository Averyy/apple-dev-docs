# replacementDepthData(for:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

A callback in which you can provide replacement depth data or strip existing depth data from the file.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
optional func replacementDepthData(for photo: AVCapturePhoto) -> AVDepthData?
```

```objc
- (AVDepthData *) replacementDepthDataForPhoto:(AVCapturePhoto *) photo;
```

## Return Value

An instance of [`AVDepthData`](../avdepthdata.md).  To preserve the existing depth data, return `photo.depthData`. To strip existing depth data, provide a replacement [`AVDepthData`](../avdepthdata.md) instance.

## Discussion

This callback is optional. If your delegate doesn’t implement this callback, the existing metadata in the in-memory [`AVCapturePhoto`](../avcapturephoto.md) container is written directly to the file data representation.

## Parameters

- `photo`: The calling instance of [`AVCapturePhoto`](../avcapturephoto.md) whose file metadata you’re modifying.

## See Also

### Replacing or removing metadata
- [func replacementMetadata(for: AVCapturePhoto) -> [String : Any]?](./replacementmetadata%28for%29.md)
  A callback in which you can provide replacement metadata or direct [`AVCapturePhoto`](../avcapturephoto.md) to strip existing metadata from the flattened file.
- [func replacementEmbeddedThumbnailPixelBuffer(withPhotoFormat: AutoreleasingUnsafeMutablePointer<NSDictionary?>, for: AVCapturePhoto) -> Unmanaged<CVPixelBuffer>?](./replacementembeddedthumbnailpixelbuffer%28withphotoformat,for%29.md)
  A callback in which you can provide a replacement embedded thumbnail image with compression settings, or strip the existing embedded thumbnail image from the flattened file.
- [func replacementPortraitEffectsMatte(for: AVCapturePhoto) -> AVPortraitEffectsMatte?](./replacementportraiteffectsmatte%28for%29.md)
  A callback in which you can provide a replacement portrait effects matte, or strip the existing portrait effects matte from the file.
- [func replacementSemanticSegmentationMatte(ofType: AVSemanticSegmentationMatte.MatteType, for: AVCapturePhoto) -> AVSemanticSegmentationMatte?](./replacementsemanticsegmentationmatte%28oftype,for%29.md)
  Replaces or removes the semantic segmentation matte of the specified type from the flattened file data representation.
- [func replacementAppleProRAWCompressionSettings(for: AVCapturePhoto, defaultSettings: [String : Any], maximumBitDepth: Int) -> [String : Any]](./replacementappleprorawcompressionsettings%28for,defaultsettings,maximumbitdepth%29.md)
  Replaces the compression settings the system uses when writing Apple ProRAW data to a Linear DNG file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotofiledatarepresentationcustomizer/replacementdepthdata(for:))*