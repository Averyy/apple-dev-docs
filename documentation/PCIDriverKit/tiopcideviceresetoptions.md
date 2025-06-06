# tIOPCIDeviceResetOptions

**Framework**: PCIDriverKit  
**Kind**: enum

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
typedef enum tIOPCIDeviceResetOptions : unsigned int { ... } tIOPCIDeviceResetOptions;
```

#### Overview

```None
        any attached client drivers. Devices with reset-initiated personality changes should use this option.

        This option causes the reset function to initiate the asynchronous termination process, but not block on its completion.
```

## Topics

### Enumeration Cases
- [kIOPCIDeviceResetOptionNone](tiopcideviceresetoptions/kiopcideviceresetoptionnone.md)
- [kIOPCIDeviceResetOptionTerminate](tiopcideviceresetoptions/kiopcideviceresetoptionterminate.md)

## See Also

- [Anonymous](anonymous-enum.md)
- [tIOPCIAccessOptions](tiopciaccessoptions.md)
- [tIOPCIDeviceResetTypes](tiopcideviceresettypes.md)
- [tIOPCILinkSpeed](tiopcilinkspeed.md)
- [IOPCIBARType](iopcibartype.md)
- [IOPCILinkSpeed](iopcilinkspeed.md)
- [IOPCIMemoryRange](iopcimemoryrange.md)
- [IOPCISaveDeviceStateOptions](iopcisavedevicestateoptions.md)
- [tIOPCIAccessOptions](tiopciaccessoptions.md)
- [tIOPCIDeviceResetTypes](tiopcideviceresettypes.md)
- [tIOPCILinkControlASPMBits](tiopcilinkcontrolaspmbits.md)
- [tIOPCILinkSpeed](tiopcilinkspeed.md)
- [Interrupt Types](interrupt-types-enum.md)
  Interrupt types that the device supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/tiopcideviceresetoptions)*