# isDualCameraFusionEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value indicating whether this capture combines image data from a dual camera.

**Availability**:
- iOS 10.2+
- iPadOS 10.2+
- Mac Catalyst 13.1+

## Declaration

```swift
var isDualCameraFusionEnabled: Bool { get }
```

#### Discussion

This property corresponds to the [`AVCapturePhotoSettings`](avcapturephotosettings.md) property [`isAutoDualCameraFusionEnabled`](avcapturephotosettings/isautodualcamerafusionenabled.md).

When this value is [`true`](https://developer.apple.com/documentation/swift/true), a dual-camera device automatically combines samples from both cameras to produce a higher quality image. This property applies only when using the [`builtInDualCamera`](avcapturedevice/devicetype-swift.struct/builtindualcamera.md) device type on supported devices.

If you specify automatic image fusion when requesting a capture, the device automatically chooses whether to use image fusion based on the scene conditions at the moment of capture. Therefore, you don’t know whether the system uses image fusion until right before the moment of capture. When the photo output calls your [`photoOutput(_:willBeginCaptureFor:)`](avcapturephotocapturedelegate/photooutput(_:willbegincapturefor:).md) method (or other delegate methods that occur later in the capture process), you can use this property to determine whether image fusion is active.

## See Also

- [var isFlashEnabled: Bool](avcaptureresolvedphotosettings/isflashenabled.md)
  A Boolean value indicating whether the camera flash fires for this capture.
- [var isRedEyeReductionEnabled: Bool](avcaptureresolvedphotosettings/isredeyereductionenabled.md)
  A Boolean value indicating whether the camera automatically reduces red-eye when capturing photos.
- [var isVirtualDeviceFusionEnabled: Bool](avcaptureresolvedphotosettings/isvirtualdevicefusionenabled.md)
  A Boolean value that specifies whether the system automatically uses virtual device image fusion.
- [var isFastCapturePrioritizationEnabled: Bool](avcaptureresolvedphotosettings/isfastcaptureprioritizationenabled.md)
  A Boolean value that indicates whether the system uses fast capture prioritization when capturing the photo.
- [var isContentAwareDistortionCorrectionEnabled: Bool](avcaptureresolvedphotosettings/iscontentawaredistortioncorrectionenabled.md)
  A Boolean value that indicates whether the system applies content-aware distortion correction when capturing the photo.
- [var isStillImageStabilizationEnabled: Bool](avcaptureresolvedphotosettings/isstillimagestabilizationenabled.md)
  A Boolean value indicating whether this capture uses image stabilization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/isdualcamerafusionenabled)*