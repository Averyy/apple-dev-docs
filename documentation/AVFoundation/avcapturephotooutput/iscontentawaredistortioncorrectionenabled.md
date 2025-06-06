# isContentAwareDistortionCorrectionEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the photo render pipeline can perform content-aware distortion correction.

**Availability**:
- iOS 14.1+
- iPadOS 14.1+
- Mac Catalyst 14.1+
- tvOS 17.0+

## Declaration

```swift
var isContentAwareDistortionCorrectionEnabled: Bool { get set }
```

#### Discussion

You can set this value to true only if [`isContentAwareDistortionCorrectionSupported`](avcapturephotooutput/iscontentawaredistortioncorrectionsupported.md) returns true.

Applying distortion correction to preserve natural-looking content may result in a small change in the field of view compared to what you see in [`AVCaptureVideoPreviewLayer`](avcapturevideopreviewlayer.md). The amount lost or gained is content specific and varies from photo to photo.

Enabling this property requires a lengthy reconfiguration of the capture render pipeline, so set this property to [`true`](https://developer.apple.com/documentation/swift/true) before calling [`startRunning()`](avcapturesession/startrunning().md) on the capture session.

## See Also

- [var isContentAwareDistortionCorrectionSupported: Bool](avcapturephotooutput/iscontentawaredistortioncorrectionsupported.md)
  A Boolean value that indicates whether the session’s current configuration supports content-aware distortion correction.
- [var isLensStabilizationDuringBracketedCaptureSupported: Bool](avcapturephotooutput/islensstabilizationduringbracketedcapturesupported.md)
  A Boolean value indicating whether the capture output currently supports lens stabilization during bracketed image capture.
- [var maxBracketedCapturePhotoCount: Int](avcapturephotooutput/maxbracketedcapturephotocount.md)
  The maximum number of images that the photo capture output can support in a single bracketed capture.
- [var supportedFlashModes: [AVCaptureDevice.FlashMode]](avcapturephotooutput/supportedflashmodes-1n6nm.md)
  A Swift array of flash settings this capture output currently supports.
- [var isAutoRedEyeReductionSupported: Bool](avcapturephotooutput/isautoredeyereductionsupported.md)
  A Boolean value indicating whether the capture output supports automatic red-eye reduction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/iscontentawaredistortioncorrectionenabled)*