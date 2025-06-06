# Configuration Data Offsets

**Framework**: PCIDriverKit

Constants for the offsets that you use to read and write configuration registers.

## Topics

### Offsets
- [kIOPCIConfigurationOffsetVendorID](kiopciconfigurationoffsetvendorid.md)
  The offset to the 16-bit value that identifies the manufacturer of the device.
- [kIOPCIConfigurationOffsetDeviceID](kiopciconfigurationoffsetdeviceid.md)
  The offset to the 16-bit value that the manufacturer uses to identify the particular function.
- [kIOPCIConfigurationOffsetCommand](kiopciconfigurationoffsetcommand.md)
  The offset to the 16-bit value that defines how the device responds to commands.
- [kIOPCIConfigurationOffsetStatus](kiopciconfigurationoffsetstatus.md)
  The offset to the 16-bit value that contains the status of the device.
- [kIOPCIConfigurationOffsetRevisionID](kiopciconfigurationoffsetrevisionid.md)
  The offset to the 8-bit value that the manufacturer uses to identify the revision of the device.
- [kIOPCIConfigurationOffsetClassCode](kiopciconfigurationoffsetclasscode.md)
  The offset to the 24-bit, read-only value that identifies the generic operation of the device.
- [kIOPCIConfigurationOffsetCacheLineSize](kiopciconfigurationoffsetcachelinesize.md)
  The offset to the 8-bit value that contains legacy information about the cache line size.
- [kIOPCIConfigurationOffsetLatencyTimer](kiopciconfigurationoffsetlatencytimer.md)
  The offset to the 8-bit value that containsn legacy information for devices with a primary latency timer.
- [kIOPCIConfigurationOffsetHeaderType](kiopciconfigurationoffsetheadertype.md)
  The offset to the 8-bit value that defines the layout of the second part of the predefined header.
- [kIOPCIConfigurationOffsetBIST](kiopciconfigurationoffsetbist.md)
  The offset to the 8-bit value that controls and reports the status of the device’s built-in, self-test behavior.
- [kIOPCIConfigurationOffsetBaseAddress0](kiopciconfigurationoffsetbaseaddress0.md)
  The offset to the 32-bit value for base address 0.
- [kIOPCIConfigurationOffsetBaseAddress1](kiopciconfigurationoffsetbaseaddress1.md)
  The offset to the 32-bit value for base address 1.
- [kIOPCIConfigurationOffsetBaseAddress2](kiopciconfigurationoffsetbaseaddress2.md)
  The offset to the 32-bit value for base address 2.
- [kIOPCIConfigurationOffsetBaseAddress3](kiopciconfigurationoffsetbaseaddress3.md)
  The offset to the 32-bit value for base address 3.
- [kIOPCIConfigurationOffsetBaseAddress4](kiopciconfigurationoffsetbaseaddress4.md)
  The offset to the 32-bit value for base address 4.
- [kIOPCIConfigurationOffsetBaseAddress5](kiopciconfigurationoffsetbaseaddress5.md)
  The offset to the 32-bit value for base address 5.
- [kIOPCIConfigurationOffsetCardBusCISPtr](kiopciconfigurationoffsetcardbuscisptr.md)
  The offset to the 32-bit read-only value that describes legacy PCI functionality.
- [kIOPCIConfigurationOffsetSubSystemVendorID](kiopciconfigurationoffsetsubsystemvendorid.md)
  The offset to the 16-bit value that identifies the manufacturer of a device containing common PCI components.
- [kIOPCIConfigurationOffsetSubSystemID](kiopciconfigurationoffsetsubsystemid.md)
  The offset to the 16-bit value that identifies a specific device that uses common PCI components.
- [kIOPCIConfigurationOffsetExpansionROMBase](kiopciconfigurationoffsetexpansionrombase.md)
  The offset to the 32-bit value that contains the base address and size of the device’s expansion ROM.
- [kIOPCIConfigurationOffsetCapabilitiesPtr](kiopciconfigurationoffsetcapabilitiesptr.md)
  The offset to the 8-bit value that points to the linked list of capabilities the device implements.
- [kIOPCIConfigurationOffsetInterruptLine](kiopciconfigurationoffsetinterruptline.md)
  The offset to the 8-bit value that contains interrupt line-routing information.
- [kIOPCIConfigurationOffsetInterruptPin](kiopciconfigurationoffsetinterruptpin.md)
  The offset to the 8-bit read-only value that identifies the device’s supported interrupt messages.
- [kIOPCIConfigurationOffsetMinimumGrant](kiopciconfigurationoffsetminimumgrant.md)
  The offset to the 8-bit value that contains legacy PCI information about the minimum grant.
- [kIOPCIConfigurationOffsetMaximumLatency](kiopciconfigurationoffsetmaximumlatency.md)
  The offset to the 8-bit value that contains legacy PCI information about the maximum latency.

## See Also

- [ConfigurationRead8](iopcidevice/configurationread8.md)
  Reads an 8-bit data value synchronously from the device’s configuration space.
- [ConfigurationRead16](iopcidevice/configurationread16.md)
  Reads a 16-bit data value synchronously from the device’s configuration space.
- [ConfigurationRead32](iopcidevice/configurationread32.md)
  Reads a 32-bit data value synchronously from the device’s configuration space.
- [ConfigurationWrite8](iopcidevice/configurationwrite8.md)
  Writes an 8-bit data value to the device’s configuration space.
- [ConfigurationWrite16](iopcidevice/configurationwrite16.md)
  Writes an 16-bit data value to the device’s configuration space.
- [ConfigurationWrite32](iopcidevice/configurationwrite32.md)
  Writes an 32-bit data value to the device’s configuration space.
- [Bridge Header Offsets](bridge-header-offsets-enum.md)
  Constants that specify offsets to distinct registers in a memory range.
- [Command Register Bits](command-register-bits-enum.md)
  Constants that you use to access specific bits of the command register.
- [Status Register Bits](status-register-bits-enum.md)
  Constants that you use to access specific bits of the status register.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/configuration-data-offsets-enum)*