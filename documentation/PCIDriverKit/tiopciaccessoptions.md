# tIOPCIAccessOptions

**Framework**: PCIDriverKit  
**Kind**: enum

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
typedef enum tIOPCIAccessOptions : unsigned int { ... } tIOPCIAccessOptions;
```

#### Overview

Options passed to memory space accessor functions

```None
        and host software is permitted to offload the access to a DMA engine in order to free the CPU for other work to
        optimize overall system performance. Use of this hint may increase the latency of the memory space accessor function.
```

```None
        if such a mapping is available. Care must be taken to ensure correct ordering of PCIe accesses (i.e., with memory barriers):
        1. Ordering between WC accesses to different addresses is not guaranteed.
        2. Ordering between WC and non-WC accesses is not guaranteed.
        3. To guarantee a write has been issued to the endpoint, a barrier is required.
```

## Topics

### Enumeration Cases
- [kIOPCIAccessLatencyTolerantHint](tiopciaccessoptions/kiopciaccesslatencytoleranthint.md)
- [kIOPCIAccessWriteCombining](tiopciaccessoptions/kiopciaccesswritecombining.md)

## See Also

- [Anonymous](anonymous-enum.md)
- [tIOPCIDeviceResetOptions](tiopcideviceresetoptions.md)
- [tIOPCIDeviceResetTypes](tiopcideviceresettypes.md)
- [tIOPCILinkSpeed](tiopcilinkspeed.md)
- [IOPCIBARType](iopcibartype.md)
- [IOPCILinkSpeed](iopcilinkspeed.md)
- [IOPCIMemoryRange](iopcimemoryrange.md)
- [IOPCISaveDeviceStateOptions](iopcisavedevicestateoptions.md)
- [tIOPCIDeviceResetOptions](tiopcideviceresetoptions.md)
- [tIOPCIDeviceResetTypes](tiopcideviceresettypes.md)
- [tIOPCILinkControlASPMBits](tiopcilinkcontrolaspmbits.md)
- [tIOPCILinkSpeed](tiopcilinkspeed.md)
- [Interrupt Types](interrupt-types-enum.md)
  Interrupt types that the device supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/tiopciaccessoptions)*