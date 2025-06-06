# Power Management Control/Status Register

**Framework**: PCIDriverKit

Constants you use when checking bits in the power management register.

## Topics

### Register Bits
- [kPCIPMCSPowerStateD0](kpcipmcspowerstated0.md)
  The device is in the D0 state.
- [kPCIPMCSPowerStateD1](kpcipmcspowerstated1.md)
  The device is in the D1 state.
- [kPCIPMCSPowerStateD2](kpcipmcspowerstated2.md)
  The device is in the D2 state.
- [kPCIPMCSPowerStateD3](kpcipmcspowerstated3.md)
  The device is in the D3 state.
- [kPCIPMCSPowerStateMask](kpcipmcspowerstatemask.md)
  A bit mask you use to determine the current power state of the device.
- [kPCIPMCSPMEEnable](kpcipmcspmeenable.md)
  The bit that specifies whether power management events are enabled.
- [kPCIPMCSPMEStatus](kpcipmcspmestatus.md)
  The bit that contains the current state of power management events.
- [kPCIPMCSDefaultEnableBits](kpcipmcsdefaultenablebits.md)
  The default power management settings.
- [kPCIPMCSPMEDisableInS3](kpcipmcspmedisableins3.md)
  A bit for a custom power management event.
- [kPCIPMCSPMEWakeReason](kpcipmcspmewakereason.md)
  A bit that indicates the reason for waking the device.

## See Also

- [HasPCIPowerManagement](iopcidevice/haspcipowermanagement.md)
  Determines whether the device has the specified PCI bus power management capabilities.
- [EnablePCIPowerManagement](iopcidevice/enablepcipowermanagement.md)
  Configures the device’s PCI bus power management capabilities.
- [Power Management Capabilities](power-management-capabilities-enum.md)
  Constants you use to get and set the state of the device’s power management features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/power-management-control-status-register-enum)*