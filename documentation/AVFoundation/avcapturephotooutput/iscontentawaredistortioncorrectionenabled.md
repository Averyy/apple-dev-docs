# isContentAwareDistortionCorrectionEnabled

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, getter=isContentAwareDistortionCorrectionEnabled) BOOL contentAwareDistortionCorrectionEnabled;
```

## Discussion

You can set this value to true only if [`isContentAwareDistortionCorrectionSupported`](./iscontentawaredistortioncorrectionsupported.md) returns true.

Applying distortion correction to preserve natural-looking content may result in a small change in the field of view compared to what you see in [`AVCaptureVideoPreviewLayer`](../avcapturevideopreviewlayer.md). The amount lost or gained is content specific and varies from photo to photo.

Enabling this property requires a lengthy reconfiguration of the capture render pipeline, so set this property to [`true`](../../Swift/true.md) before calling [`startRunning()`](../avcapturesession/startrunning%28%29.md) on the capture session.

## See Also

### Determining available settings
- [var isContentAwareDistortionCorrectionSupported: Bool](./iscontentawaredistortioncorrectionsupported.md)
  A Boolean value that indicates whether the session’s current configuration supports content-aware distortion correction.
- [var isLensStabilizationDuringBracketedCaptureSupported: Bool](./islensstabilizationduringbracketedcapturesupported.md)
  A Boolean value indicating whether the capture output currently supports lens stabilization during bracketed image capture.
- [var maxBracketedCapturePhotoCount: Int](./maxbracketedcapturephotocount.md)
  The maximum number of images that the photo capture output can support in a single bracketed capture.
- [var supportedFlashModes: [AVCaptureDevice.FlashMode]](./supportedflashmodes-1n6nm.md)
  A Swift array of flash settings this capture output currently supports.
- [var isAutoRedEyeReductionSupported: Bool](./isautoredeyereductionsupported.md)
  A Boolean value indicating whether the capture output supports automatic red-eye reduction.
- [supportedFlashModes](./supportedflashmodes-4u69s.md)
  The flash settings this capture output currently supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/iscontentawaredistortioncorrectionenabled)*