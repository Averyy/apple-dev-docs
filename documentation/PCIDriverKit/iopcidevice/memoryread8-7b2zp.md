# MemoryRead8

**Framework**: PCIDriverKit  
**Kind**: method

Reads a 8-bit value synchronously from the PCI device’s aperture at the specified memory index.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
void MemoryRead8(uint8_t memoryIndex, uint64_t offset, uint8_t * readData, IOOptionBits options);
```

## Parameters

- `memoryIndex`: The index of the memory range from which to read.
- `offset`: An offset from the beginning of the specified memory range.
- `readData`: A variable in which to store the data. If this method encounters an error when reading the data, it sets the value to -1.

## See Also

- [MemoryRead8](iopcidevice/memoryread8-1edw0.md)
  Reads a 8-bit value synchronously from the PCI device’s aperture at the specified memory index.
- [MemoryRead16](iopcidevice/memoryread16-9qkdh.md)
  Reads a 16-bit value synchronously from the PCI device’s aperture at the specified memory index.
- [MemoryRead16](iopcidevice/memoryread16-50bq8.md)
  Reads a 16-bit value synchronously from the PCI device’s aperture at the specified memory index.
- [MemoryRead32](iopcidevice/memoryread32-60hg9.md)
  Reads a 32-bit value synchronously from the PCI device’s aperture at the specified memory index.
- [MemoryRead32](iopcidevice/memoryread32-84jap.md)
  Reads a 32-bit value synchronously from the PCI device’s aperture at the specified memory index.
- [MemoryRead64](iopcidevice/memoryread64-9ntrf.md)
  Reads a 64-bit value synchronously from the PCI device’s aperture at the specified memory index.
- [MemoryRead64](iopcidevice/memoryread64-37uob.md)
  Reads a 64-bit value synchronously from the PCI device’s aperture at the specified memory index.
- [MemoryWrite8](iopcidevice/memorywrite8-1uey6.md)
  Writes an 8-bit value to the PCI device’s aperture at the specified memory index.
- [MemoryWrite8](iopcidevice/memorywrite8-fzh6.md)
  Writes an 8-bit value to the PCI device’s aperture at the specified memory index.
- [MemoryWrite16](iopcidevice/memorywrite16-8k6ch.md)
  Writes an 16-bit value to the PCI device’s aperture at the specified memory index.
- [MemoryWrite16](iopcidevice/memorywrite16-534yk.md)
  Writes an 16-bit value to the PCI device’s aperture at the specified memory index.
- [MemoryWrite32](iopcidevice/memorywrite32-4pmh.md)
  Writes an 32-bit value to the PCI device’s aperture at the specified memory index.
- [MemoryWrite32](iopcidevice/memorywrite32-ow7r.md)
  Writes an 32-bit value to the PCI device’s aperture at the specified memory index.
- [MemoryWrite64](iopcidevice/memorywrite64-8qyob.md)
  Writes an 64-bit value to the PCI device’s aperture at the specified memory index.
- [MemoryWrite64](iopcidevice/memorywrite64-nvpu.md)
  Writes an 64-bit value to the PCI device’s aperture at the specified memory index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pcidriverkit/iopcidevice/memoryread8-7b2zp)*