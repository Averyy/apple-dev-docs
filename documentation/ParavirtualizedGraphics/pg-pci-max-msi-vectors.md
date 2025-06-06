# PG_PCI_MAX_MSI_VECTORS

**Framework**: Paravirtualized Graphics  
**Kind**: var

The number of MSI vectors that you need to allocate for the graphics configuration.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
var PG_PCI_MAX_MSI_VECTORS: Int32 { get }
```

## See Also

- [var PG_PCI_DEVICE_ID: Int32](pg_pci_device_id.md)
  The PCI device identifier to use when advertising the graphics stack inside a virtual machine.
- [var PG_PCI_VENDOR_ID: Int32](pg_pci_vendor_id.md)
  The vendor identifier to use when advertising the graphics stack inside a virtual machine.
- [var PG_PCI_BAR_MMIO: Int32](pg_pci_bar_mmio.md)
  The base address register to use when advertising the graphics stack inside a virtual machine.
- [func PGCopyOptionROMURL() -> URL](pgcopyoptionromurl().md)
  Copies the URL of the ROM image to use on the guest graphics device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pg_pci_max_msi_vectors)*