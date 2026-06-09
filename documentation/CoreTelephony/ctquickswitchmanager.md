# CTQuickSwitchManager

**Framework**: Core Telephony  
**Kind**: class

An object that enables an app to register and query a device’s quick switch state.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
class CTQuickSwitchManager
```

## Topics

### Getting the state of the device
- [func getDeviceState((CTQuickSwitchState, (any Error)?) -> Void)](ctquickswitchmanager/getdevicestate(_:).md)
  Gets the quick switch state of the current device.
- [func getPhoneNumberState(forSuffix: String, completion: (CTQuickSwitchState, (any Error)?) -> Void)](ctquickswitchmanager/getphonenumberstate(forsuffix:completion:).md)
  Queries the quick switch state for a phone number whose suffix matches the provided phone number suffix.
### Registering and unregistering a device
- [func registerForLaunch(onQuickSwitchStateEvents: ((any Error)?) -> Void)](ctquickswitchmanager/registerforlaunch(onquickswitchstateevents:).md)
  Registers the calling app for background launch whenever the device’s quick switch state changes.
- [func unregisterForLaunch(onQuickSwitchStateEvents: ((any Error)?) -> Void)](ctquickswitchmanager/unregisterforlaunch(onquickswitchstateevents:).md)
  Removes the calling app’s registration for background launch on quick switch state changes.
### Responding to changes in the quick switch state
- [var delegate: (any CTQuickSwitchManager.Delegate)?](ctquickswitchmanager/delegate-swift.property.md)
  An object the system notifies to respond to quick switch events.
- [func quickSwitchManager(CTQuickSwitchManager, didChangeTo: CTQuickSwitchState)](ctquickswitchmanager/delegate-swift.protocol/quickswitchmanager(_:didchangeto:).md)
  Indicates there’s been a change in device’s quick switch state.
- [enum CTQuickSwitchState](ctquickswitchstate.md)
  Values that describe a device’s quick switch status.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any CTQuickSwitchManager.Delegate)?](ctquickswitchmanager/delegate-swift.property.md)
  An object the system notifies to respond to quick switch events.
- [CTQuickSwitchManager.Delegate](ctquickswitchmanager/delegate-swift.protocol.md)
  Methods you implement to respond to changes in a device’s quick switch state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretelephony/ctquickswitchmanager)*