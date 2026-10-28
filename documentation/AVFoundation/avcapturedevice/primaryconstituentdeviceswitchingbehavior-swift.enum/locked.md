# AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.locked

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

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

```c
AVCapturePrimaryConstituentDeviceSwitchingBehaviorLocked
```

## Discussion

A locked value restricts the [`minAvailableVideoZoomFactor`](../minavailablevideozoomfactor.md) property value to the switch-over zoom factor of the active primary constituent device. See [`virtualDeviceSwitchOverVideoZoomFactors`](../virtualdeviceswitchovervideozoomfactors.md) for more information.

## See Also

### Switching behaviors
- [AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.unsupported](./unsupported.md)
  The device doesn’t support constituent device switching.
- [AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.auto](./auto.md)
  The device automatically selects the best camera for the current scene.
- [AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.restricted](./restricted.md)
  The device restricts fallback camera selection to certain conditions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/locked)*