# Power Management Capabilities

**Framework**: PCIDriverKit

Constants you use to get and set the state of the device’s power management features.

## Topics

### Capabilities Registers
- [kPCIPMCPMESupportFromD0](kpcipmcpmesupportfromd0.md)
  The full-power state of the device, in which the device is running and fully operational.
- [kPCIPMCPMESupportFromD1](kpcipmcpmesupportfromd1.md)
  A low-power state of the device, in which the device is handling only configuration and message requests.
- [kPCIPMCPMESupportFromD2](kpcipmcpmesupportfromd2.md)
  A low-power state of the device, in which the device is not in use.
- [kPCIPMCPMESupportFromD3Hot](kpcipmcpmesupportfromd3hot.md)
  A low-power state of the device, in which the device is running in a limited capacity.
- [kPCIPMCPMESupportFromD3Cold](kpcipmcpmesupportfromd3cold.md)
  The state where the device has no power.
- [kPCIPMCD1Support](kpcipmcd1support.md)
  A constant that indicates the device supports the D1 state.
- [kPCIPMCD2Support](kpcipmcd2support.md)
  A constant that indicates the device supports the D2 state.
- [kPCIPMCD3Support](kpcipmcd3support.md)
  A constant that indicates the device supports the D3 state.

## See Also

- [HasPCIPowerManagement](iopcidevice/haspcipowermanagement.md)
  Determines whether the device has the specified PCI bus power management capabilities.
- [EnablePCIPowerManagement](iopcidevice/enablepcipowermanagement.md)
  Configures the device’s PCI bus power management capabilities.
- [Power Management Control/Status Register](power-management-control-status-register-enum.md)
  Constants you use when checking bits in the power management register.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/power-management-capabilities-enum)*