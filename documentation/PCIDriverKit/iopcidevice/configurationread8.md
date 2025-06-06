# ConfigurationRead8

**Framework**: PCIDriverKit  
**Kind**: method

Reads an 8-bit data value synchronously from the device’s configuration space.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
void ConfigurationRead8(uint64_t offset, uint8_t * readData);
```

#### Discussion

- offset: An offset into the configuration space. This method ignores bits 0 and 1. For a list of possible offset values, see [`Configuration Data Offsets`](configuration-data-offsets-enum.md). - readData: A variable that stores the 8-bit data value. If the method encounters an error, it sets the value to -1.

## See Also

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
- [Status Register Bits](status-register-bits-enum.md)
  Constants that you use to access specific bits of the status register.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/iopcidevice/configurationread8)*