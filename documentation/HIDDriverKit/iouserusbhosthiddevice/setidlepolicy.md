# setIdlePolicy

**Framework**: HIDDriverKit  
**Kind**: method

Sets the amount of idle time that must pass before suspending the device.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
virtual kern_return_t setIdlePolicy(USBIdlePolicyType type, uint16_t idleTimeMs);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/driverkit/error-codes).

#### Discussion

Once the interface or pipe is idle, it defers electrical suspension of the device for the specified duration.

## Parameters

- `type`: The target of the idle policy. For a list of possible values, see [`USBIdlePolicyType`](usbidlepolicytype.md).
- `idleTimeMs`: The idle time in milliseconds.

## See Also

- [setProtocol](iouserusbhosthiddevice/setprotocol.md)
  Sets the active protocol to use for communicating with the USB device.
- [setIdle](iouserusbhosthiddevice/setidle.md)
  Sets the device’s idle time.
- [setProperty](iouserusbhosthiddevice/setproperty.md)
  Updates the specified property on the corresponding kernel object.
- [reset](iouserusbhosthiddevice/reset.md)
  Resets the USB device.
- [USBIdlePolicyType](usbidlepolicytype.md)
  Constants that specify whether to apply the idle policy to an interface or pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/setidlepolicy)*