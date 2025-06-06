# AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.locked

**Framework**: AVFoundation  
**Kind**: case

The device locks camera switching to the active primary constituent device.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+

## Declaration

```swift
case locked
```

#### Discussion

A locked value restricts the [`minAvailableVideoZoomFactor`](avcapturedevice/minavailablevideozoomfactor.md) property value to the switch-over zoom factor of the active primary constituent device. See [`virtualDeviceSwitchOverVideoZoomFactors`](avcapturedevice/virtualdeviceswitchovervideozoomfactors.md) for more information.

## See Also

- [AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.unsupported](avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/unsupported.md)
  The device doesn’t support constituent device switching.
- [AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.auto](avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/auto.md)
  The device automatically selects the best camera for the current scene.
- [AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.restricted](avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/restricted.md)
  The device restricts fallback camera selection to certain conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/locked)*