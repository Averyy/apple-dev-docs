# AbortDeviceConfigurationChange

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Tells the clock device to stop handling a configuration change.

**Availability**:
- DriverKit 21.0+

## Declaration

```cpp
virtual kern_return_t AbortDeviceConfigurationChange(uint64_t change_action, OSObject *in_change_info);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [Error Codes](../../DriverKit/error-codes.md).

#### Discussion

The host calls this method to tell the driver not to perform a configuration change previously requested by the host method `RequestDeviceConfigurationChange`. Subclass and override this method to abort the change, then call the superclass to update the I/O state.

## Parameters

- `change_action`: A `uint64_t` indicating the action that the device object takes. This is the same value previously passed to `RequestDeviceConfigurationChange`. This value is purely for the clock device’s usage; the host doesn’t look at this value.
- `in_change_info`: A pointer to an [`OSObject`](../../DriverKit/osobject.md) about the configuration change. This is the same value previously passed to `RequestDeviceConfigurationChange`. This value is purely for the clock device’s usage; the host doesn’t look at this value. Retain and release this object reference as needed.

## See Also

### Supporting Device Configuration Changes
- [PerformDeviceConfigurationChange](./performdeviceconfigurationchange.md)
  Tells the clock device to handle a configuration change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/abortdeviceconfigurationchange)*