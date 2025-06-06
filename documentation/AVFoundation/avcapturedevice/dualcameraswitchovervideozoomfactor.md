# dualCameraSwitchOverVideoZoomFactor

**Framework**: AVFoundation  
**Kind**: property

The video zoom factor at which a dual camera device can automatically switch between cameras.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var dualCameraSwitchOverVideoZoomFactor: CGFloat { get }
```

#### Discussion

A dual camera device (see [`builtInDualCamera`](avcapturedevice/devicetype-swift.struct/builtindualcamera.md)) contains both wide-angle and telephoto cameras.

This property’s value is the zoom factor at which the zoomed field of view from the wide-angle camera matches the full field of view from the telephoto camera. When the [`videoZoomFactor`](avcapturedevice/videozoomfactor.md) setting meets or exceeds this value, the device can automatically chooses which camera provides output imagery (or automatically combine imagery from both to create final output) based on scene conditions. For zoom factors below this value, the device always uses imagery from the wide-angle camera.

On a single-camera device, this value is always `1.0`.

## See Also

- [var minAvailableVideoZoomFactor: CGFloat](avcapturedevice/minavailablevideozoomfactor.md)
  The minimum zoom factor allowed in the current capture configuration.
- [var maxAvailableVideoZoomFactor: CGFloat](avcapturedevice/maxavailablevideozoomfactor.md)
  The maximum zoom factor allowed in the current capture configuration.
- [var virtualDeviceSwitchOverVideoZoomFactors: [NSNumber]](avcapturedevice/virtualdeviceswitchovervideozoomfactors.md)
  An array of video zoom factors at or above which a virtual device, such as the dual camera, may switch to its next constituent device.
- [var displayVideoZoomFactorMultiplier: CGFloat](avcapturedevice/displayvideozoomfactormultiplier.md)
  A video zoom factor multiplier to use when displaying zoom information in a user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/dualcameraswitchovervideozoomfactor)*