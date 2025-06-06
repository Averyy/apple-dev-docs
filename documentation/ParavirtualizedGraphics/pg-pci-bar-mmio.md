# PG_PCI_BAR_MMIO

**Framework**: Paravirtualized Graphics  
**Kind**: var

The base address register to use when advertising the graphics stack inside a virtual machine.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
var PG_PCI_BAR_MMIO: Int32 { get }
```

#### Discussion

Specify the following characteristics for the memory that this base address register references:

- Allocate 16 kilobytes of memory.
- Place MSI interrupt vectors between offsets `0x0000` and `0x0FFF` of this memory block.
- Place MMIO mapped registers starting at offset `0x1000`.

When you see a read or write access to this memory region, call [`mmioRead(atOffset:)`](pgdevice/mmioread(atoffset:).md) or [`mmioWrite(atOffset:value:)`](pgdevice/mmiowrite(atoffset:value:).md) on the host device. The framework aligns reads and writes to addresses that are multiples of `4` bytes with a length of `4` bytes.

## See Also

- [var PG_PCI_DEVICE_ID: Int32](pg_pci_device_id.md)
  The PCI device identifier to use when advertising the graphics stack inside a virtual machine.
- [var PG_PCI_VENDOR_ID: Int32](pg_pci_vendor_id.md)
  The vendor identifier to use when advertising the graphics stack inside a virtual machine.
- [var PG_PCI_MAX_MSI_VECTORS: Int32](pg_pci_max_msi_vectors.md)
  The number of MSI vectors that you need to allocate for the graphics configuration.
- [func PGCopyOptionROMURL() -> URL](pgcopyoptionromurl().md)
  Copies the URL of the ROM image to use on the guest graphics device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pg_pci_bar_mmio)*