# isDualCameraFusionSupported

**Framework**: AVFoundation  
**Kind**: property

A Boolean value indicating whether the capture output currently supports automatically combining image data on a dual camera device.

**Availability**:
- iOS 10.2+
- iPadOS 10.2+
- Mac Catalyst 13.1+

## Declaration

```swift
var isDualCameraFusionSupported: Bool { get }
```

#### Discussion

On devices equipped with a dual camera, image fusion combines samples from both cameras to produce a higher quality image.

To capture a photo with image fusion, set the [`isAutoDualCameraFusionEnabled`](avcapturephotosettings/isautodualcamerafusionenabled.md) property of your photo settings object. If a device does not support image fusion, setting the [`isAutoDualCameraFusionEnabled`](avcapturephotosettings/isautodualcamerafusionenabled.md) property has no effect (that is, the resolved [`isDualCameraFusionEnabled`](avcaptureresolvedphotosettings/isdualcamerafusionenabled.md) setting will always be false).

> **Note**:  This property’s value can change if the [`sessionPreset`](avcapturesession/sessionpreset.md) property of the current capture session or the [`activeFormat`](avcapturedevice/activeformat.md) property of the underlying capture device changes.

 This property’s value can change if the [`sessionPreset`](avcapturesession/sessionpreset.md) property of the current capture session or the [`activeFormat`](avcapturedevice/activeformat.md) property of the underlying capture device changes.

This property supports key-value observing.

## See Also

- [var isDualCameraDualPhotoDeliverySupported: Bool](avcapturephotooutput/isdualcameradualphotodeliverysupported.md)
  A Boolean value indicating whether the capture output currently supports simultaneous photo capture with both cameras on a dual-camera device.
- [var isDualCameraDualPhotoDeliveryEnabled: Bool](avcapturephotooutput/isdualcameradualphotodeliveryenabled.md)
  A Boolean value that specifies whether to configure the capture pipeline for simultaneous photo capture with both cameras on a dual-camera device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isdualcamerafusionsupported)*