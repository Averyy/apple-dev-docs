# CTQuickSwitchState.passive

**Framework**: Core Telephony  
**Kind**: case  
**Role**: Case

This device is passive; cellular service is held by another device.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
case passive
```

```c
CTQuickSwitchStatePassive
```

## See Also

### Quick switch states
- [CTQuickSwitchState.active](./active.md)
  This device is the active participant; cellular service is available on this device.
- [CTQuickSwitchState.failed](./failed.md)
  The framework couldn’t determine the state of the device due to an error.
- [CTQuickSwitchState.notEnrolled](./notenrolled.md)
  The device or phone number isn’t enrolled in quick switch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctquickswitchstate/passive)*