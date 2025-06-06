# AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.unsupported

**Framework**: AVFoundation  
**Kind**: case

The device doesn’t support constituent device switching.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+

## Declaration

```swift
case unsupported
```

#### Discussion

Switching cameras isn’t supported on devices that don’t have more than one constituent device.

## See Also

- [AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.auto](avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/auto.md)
  The device automatically selects the best camera for the current scene.
- [AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.restricted](avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/restricted.md)
  The device restricts fallback camera selection to certain conditions.
- [AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.locked](avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/locked.md)
  The device locks camera switching to the active primary constituent device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/unsupported)*