# AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.auto

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

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

```c
AVCapturePrimaryConstituentDeviceSwitchingBehaviorAuto
```

## Discussion

This mode places no restrictions on when a camera switch can occur.

## See Also

### Switching behaviors
- [AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.unsupported](./unsupported.md)
  The device doesn’t support constituent device switching.
- [AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.restricted](./restricted.md)
  The device restricts fallback camera selection to certain conditions.
- [AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior.locked](./locked.md)
  The device locks camera switching to the active primary constituent device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/primaryconstituentdeviceswitchingbehavior-swift.enum/auto)*