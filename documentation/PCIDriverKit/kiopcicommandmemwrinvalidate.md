# kIOPCICommandMemWrInvalidate

**Framework**: PCIDriverKit  
**Kind**: case

The bit that enables legacy memory writing and invalidation.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
kIOPCICommandMemWrInvalidate
```

## See Also

- [kIOPCICommandIOSpace](kiopcicommandiospace.md)
  The bit that indicates whether the device allows access to I/O space.
- [kIOPCICommandMemorySpace](kiopcicommandmemoryspace.md)
  The bit that indicates whether the device allows access to memory space.
- [kIOPCICommandBusMaster](kiopcicommandbusmaster.md)
  The bit that controls the ability to issue or forward memory and I/O requests.
- [kIOPCICommandSpecialCycles](kiopcicommandspecialcycles.md)
  The bit that enables the legacy special cycle feature.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/kiopcicommandmemwrinvalidate)*