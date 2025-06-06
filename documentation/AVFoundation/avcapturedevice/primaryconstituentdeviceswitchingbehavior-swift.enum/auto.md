# AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.auto

**Framework**: AVFoundation  
**Kind**: case

The device automatically selects the best camera for the current scene.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+

## Declaration

```swift
case auto
```

#### Discussion

This mode places no restrictions on when a camera switch can occur.

## See Also

- [AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.unsupported](avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/unsupported.md)
  The device doesn’t support constituent device switching.
- [AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.restricted](avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/restricted.md)
  The device restricts fallback camera selection to certain conditions.
- [AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.locked](avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/locked.md)
  The device locks camera switching to the active primary constituent device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/auto)*