# isContentAwareDistortionCorrectionSupported

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the session’s current configuration supports content-aware distortion correction.

**Availability**:
- iOS 14.1+
- iPadOS 14.1+
- Mac Catalyst 14.1+
- tvOS 17.0+

## Declaration

```swift
var isContentAwareDistortionCorrectionSupported: Bool { get }
```

#### Discussion

Optical design and geometric distortion correction use a rectilinear model that preserves lines but not area, angles, or distance. The wider the field of view of a lens, the greater the areal distortion along the edges of images. Content-aware distortion correction intelligently adjusts its behavior to correct distortions based on the photo’s content. For example, the algorithm may not apply correction to faces in the center of a photo, but may apply it to faces near the photo’s edges.

Switching cameras or formats, or enabling depth data delivery, may result in a change to this property value. When the property changes from [`true`](https://developer.apple.com/documentation/swift/true) to [`false`](https://developer.apple.com/documentation/swift/false), [`isContentAwareDistortionCorrectionEnabled`](avcapturephotooutput/iscontentawaredistortioncorrectionenabled.md) also reverts to [`false`](https://developer.apple.com/documentation/swift/false).

This property is key-value observable.

## See Also

- [var isContentAwareDistortionCorrectionEnabled: Bool](avcapturephotooutput/iscontentawaredistortioncorrectionenabled.md)
  A Boolean value that indicates whether the photo render pipeline can perform content-aware distortion correction.
- [var isLensStabilizationDuringBracketedCaptureSupported: Bool](avcapturephotooutput/islensstabilizationduringbracketedcapturesupported.md)
  A Boolean value indicating whether the capture output currently supports lens stabilization during bracketed image capture.
- [var maxBracketedCapturePhotoCount: Int](avcapturephotooutput/maxbracketedcapturephotocount.md)
  The maximum number of images that the photo capture output can support in a single bracketed capture.
- [var supportedFlashModes: [AVCaptureDevice.FlashMode]](avcapturephotooutput/supportedflashmodes-1n6nm.md)
  A Swift array of flash settings this capture output currently supports.
- [var isAutoRedEyeReductionSupported: Bool](avcapturephotooutput/isautoredeyereductionsupported.md)
  A Boolean value indicating whether the capture output supports automatic red-eye reduction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/iscontentawaredistortioncorrectionsupported)*