# PerformDeviceConfigurationChange

**Framework**: AudioDriverKit  
**Kind**: method

Tells the device to handle a configuration change.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
kern_return_t PerformDeviceConfigurationChange(uint64_t in_change_action, OSObject * in_change_info);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

The host calls this method to allow the clock device to perform a configuration change. This call can result from a call to `RequestDeviceConfigurationChange` or a from change to an I/O state that requires a configuration change.

Subclass and override this method to handle any custom configuration change requests, then call the superclass to update the I/O state. The framework stops I/O prior to performing the configuration change.

## Parameters

- `in_change_action`: A   that indicates the action the device object takes. This is the same value previously passed to  . This value is purely for the device’s usage; the host doesn’t look at this value.
- `in_change_info`: A pointer to an   about the configuration change. This is the same value previously passed to  . This value is purely for the clock device’s usage; the host doesn’t look at this value. Retain and release this object reference as needed.

## See Also

- [AbortDeviceConfigurationChange](iouseraudiodevice/abortdeviceconfigurationchange.md)
  Tells the device to stop handling a configuration change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudiodevice/performdeviceconfigurationchange)*