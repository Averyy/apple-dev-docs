# IOPCIClassMatch

**Framework**: Bundle Resources  
**Kind**: typealias

A key to match PCI devices by class code register.

**Availability**:
- macOS 10.15.4+

#### Discussion

This value of this key matches the class code register (`0x08`). The default mask for this register is `0xffffff00`.

## See Also

- [IOPCIMatch](entitlements/com.apple.developer.driverkit.transport.pci/iopcimatch.md)
  A key to match PCI devices by vendor and device ID registers or subsystem registers.
- [IOPCIPrimaryMatch](entitlements/com.apple.developer.driverkit.transport.pci/iopciprimarymatch.md)
  A key to match PCI devices by vendor and device ID registers.
- [IOPCISecondaryMatch](entitlements/com.apple.developer.driverkit.transport.pci/iopcisecondarymatch.md)
  A key to match PCI devices by subsystem vendor ID and device ID registers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.driverkit.transport.pci/iopciclassmatch)*