# isDualCameraDualPhotoDeliveryEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that specifies whether to configure the capture pipeline for simultaneous photo capture with both cameras on a dual-camera device.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var isDualCameraDualPhotoDeliveryEnabled: Bool { get set }
```

#### Discussion

Enabling this property (on a supported device) allows the capture output to deliver separate images from both the wide-angle and telephoto cameras in a single capture.

Dual photo delivery requires that a capture session set up its internal rendering pipeline differently. If you intend to capture with dual photo delivery at all, set this property to [`true`](https://developer.apple.com/documentation/Swift/true) before calling the [`AVCaptureSession`](avcapturesession.md) [`startRunning()`](avcapturesession/startrunning().md) method. Changing this property while the session is running requires a lengthy reconfiguration of the capture render pipeline: Live Photo captures in progress will end immediately, unfulfilled photo requests will abort, and video preview will temporarily freeze.

You must enable this option before initiating a photo capture with the [`isDualCameraDualPhotoDeliveryEnabled`](avcapturephotosettings/isdualcameradualphotodeliveryenabled.md) property of your photo settings object set to [`true`](https://developer.apple.com/documentation/Swift/true). However, after you’ve enabled this option, you are free to issue photo capture requests both with and without dual photo delivery.

## See Also

- [var isDualCameraFusionSupported: Bool](avcapturephotooutput/isdualcamerafusionsupported.md)
  A Boolean value indicating whether the capture output currently supports automatically combining image data on a dual camera device.
- [var isDualCameraDualPhotoDeliverySupported: Bool](avcapturephotooutput/isdualcameradualphotodeliverysupported.md)
  A Boolean value indicating whether the capture output currently supports simultaneous photo capture with both cameras on a dual-camera device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isdualcameradualphotodeliveryenabled)*