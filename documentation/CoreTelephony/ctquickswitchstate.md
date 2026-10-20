# CTQuickSwitchState

**Framework**: Core Telephony  
**Kind**: enum  
**Role**: Enumeration

Values that describe a device’s quick switch status.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
enum CTQuickSwitchState
```

```c
enum CTQuickSwitchState : NSInteger;
```

## Topics

### Creating a quick switch state value
- [init?(rawValue: Int)](./ctquickswitchstate/init%28rawvalue%29.md)
  Initializes a quick switch state with the provided value.
### Quick switch states
- [CTQuickSwitchState.active](./ctquickswitchstate/active.md)
  This device is the active participant; cellular service is available on this device.
- [CTQuickSwitchState.failed](./ctquickswitchstate/failed.md)
  The framework couldn’t determine the state of the device due to an error.
- [CTQuickSwitchState.notEnrolled](./ctquickswitchstate/notenrolled.md)
  The device or phone number isn’t enrolled in quick switch.
- [CTQuickSwitchState.passive](./ctquickswitchstate/passive.md)
  This device is passive; cellular service is held by another device.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Checking the state of a device
- [func getDeviceState((CTQuickSwitchState, (any Error)?) -> Void)](./ctquickswitchmanager/getdevicestate%28_%29.md)
  Gets the quick switch state of the current device.
- [func getPhoneNumberState(forSuffix: String, completion: (CTQuickSwitchState, (any Error)?) -> Void)](./ctquickswitchmanager/getphonenumberstate%28forsuffix,completion%29.md)
  Queries the quick switch state for a phone number whose suffix matches the provided phone number suffix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctquickswitchstate)*