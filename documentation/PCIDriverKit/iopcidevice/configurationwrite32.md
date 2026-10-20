# ConfigurationWrite32

**Framework**: PCIDriverKit  
**Kind**: method  
**Role**: Instance Method

Writes an 32-bit data value to the device’s configuration space.

**Availability**:
- DriverKit
- macOS

## Declaration

```c
void ConfigurationWrite32(uint64_t offset, uint32_t data);
```

## Parameters

- `offset`: An offset into the configuration space. This method ignores bits 0 and 1. For a list of possible offset values, see [Configuration Data Offsets](../configuration-data-offsets-enum.md).
- `data`: The data value that you want DriverKit to write to the specified location.

## See Also

### Reading and Writing Configuration Data
- [ConfigurationRead8](./configurationread8.md)
  Reads an 8-bit data value synchronously from the device’s configuration space.
- [ConfigurationRead16](./configurationread16.md)
  Reads a 16-bit data value synchronously from the device’s configuration space.
- [ConfigurationRead32](./configurationread32.md)
  Reads a 32-bit data value synchronously from the device’s configuration space.
- [ConfigurationWrite8](./configurationwrite8.md)
  Writes an 8-bit data value to the device’s configuration space.
- [ConfigurationWrite16](./configurationwrite16.md)
  Writes an 16-bit data value to the device’s configuration space.
- [Configuration Data Offsets](../configuration-data-offsets-enum.md)
  Constants for the offsets that you use to read and write configuration registers.
- [Bridge Header Offsets](../bridge-header-offsets-enum.md)
  Constants that specify offsets to distinct registers in a memory range.
- [Command Register Bits](../command-register-bits-enum.md)
  Constants that you use to access specific bits of the command register.
- [Status Register Bits](../status-register-bits-enum.md)
  Constants that you use to access specific bits of the status register.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/iopcidevice/configurationwrite32)*