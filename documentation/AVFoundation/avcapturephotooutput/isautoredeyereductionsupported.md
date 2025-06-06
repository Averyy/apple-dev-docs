# isAutoRedEyeReductionSupported

**Framework**: AVFoundation  
**Kind**: property

A Boolean value indicating whether the capture output supports automatic red-eye reduction.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isAutoRedEyeReductionSupported: Bool { get }
```

#### Discussion

In iOS 12 and later, AVFoundation applies a red-eye reduction effect only when needed. It won’t apply red-eye reduction in the following situations:

- When you force a flash capture in good light
- When only one eye is visible
- When doing a bracketed capture
- When taking a picture with depth on the dual camera

When taking RAW + processed (JPEG or HEIC) still-photo capture with auto red-eye reduction enabled, AVFoundation applies correction to only the processed photo,  the RAW photo.

## See Also

- [var isContentAwareDistortionCorrectionSupported: Bool](avcapturephotooutput/iscontentawaredistortioncorrectionsupported.md)
  A Boolean value that indicates whether the session’s current configuration supports content-aware distortion correction.
- [var isContentAwareDistortionCorrectionEnabled: Bool](avcapturephotooutput/iscontentawaredistortioncorrectionenabled.md)
  A Boolean value that indicates whether the photo render pipeline can perform content-aware distortion correction.
- [var isLensStabilizationDuringBracketedCaptureSupported: Bool](avcapturephotooutput/islensstabilizationduringbracketedcapturesupported.md)
  A Boolean value indicating whether the capture output currently supports lens stabilization during bracketed image capture.
- [var maxBracketedCapturePhotoCount: Int](avcapturephotooutput/maxbracketedcapturephotocount.md)
  The maximum number of images that the photo capture output can support in a single bracketed capture.
- [var supportedFlashModes: [AVCaptureDevice.FlashMode]](avcapturephotooutput/supportedflashmodes-1n6nm.md)
  A Swift array of flash settings this capture output currently supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isautoredeyereductionsupported)*