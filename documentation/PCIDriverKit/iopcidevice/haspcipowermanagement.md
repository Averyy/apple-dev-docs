# HasPCIPowerManagement

**Framework**: PCIDriverKit  
**Kind**: method

Determines whether the device has the specified PCI bus power management capabilities.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
kern_return_t HasPCIPowerManagement(uint64_t state);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) if the specified state is supported, or another value if isn’t supported. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

#### Discussion

- state: The flags for the power management capabilities you want to check. If you specify `0`, this method checks for the power-management information in the device’s registry. For a list of possible flags, see [`Power Management Capabilities`](power-management-capabilities-enum.md).

## See Also

- [EnablePCIPowerManagement](iopcidevice/enablepcipowermanagement.md)
  Configures the device’s PCI bus power management capabilities.
- [Power Management Capabilities](power-management-capabilities-enum.md)
  Constants you use to get and set the state of the device’s power management features.
- [Power Management Control/Status Register](power-management-control-status-register-enum.md)
  Constants you use when checking bits in the power management register.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/iopcidevice/haspcipowermanagement)*