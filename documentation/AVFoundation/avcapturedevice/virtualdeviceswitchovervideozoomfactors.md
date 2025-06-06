# virtualDeviceSwitchOverVideoZoomFactors

**Framework**: AVFoundation  
**Kind**: property

An array of video zoom factors at or above which a virtual device, such as the dual camera, may switch to its next constituent device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var virtualDeviceSwitchOverVideoZoomFactors: [NSNumber] { get }
```

#### Discussion

This property contains zoom factors at which the field of view of one constituent device matches the full field of view of the next constituent device. The number of switched-over video zoom factors is always one fewer than the count of the [`constituentDevices`](avcapturedevice/constituentdevices.md) property. These factors progress in the same order as the devices listed in that property.

The value of this property is an empty array for nonvirtual devices.

## See Also

- [var minAvailableVideoZoomFactor: CGFloat](avcapturedevice/minavailablevideozoomfactor.md)
  The minimum zoom factor allowed in the current capture configuration.
- [var maxAvailableVideoZoomFactor: CGFloat](avcapturedevice/maxavailablevideozoomfactor.md)
  The maximum zoom factor allowed in the current capture configuration.
- [var dualCameraSwitchOverVideoZoomFactor: CGFloat](avcapturedevice/dualcameraswitchovervideozoomfactor.md)
  The video zoom factor at which a dual camera device can automatically switch between cameras.
- [var displayVideoZoomFactorMultiplier: CGFloat](avcapturedevice/displayvideozoomfactormultiplier.md)
  A video zoom factor multiplier to use when displaying zoom information in a user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/virtualdeviceswitchovervideozoomfactors)*