# setProtocol

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the active protocol to use for communicating with the USB device.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual kern_return_t setProtocol(uint16_t protocol);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

## Discussion

At startup, the [`Start`](./start.md) method sets the protocol to the report protocol.

## Parameters

- `protocol`: The protocol to use for the device. Specify `0` to use the boot protocol or `1` to use the report protocol.

## See Also

### Configuring the Device
- [setIdle](./setidle.md)
  Sets the device’s idle time.
- [setIdlePolicy](./setidlepolicy.md)
  Sets the amount of idle time that must pass before suspending the device.
- [setProperty](./setproperty.md)
  Updates the specified property on the corresponding kernel object.
- [reset](./reset.md)
  Resets the USB device.
- [USBIdlePolicyType](../usbidlepolicytype.md)
  Constants that specify whether to apply the idle policy to an interface or pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/setprotocol)*