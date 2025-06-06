# supportedFlashModes

**Framework**: AVFoundation  
**Kind**: property

A Swift array of flash settings this capture output currently supports.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 17.0+

## Declaration

```swift
@nonobjc
var supportedFlashModes: [AVCaptureDevice.FlashMode] { get }
```

#### Discussion

To set the flash mode for a capture, set the [`flashMode`](avcapturephotosettings/flashmode.md) property of your photo settings object to one of the [`AVCaptureDevice.FlashMode`](avcapturedevice/flashmode-swift.enum.md) values listed in this array.

This property supports Key-Value Observing.

## See Also

- [var isContentAwareDistortionCorrectionSupported: Bool](avcapturephotooutput/iscontentawaredistortioncorrectionsupported.md)
  A Boolean value that indicates whether the session’s current configuration supports content-aware distortion correction.
- [var isContentAwareDistortionCorrectionEnabled: Bool](avcapturephotooutput/iscontentawaredistortioncorrectionenabled.md)
  A Boolean value that indicates whether the photo render pipeline can perform content-aware distortion correction.
- [var isLensStabilizationDuringBracketedCaptureSupported: Bool](avcapturephotooutput/islensstabilizationduringbracketedcapturesupported.md)
  A Boolean value indicating whether the capture output currently supports lens stabilization during bracketed image capture.
- [var maxBracketedCapturePhotoCount: Int](avcapturephotooutput/maxbracketedcapturephotocount.md)
  The maximum number of images that the photo capture output can support in a single bracketed capture.
- [var isAutoRedEyeReductionSupported: Bool](avcapturephotooutput/isautoredeyereductionsupported.md)
  A Boolean value indicating whether the capture output supports automatic red-eye reduction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/supportedflashmodes-1n6nm)*