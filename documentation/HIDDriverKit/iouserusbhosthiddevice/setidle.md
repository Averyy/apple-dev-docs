# setIdle

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Sets the device’s idle time.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual kern_return_t setIdle(uint16_t idleTimeMs);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

## Discussion

The idle rate determines how often a device resends data that hasn’t changed since the last report. Use this method to limit the reporting frequency of an interrupt `IN` endpoint.

## Parameters

- `idleTimeMs`: The idle time in milliseconds.

## See Also

### Configuring the Device
- [setProtocol](./setprotocol.md)
  Sets the active protocol to use for communicating with the USB device.
- [setIdlePolicy](./setidlepolicy.md)
  Sets the amount of idle time that must pass before suspending the device.
- [setProperty](./setproperty.md)
  Updates the specified property on the corresponding kernel object.
- [reset](./reset.md)
  Resets the USB device.
- [USBIdlePolicyType](../usbidlepolicytype.md)
  Constants that specify whether to apply the idle policy to an interface or pipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iouserusbhosthiddevice/setidle)*