# AbortDeviceConfigurationChange

**Framework**: AudioDriverKit  
**Kind**: method

Tells the device to stop handling a configuration change.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t AbortDeviceConfigurationChange(uint64_t in_change_action, OSObject * in_change_info);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

The host calls this method to tell the driver not to perform a configuration change previously requested by the host method `RequestDeviceConfigurationChange`. Subclass and override this method to abort the change, then call the superclass to update the I/O state.

## Parameters

- `in_change_action`: A   indicating the action that the device object takes. This is the same value previously passed to  . This value is purely for the clock device’s usage; the host doesn’t look at this value.
- `in_change_info`: A pointer to an   about the configuration change. This is the same value previously passed to  . This value is purely for the clock device’s usage; the host doesn’t look at this value. Retain and release this object reference as needed.

## See Also

- [PerformDeviceConfigurationChange](iouseraudiodevice/performdeviceconfigurationchange.md)
  Tells the device to handle a configuration change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/abortdeviceconfigurationchange)*