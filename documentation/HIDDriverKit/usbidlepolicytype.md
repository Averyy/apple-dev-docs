# USBIdlePolicyType

**Framework**: HIDDriverKit  
**Kind**: enum

Constants that specify whether to apply the idle policy to an interface or pipe.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
typedef enum { ... } USBIdlePolicyType;
```

## Topics

### Getting the Idle Policy
- [USBIdlePolicyTypeInterface](usbidlepolicytype/usbidlepolicytypeinterface.md)
  An idle policy that applies to the interface connected to the device.
- [USBIdlePolicyTypePipe](usbidlepolicytype/usbidlepolicytypepipe.md)
  An idle policy that applies to the pipe that communicates with the device.

## See Also

- [setProtocol](iouserusbhosthiddevice/setprotocol.md)
  Sets the active protocol to use for communicating with the USB device.
- [setIdle](iouserusbhosthiddevice/setidle.md)
  Sets the device’s idle time.
- [setIdlePolicy](iouserusbhosthiddevice/setidlepolicy.md)
  Sets the amount of idle time that must pass before suspending the device.
- [setProperty](iouserusbhosthiddevice/setproperty.md)
  Updates the specified property on the corresponding kernel object.
- [reset](iouserusbhosthiddevice/reset.md)
  Resets the USB device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/usbidlepolicytype)*