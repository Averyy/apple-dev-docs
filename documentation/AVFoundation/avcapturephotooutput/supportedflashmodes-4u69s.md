# supportedFlashModes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The flash settings this capture output currently supports.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- tvOS 17.0+

## Declaration

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * supportedFlashModes;
```

#### Discussion

To set the flash mode for a capture, set the [`flashMode`](../avcapturephotosettings/flashmode.md) property of your photo settings object to one of the [`AVCaptureDevice.FlashMode`](../avcapturedevice/flashmode-swift.enum.md) values listed in this array.

This property supports key-value observing.

## See Also

### Determining available settings
- [var isContentAwareDistortionCorrectionSupported: Bool](./iscontentawaredistortioncorrectionsupported.md)
  A Boolean value that indicates whether the session’s current configuration supports content-aware distortion correction.
- [var isContentAwareDistortionCorrectionEnabled: Bool](./iscontentawaredistortioncorrectionenabled.md)
  A Boolean value that indicates whether the photo render pipeline can perform content-aware distortion correction.
- [var isLensStabilizationDuringBracketedCaptureSupported: Bool](./islensstabilizationduringbracketedcapturesupported.md)
  A Boolean value indicating whether the capture output currently supports lens stabilization during bracketed image capture.
- [var maxBracketedCapturePhotoCount: Int](./maxbracketedcapturephotocount.md)
  The maximum number of images that the photo capture output can support in a single bracketed capture.
- [var isAutoRedEyeReductionSupported: Bool](./isautoredeyereductionsupported.md)
  A Boolean value indicating whether the capture output supports automatic red-eye reduction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/supportedflashmodes-4u69s)*