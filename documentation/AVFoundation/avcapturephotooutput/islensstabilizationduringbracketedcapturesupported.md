# isLensStabilizationDuringBracketedCaptureSupported

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the capture output currently supports lens stabilization during bracketed image capture.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isLensStabilizationDuringBracketedCaptureSupported: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isLensStabilizationDuringBracketedCaptureSupported) BOOL lensStabilizationDuringBracketedCaptureSupported;
```

#### Discussion

To make use of optical image stabilization across the entire duration of a bracketed capture, set the [`isLensStabilizationEnabled`](../avcapturephotobracketsettings/islensstabilizationenabled.md) property of your bracketed photo settings object.

> **Note**:  This property’s value can change if the [`sessionPreset`](../avcapturesession/sessionpreset.md) property of the current capture session or the [`activeFormat`](../avcapturedevice/activeformat.md) property of the underlying capture device changes.

This property supports key-value observing.

## See Also

### Determining available settings
- [var isContentAwareDistortionCorrectionSupported: Bool](./iscontentawaredistortioncorrectionsupported.md)
  A Boolean value that indicates whether the session’s current configuration supports content-aware distortion correction.
- [var isContentAwareDistortionCorrectionEnabled: Bool](./iscontentawaredistortioncorrectionenabled.md)
  A Boolean value that indicates whether the photo render pipeline can perform content-aware distortion correction.
- [var maxBracketedCapturePhotoCount: Int](./maxbracketedcapturephotocount.md)
  The maximum number of images that the photo capture output can support in a single bracketed capture.
- [var supportedFlashModes: [AVCaptureDevice.FlashMode]](./supportedflashmodes-1n6nm.md)
  A Swift array of flash settings this capture output currently supports.
- [var isAutoRedEyeReductionSupported: Bool](./isautoredeyereductionsupported.md)
  A Boolean value indicating whether the capture output supports automatic red-eye reduction.
- [supportedFlashModes](./supportedflashmodes-4u69s.md)
  The flash settings this capture output currently supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/islensstabilizationduringbracketedcapturesupported)*