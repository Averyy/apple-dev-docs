# PCI Capabilities

**Framework**: PCIDriverKit

Constants that you use to get the capabilities of the PCI device.

## Topics

### Capability Bits
- [kIOPCICapabilityIDOffset](kiopcicapabilityidoffset.md)
  The offset to the location of the device’s capability ID.
- [kIOPCINextCapabilityOffset](kiopcinextcapabilityoffset.md)
  The offset to the next PCI capability structure.
- [kIOPCICapabilityIDPowerManagement](kiopcicapabilityidpowermanagement.md)
  The identifier for the power management interface.
- [kIOPCICapabilityIDAGP](kiopcicapabilityidagp.md)
  The identifier for the AGP capability.
- [kIOPCICapabilityIDVitalProductData](kiopcicapabilityidvitalproductdata.md)
  The identifier for the vital product data capability.
- [kIOPCICapabilityIDSlotID](kiopcicapabilityidslotid.md)
  The identifier for the slot identification capability.
- [kIOPCICapabilityIDMSI](kiopcicapabilityidmsi.md)
  The identifier for the MSI capability.
- [kIOPCICapabilityIDCPCIHotswap](kiopcicapabilityidcpcihotswap.md)
  The identifier for the CompactPCI hot swap capability.
- [kIOPCICapabilityIDPCIX](kiopcicapabilityidpcix.md)
  The identifier for the PCI-X capability.
- [kIOPCICapabilityIDLDT](kiopcicapabilityidldt.md)
  The identifier for the HyperTransport capability.
- [kIOPCICapabilityIDVendorSpecific](kiopcicapabilityidvendorspecific.md)
  The identifier for any vendor-specific capabilities.
- [kIOPCICapabilityIDDebugPort](kiopcicapabilityiddebugport.md)
  The identifier for the debug port capability.
- [kIOPCICapabilityIDCPCIResourceControl](kiopcicapabilityidcpciresourcecontrol.md)
  The identifier for the CompactPCI central resource control capability.
- [kIOPCICapabilityIDHotplug](kiopcicapabilityidhotplug.md)
  The identifier for the PCI hot plug capability.
- [kIOPCICapabilityIDAGP8](kiopcicapabilityidagp8.md)
  The identifier for the AGP 8x capability.
- [kIOPCICapabilityIDSecure](kiopcicapabilityidsecure.md)
  The identifer for the secure device capability.
- [kIOPCICapabilityIDPCIExpress](kiopcicapabilityidpciexpress.md)
  The identifier for the PCI Express capability.
- [kIOPCICapabilityIDMSIX](kiopcicapabilityidmsix.md)
  The identifer for the MSI-X capability.
- [kIOPCICapabilityIDFPB](kiopcicapabilityidfpb.md)
  The identifier for the flattening portal bridge capability.
- [kIOPCIExpressCapabilityIDErrorReporting](kiopciexpresscapabilityiderrorreporting.md)
  The identifier for the advanced error reporting extended capability.
- [kIOPCIExpressCapabilityIDVirtualChannel](kiopciexpresscapabilityidvirtualchannel.md)
  The identifier for the virtual channel extended capability.
- [kIOPCIExpressCapabilityIDDeviceSerialNumber](kiopciexpresscapabilityiddeviceserialnumber.md)
  The identifier for the device serial number extended capability.
- [kIOPCIExpressCapabilityIDPowerBudget](kiopciexpresscapabilityidpowerbudget.md)
  The identifier for the power budgeting extended capability.
- [kIOPCIExpressCapabilityIDAccessControlServices](kiopciexpresscapabilityidaccesscontrolservices.md)
  The identifier for the access control services extended capability.
- [kIOPCIExpressCapabilityIDLatencyTolerenceReporting](kiopciexpresscapabilityidlatencytolerencereporting.md)
  The identifier for the latency tolerance reporting extended capability.
- [kIOPCIExpressCapabilityIDL1PMSubstates](kiopciexpresscapabilityidl1pmsubstates.md)
  The identifier for the L1 power management substates extended capability.
### Constants
- [kIOPCIExpressCapabilityIDAlternativeRoutingID](kiopciexpresscapabilityidalternativeroutingid.md)
- [kIOPCIExpressCapabilityIDPrecisionTimeManagement](kiopciexpresscapabilityidprecisiontimemanagement.md)

## See Also

- [FindPCICapability](iopcidevice/findpcicapability.md)
  Search the configuration space for a PCI capability register.
- [GetBusDeviceFunction](iopcidevice/getbusdevicefunction.md)
  Returns the device’s bus, device, and function numbers.
- [Slot Capabilities](slot-capabilities-enum.md)
  Constants that you use to get the slot-related capabilities of the PCI device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/pci-capabilities-enum)*