# FindPCICapability

**Framework**: PCIDriverKit  
**Kind**: method

Search the configuration space for a PCI capability register.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
virtual kern_return_t FindPCICapability(uint32_t capabilityID, uint64_t searchOffset, uint64_t *foundCapabilityOffset);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/driverkit/error-codes).

## Parameters

- `capabilityID`: A PCI capability ID. PCI Express devices may support extended capabilities in configuraiton space, starting at offset `0x100`. To search this space, pass an ID that is the negated value of the PCI-SIG assigned ID for the extended capability.
- `searchOffset`: The offset into configuration space at which to start the search.
- `foundCapabilityOffset`: A variable in which you want to store the resulting offset value.

## See Also

- [GetBusDeviceFunction](iopcidevice/getbusdevicefunction.md)
  Returns the device’s bus, device, and function numbers.
- [PCI Capabilities](pci-capabilities-enum.md)
  Constants that you use to get the capabilities of the PCI device.
- [Slot Capabilities](slot-capabilities-enum.md)
  Constants that you use to get the slot-related capabilities of the PCI device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/iopcidevice/findpcicapability)*