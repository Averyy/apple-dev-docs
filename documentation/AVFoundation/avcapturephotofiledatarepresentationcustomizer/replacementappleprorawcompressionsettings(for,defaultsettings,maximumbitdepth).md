# replacementAppleProRAWCompressionSettings(for:defaultSettings:maximumBitDepth:)

**Framework**: AVFoundation  
**Kind**: method

Replaces the compression settings the system uses when writing Apple ProRAW data to a Linear DNG file.

**Availability**:
- iOS 14.3+
- iPadOS 14.3+
- Mac Catalyst 14.3+
- tvOS 17.0+

## Declaration

```swift
optional func replacementAppleProRAWCompressionSettings(for photo: AVCapturePhoto, defaultSettings: [String : Any], maximumBitDepth: Int) -> [String : Any]
```

#### Return Value

A dictionary that contains the replacement compression settings.

#### Discussion

The system calls this method when writing an Apple ProRAW image to a DNG file. To configure the compression settings the system uses when writing the file, return a dictionary that contains values for the following keys:

- [`AVVideoQualityKey`](avvideoqualitykey.md). A floating-point value from 0.0 to 1.0. Specify a value of 1.0 to use lossless compression, or less than 1.0 for lossy compression.
- [`AVVideoAppleProRAWBitDepthKey`](avvideoappleprorawbitdepthkey.md). An integer value from 8 to `maximumBitDepth`. Setting this key to a value less than the value specified in `defaultSettings` may result in quantization losses.

Any keys not specified in the returned dictionary use the values from the `defaultSettings` dictionary. If your delegate object doesn’t implement this method, the system uses the default compression settings for DNG files.

## Parameters

- `photo`: The calling photo instance.
- `defaultSettings`: The default settings to use, if not overridden.
- `maximumBitDepth`: The maximum bit depth you can specify in the returned settings dictionary.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotofiledatarepresentationcustomizer/replacementappleprorawcompressionsettings(for:defaultsettings:maximumbitdepth:))*