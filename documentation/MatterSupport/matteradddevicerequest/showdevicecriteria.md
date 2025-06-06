# showDeviceCriteria

**Framework**: MatterSupport  
**Kind**: property

A predicate that filters what devices appear in the picker.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
var showDeviceCriteria: MatterAddDeviceRequest.DeviceCriteria
```

#### Discussion

During setup user interface flows, the system may present a picker to choose the device to set up. Only devices that match the specified criteria appear in the picker.

Use `.allDevices` to display all devices. Use `.not(...)` to hide blocked devices, such as those already paired in the ecosystem.

## See Also

- [MatterAddDeviceRequest.DeviceCriteria](matteradddevicerequest/devicecriteria.md)
  A predicate to match against possible devices that may appear in the picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddevicerequest/showdevicecriteria)*