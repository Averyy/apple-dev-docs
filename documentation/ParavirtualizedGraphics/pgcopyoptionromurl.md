# PGCopyOptionROMURL()

**Framework**: Paravirtualized Graphics  
**Kind**: func

Copies the URL of the ROM image to use on the guest graphics device.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
func PGCopyOptionROMURL() -> URL
```

#### Return Value

The URL of the ROM file to load.

#### Discussion

The URL points to a local file of a flat ROM image. After loading the file, pad the data size to a power of two and fill the extra bytes with zeroes. Map the resulting data into the guest, setting the PCI ROM base address register to point to the data.

## See Also

- [var PG_PCI_DEVICE_ID: Int32](pg_pci_device_id.md)
  The PCI device identifier to use when advertising the graphics stack inside a virtual machine.
- [var PG_PCI_VENDOR_ID: Int32](pg_pci_vendor_id.md)
  The vendor identifier to use when advertising the graphics stack inside a virtual machine.
- [var PG_PCI_BAR_MMIO: Int32](pg_pci_bar_mmio.md)
  The base address register to use when advertising the graphics stack inside a virtual machine.
- [var PG_PCI_MAX_MSI_VECTORS: Int32](pg_pci_max_msi_vectors.md)
  The number of MSI vectors that you need to allocate for the graphics configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgcopyoptionromurl())*