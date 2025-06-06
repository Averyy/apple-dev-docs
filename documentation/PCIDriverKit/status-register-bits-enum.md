# Status Register Bits

**Framework**: PCIDriverKit

Constants that you use to access specific bits of the status register.

## Topics

### Registers
- [kIOPCIStatusInterrupt](kiopcistatusinterrupt.md)
  The bit that contains the interrupt status.
- [kIOPCIStatusCapabilities](kiopcistatuscapabilities.md)
  The bit that indicates the presence of an extended capability list item.
- [kIOPCIStatusPCI66](kiopcistatuspci66.md)
  The bit that indicates the device is capable of 66 MHz operation.
- [kIOPCIStatusUDF](kiopcistatusudf.md)
  The bit that indicates the status of UDF support.
- [kIOPCIStatusFastBack2Back](kiopcistatusfastback2back.md)
  The bit that indicates whether the device is capable of fast back-to-back transactions.
- [kIOPCIStatusTargetAbortCapable](kiopcistatustargetabortcapable.md)
  The bit that indicates whether a function completed a posted or non-posted request as a completer abort error.
- [kIOPCIStatusTargetAbortActive](kiopcistatustargetabortactive.md)
  The bit that indicates whether a requester received a completion with a completer abort completion status.
- [kIOPCIStatusMasterAbortActive](kiopcistatusmasterabortactive.md)
  The bit that indicates whether a requester received a completion with an unsupported request completion status
- [kIOPCIStatusSERRActive](kiopcistatusserractive.md)
  The bit that indicates whether a function sent a fatal or nonfatal error message and set the SERR enable bit in the command register.
- [kIOPCIStatusParityErrActive](kiopcistatusparityerractive.md)
  The bit that indicates whether a function received a poisoned transaction-layer packet.
- [kIOPCIStatusDevSel0](kiopcistatusdevsel0.md)
  The DEVSEL timing status is set to 0.
- [kIOPCIStatusDevSel1](kiopcistatusdevsel1.md)
  The DEVSEL timing status is set to 1.
- [kIOPCIStatusDevSel2](kiopcistatusdevsel2.md)
  The DEVSEL timing status is set to 2.
- [kIOPCIStatusDevSel3](kiopcistatusdevsel3.md)
  The DEVSEL timing status is set to 3.
### Constants
- [kIOPCIStatusLeadAbortActive](kiopcistatusleadabortactive.md)

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
- [Configuration Data Offsets](configuration-data-offsets-enum.md)
  Constants for the offsets that you use to read and write configuration registers.
- [Bridge Header Offsets](bridge-header-offsets-enum.md)
  Constants that specify offsets to distinct registers in a memory range.
- [Command Register Bits](command-register-bits-enum.md)
  Constants that you use to access specific bits of the command register.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/status-register-bits-enum)*