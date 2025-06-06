# ConfigurationWrite8

**Framework**: PCIDriverKit  
**Kind**: method

Writes an 8-bit data value to the device’s configuration space.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
void ConfigurationWrite8(uint64_t offset, uint8_t data);
```

## Parameters

- `offset`: An offset into the configuration space. This method ignores bits 0 and 1. For a list of possible offset values, see  .
- `data`: The data value that you want DriverKit to write to the specified location.

## See Also

- [ConfigurationRead8](iopcidevice/configurationread8.md)
  Reads an 8-bit data value synchronously from the device’s configuration space.
- [ConfigurationRead16](iopcidevice/configurationread16.md)
  Reads a 16-bit data value synchronously from the device’s configuration space.
- [ConfigurationRead32](iopcidevice/configurationread32.md)
  Reads a 32-bit data value synchronously from the device’s configuration space.
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
- [Status Register Bits](status-register-bits-enum.md)
  Constants that you use to access specific bits of the status register.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/iopcidevice/configurationwrite8)*