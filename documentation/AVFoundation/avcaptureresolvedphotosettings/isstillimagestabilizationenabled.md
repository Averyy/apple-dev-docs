# isStillImageStabilizationEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value indicating whether this capture uses image stabilization.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+

## Declaration

```swift
var isStillImageStabilizationEnabled: Bool { get }
```

#### Discussion

This property corresponds to the [`AVCapturePhotoSettings`](avcapturephotosettings.md) property [`isAutoStillImageStabilizationEnabled`](avcapturephotosettings/isautostillimagestabilizationenabled.md).

When this value is [`true`](https://developer.apple.com/documentation/swift/true), the device automatically applies stabilization in low-light conditions to counteract hand shake. Automatic stabilization always includes digital image stabilization, and may also include optical lens stabilization, based on the current device.

If you specify automatic stabilization when requesting a capture, the device automatically chooses whether to use image stabilization based on the scene contents at the moment of capture. Therefore, you don’t know whether the system uses stabilization until right before the moment of capture. When the photo output calls your [`photoOutput(_:willBeginCaptureFor:)`](avcapturephotocapturedelegate/photooutput(_:willbegincapturefor:).md) method (or other delegate methods that occur later in the capture process), you can use this property to determine whether stabilization is active.

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
- [var isDualCameraFusionEnabled: Bool](avcaptureresolvedphotosettings/isdualcamerafusionenabled.md)
  A Boolean value indicating whether this capture combines image data from a dual camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/isstillimagestabilizationenabled)*