# Command Register Bits

**Framework**: PCIDriverKit

Constants that you use to access specific bits of the command register.

## Topics

### Bits
- [kIOPCICommandIOSpace](kiopcicommandiospace.md)
  The bit that indicates whether the device allows access to I/O space.
- [kIOPCICommandMemorySpace](kiopcicommandmemoryspace.md)
  The bit that indicates whether the device allows access to memory space.
- [kIOPCICommandBusMaster](kiopcicommandbusmaster.md)
  The bit that controls the ability to issue or forward memory and I/O requests.
- [kIOPCICommandSpecialCycles](kiopcicommandspecialcycles.md)
  The bit that enables the legacy special cycle feature.
- [kIOPCICommandMemWrInvalidate](kiopcicommandmemwrinvalidate.md)
  The bit that enables legacy memory writing and invalidation.
- [kIOPCICommandPaletteSnoop](kiopcicommandpalettesnoop.md)
  The bit that enables the legacy palette snooping feature.
- [kIOPCICommandParityError](kiopcicommandparityerror.md)
  The bit that controls the logging of poisoned transaction-layer packets.
- [kIOPCICommandAddressStepping](kiopcicommandaddressstepping.md)
  The bit that controls the legacy address stepping and wait cycle feature.
- [kIOPCICommandSERR](kiopcicommandserr.md)
  The bit that enables the upstream reporting of fatal and non-fatal errors.
- [kIOPCICommandFastBack2Back](kiopcicommandfastback2back.md)
  The bit that enables legacy fast back-to-back transactions.
- [kIOPCICommandInterruptDisable](kiopcicommandinterruptdisable.md)
  The bit that prevents the generation of INTx emulation interrupts.
- [kIOPCICommandBusLead](kiopcicommandbuslead.md)

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
- [Status Register Bits](status-register-bits-enum.md)
  Constants that you use to access specific bits of the status register.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/command-register-bits-enum)*