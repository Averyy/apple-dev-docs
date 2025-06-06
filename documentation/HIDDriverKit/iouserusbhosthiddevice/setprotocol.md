# setProtocol

**Framework**: HIDDriverKit  
**Kind**: method

Sets the active protocol to use for communicating with the USB device.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
kern_return_t setProtocol(uint16_t protocol);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

At startup, the [`Start`](iouserusbhosthiddevice/start.md) method sets the protocol to the report protocol.

## Parameters

- `protocol`: The protocol to use for the device. Specify   to use the boot protocol or   to use the report protocol.

## See Also

- [setIdle](iouserusbhosthiddevice/setidle.md)
  Sets the device’s idle time.
- [setIdlePolicy](iouserusbhosthiddevice/setidlepolicy.md)
  Sets the amount of idle time that must pass before suspending the device.
- [setProperty](iouserusbhosthiddevice/setproperty.md)
  Updates the specified property on the corresponding kernel object.
- [reset](iouserusbhosthiddevice/reset.md)
  Resets the USB device.
- [USBIdlePolicyType](usbidlepolicytype.md)
  Constants that specify whether to apply the idle policy to an interface or pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/setprotocol)*