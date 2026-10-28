# GetBusDeviceFunction

**Framework**: PCIDriverKit  
**Kind**: method  
**Role**: Instance Method

Returns the device’s bus, device, and function numbers.

**Availability**:
- DriverKit
- macOS

## Declaration

```cpp
virtual kern_return_t GetBusDeviceFunction(uint8_t *returnBusNumber, uint8_t *returnDeviceNumber, uint8_t *returnFunctionNumber);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

## Parameters

- `returnBusNumber`: A variable in which you want to store the bus number.
- `returnDeviceNumber`: A variable in which you want to store the device number.
- `returnFunctionNumber`: A variable in which you want to store the function number.

## See Also

### Getting Device Information
- [FindPCICapability](./findpcicapability.md)
  Search the configuration space for a PCI capability register.
- [PCI Capabilities](../pci-capabilities-enum.md)
  Constants that you use to get the capabilities of the PCI device.
- [Slot Capabilities](../slot-capabilities-enum.md)
  Constants that you use to get the slot-related capabilities of the PCI device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/iopcidevice/getbusdevicefunction)*