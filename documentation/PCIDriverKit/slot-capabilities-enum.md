# Slot Capabilities

**Framework**: PCIDriverKit

Constants that you use to get the slot-related capabilities of the PCI device.

## Topics

### Capabilities
- [kIOPCISlotCapabilitiesBitAttentionButtonPresent](kiopcislotcapabilitiesbitattentionbuttonpresent.md)
  The bit that indicates whether an attention button for this slot is electrically controlled by the chassis.
- [kIOPCISlotCapabilitiesBitPowerControllerPresent](kiopcislotcapabilitiesbitpowercontrollerpresent.md)
  The bit that indicates whether the slot implements a software programmable power controller.
- [kIOPCISlotCapabilitiesBitMRLSensorPresent](kiopcislotcapabilitiesbitmrlsensorpresent.md)
  The bit that indicates whether the chassis for this slot implements an MRL sensor.
- [kIOPCISlotCapabilitiesBitAttentionIndicatorPresent](kiopcislotcapabilitiesbitattentionindicatorpresent.md)
  The bit that indicates whether the chassis electrically controls the attention indicator.
- [kIOPCISlotCapabilitiesBitPowerIndicatorPresent](kiopcislotcapabilitiesbitpowerindicatorpresent.md)
  The bit that indicates whether chassis electrically controls the power indicator.
- [kIOPCISlotCapabilitiesBitHotPlugSurprise](kiopcislotcapabilitiesbithotplugsurprise.md)
  The bit that indicates whether the adaptor might be removed without prior notification.
- [kIOPCISlotCapabilitiesBitHotPlugCapable](kiopcislotcapabilitiesbithotplugcapable.md)
  The bit that indicates whether the slot supports hot-plug operations.
- [kIOPCISlotCapabilitiesBitElectromechanicalInterlockPresent](kiopcislotcapabilitiesbitelectromechanicalinterlockpresent.md)
  The bit that indicates whether the chassis implements an electromechanical interlock for this slot.
- [kIOPCISlotCapabilitiesBitNoCommandCompletedSupport](kiopcislotcapabilitiesbitnocommandcompletedsupport.md)
  The bit that indicates whether the slot generates a software notification when the Hot-Plug controller finishes a command.

## See Also

- [FindPCICapability](iopcidevice/findpcicapability.md)
  Search the configuration space for a PCI capability register.
- [GetBusDeviceFunction](iopcidevice/getbusdevicefunction.md)
  Returns the device’s bus, device, and function numbers.
- [PCI Capabilities](pci-capabilities-enum.md)
  Constants that you use to get the capabilities of the PCI device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/slot-capabilities-enum)*