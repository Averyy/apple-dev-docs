# CTQuickSwitchState

**Framework**: Core Telephony  
**Kind**: enum

Values that describe a device’s quick switch status.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
enum CTQuickSwitchState
```

## Topics

### Creating a quick switch state value
- [init?(rawValue: Int)](ctquickswitchstate/init(rawvalue:).md)
  Initializes a quick switch state with the provided value.
### Quick switch states
- [CTQuickSwitchState.active](ctquickswitchstate/active.md)
  This device is the active participant; cellular service is available on this device.
- [CTQuickSwitchState.failed](ctquickswitchstate/failed.md)
  The framework couldn’t determine the state of the device due to an error.
- [CTQuickSwitchState.notEnrolled](ctquickswitchstate/notenrolled.md)
  The device or phone number isn’t enrolled in quick switch.
- [CTQuickSwitchState.passive](ctquickswitchstate/passive.md)
  This device is passive; cellular service is held by another device.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func getDeviceState((CTQuickSwitchState, (any Error)?) -> Void)](ctquickswitchmanager/getdevicestate(_:).md)
  Gets the quick switch state of the current device.
- [func getPhoneNumberState(forSuffix: String, completion: (CTQuickSwitchState, (any Error)?) -> Void)](ctquickswitchmanager/getphonenumberstate(forsuffix:completion:).md)
  Queries the quick switch state for a phone number whose suffix matches the provided phone number suffix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctquickswitchstate)*