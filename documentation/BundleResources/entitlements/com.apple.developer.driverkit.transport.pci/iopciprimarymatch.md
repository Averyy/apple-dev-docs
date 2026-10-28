# IOPCIPrimaryMatch

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A key to match PCI devices by vendor and device ID registers.

**Availability**:
- macOS 10.15.4+

## Details

- **Name**: `IOPCIPrimaryMatch`
- **Type**: string

## Discussion

This value of this key matches the vendor and device ID (`0x00`) register.

## See Also

### Identifying PCI Devices
- [IOPCIMatch](./iopcimatch.md)
  A key to match PCI devices by vendor and device ID registers or subsystem registers.
- [IOPCISecondaryMatch](./iopcisecondarymatch.md)
  A key to match PCI devices by subsystem vendor ID and device ID registers.
- [IOPCIClassMatch](./iopciclassmatch.md)
  A key to match PCI devices by class code register.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.driverkit.transport.pci/iopciprimarymatch)*