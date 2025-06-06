# setProperty

**Framework**: HIDDriverKit  
**Kind**: method

Updates the specified property on the corresponding kernel object.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
void setProperty(OSObject * key, OSObject * value);
```

## Parameters

- `key`: The property key.
- `value`: The property value.

## See Also

- [setProtocol](iouserusbhosthiddevice/setprotocol.md)
  Sets the active protocol to use for communicating with the USB device.
- [setIdle](iouserusbhosthiddevice/setidle.md)
  Sets the device’s idle time.
- [setIdlePolicy](iouserusbhosthiddevice/setidlepolicy.md)
  Sets the amount of idle time that must pass before suspending the device.
- [reset](iouserusbhosthiddevice/reset.md)
  Resets the USB device.
- [USBIdlePolicyType](usbidlepolicytype.md)
  Constants that specify whether to apply the idle policy to an interface or pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/setproperty)*