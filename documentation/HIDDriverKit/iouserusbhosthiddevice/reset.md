# reset

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Resets the USB device.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual void reset();
```

## See Also

### Configuring the Device
- [setProtocol](./setprotocol.md)
  Sets the active protocol to use for communicating with the USB device.
- [setIdle](./setidle.md)
  Sets the device’s idle time.
- [setIdlePolicy](./setidlepolicy.md)
  Sets the amount of idle time that must pass before suspending the device.
- [setProperty](./setproperty.md)
  Updates the specified property on the corresponding kernel object.
- [USBIdlePolicyType](../usbidlepolicytype.md)
  Constants that specify whether to apply the idle policy to an interface or pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/reset)*