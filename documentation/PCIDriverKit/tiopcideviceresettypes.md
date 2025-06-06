# tIOPCIDeviceResetTypes

**Framework**: PCIDriverKit  
**Kind**: enum

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
typedef enum tIOPCIDeviceResetTypes : unsigned int { ... } tIOPCIDeviceResetTypes;
```

#### Overview

```None
        This will issue a hot reset from its upstream bridge by setting the secondary bus reset bit in the bridge's control
        register.
```

```None
        specific function exists.
```

```None
        specific function exists. Upon completion, the device is unusable until the caller requests reset with type
        kIOPCIDeviceResetTypeWarmResetEnable.

        This type facilitates the generation of a cold reset, i.e. by removing power before using kIOPCIDeviceResetTypeWarmResetDisable
        and re-applying it before using kIOPCIDeviceResetTypeWarmResetEnable.
```

```None
        (e.g. deassert PERST#). See kIOPCIDeviceResetTypeWarmResetDisable for more details.
```

## Topics

### Enumeration Cases
- [kIOPCIDeviceResetTypeFunctionReset](tiopcideviceresettypes/kiopcideviceresettypefunctionreset.md)
- [kIOPCIDeviceResetTypeHotReset](tiopcideviceresettypes/kiopcideviceresettypehotreset.md)
- [kIOPCIDeviceResetTypeWarmReset](tiopcideviceresettypes/kiopcideviceresettypewarmreset.md)
- [kIOPCIDeviceResetTypeWarmResetDisable](tiopcideviceresettypes/kiopcideviceresettypewarmresetdisable.md)
- [kIOPCIDeviceResetTypeWarmResetEnable](tiopcideviceresettypes/kiopcideviceresettypewarmresetenable.md)

## See Also

- [Anonymous](anonymous-enum.md)
- [tIOPCIAccessOptions](tiopciaccessoptions.md)
- [tIOPCIDeviceResetOptions](tiopcideviceresetoptions.md)
- [tIOPCILinkSpeed](tiopcilinkspeed.md)
- [IOPCIBARType](iopcibartype.md)
- [IOPCILinkSpeed](iopcilinkspeed.md)
- [IOPCIMemoryRange](iopcimemoryrange.md)
- [IOPCISaveDeviceStateOptions](iopcisavedevicestateoptions.md)
- [tIOPCIAccessOptions](tiopciaccessoptions.md)
- [tIOPCIDeviceResetOptions](tiopcideviceresetoptions.md)
- [tIOPCILinkControlASPMBits](tiopcilinkcontrolaspmbits.md)
- [tIOPCILinkSpeed](tiopcilinkspeed.md)
- [Interrupt Types](interrupt-types-enum.md)
  Interrupt types that the device supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/tiopcideviceresettypes)*