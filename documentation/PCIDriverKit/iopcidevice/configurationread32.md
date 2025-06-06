# ConfigurationRead32

**Framework**: PCIDriverKit  
**Kind**: method

Reads a 32-bit data value synchronously from the device’s configuration space.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
void ConfigurationRead32(uint64_t offset, uint32_t * readData);
```

## Parameters

- `offset`: An offset into the configuration space. This method ignores bits 0 and 1. For a list of possible offset values, see  .
- `readData`: A variable that stores the 32-bit data value. If the method encounters an error, it sets the value to -1.

## See Also

- [ConfigurationRead8](iopcidevice/configurationread8.md)
  Reads an 8-bit data value synchronously from the device’s configuration space.
- [ConfigurationRead16](iopcidevice/configurationread16.md)
  Reads a 16-bit data value synchronously from the device’s configuration space.
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
- [Status Register Bits](status-register-bits-enum.md)
  Constants that you use to access specific bits of the status register.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/iopcidevice/configurationread32)*