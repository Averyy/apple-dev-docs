# ChangePowerState

**Framework**: DriverKit  
**Kind**: method

Changes the device’s power state to the specified level.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t ChangePowerState(uint32_t powerFlags);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. For a list of error codes, see [`Error Codes`](error-codes.md).

#### Discussion

If the new state is different than the device’s current state, this method places an asynchronous request to change the state to the new value. If the change is successful, the system subsequently calls the [`SetPowerState`](ioservice/setpowerstate.md) method of your service.

## Parameters

- `powerFlags`: The new power state for the device. Typically, you specify only   for this parameter. For a list of all possible values, see  .

## See Also

- [SetPowerState](ioservice/setpowerstate.md)
  Updates the service in response to power-related changes for a provider.
- [Service Power Capabilities](3325571-service_power_capabilities.md)
  Constants that indicate the power state of a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioservice/changepowerstate)*