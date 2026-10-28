# IOPCISecondaryMatch

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A key to match PCI devices by subsystem vendor ID and device ID registers.

**Availability**:
- macOS 10.15.4+

## Details

- **Name**: `IOPCISecondaryMatch`
- **Type**: string

## Discussion

This value of this key matches the subsystem register (`0x2c`).

## See Also

### Identifying PCI Devices
- [IOPCIMatch](./iopcimatch.md)
  A key to match PCI devices by vendor and device ID registers or subsystem registers.
- [IOPCIPrimaryMatch](./iopciprimarymatch.md)
  A key to match PCI devices by vendor and device ID registers.
- [IOPCIClassMatch](./iopciclassmatch.md)
  A key to match PCI devices by class code register.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.driverkit.transport.pci/iopcisecondarymatch)*