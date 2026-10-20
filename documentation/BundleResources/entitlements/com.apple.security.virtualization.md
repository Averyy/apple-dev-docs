# com.apple.security.virtualization

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether your app can use the Virtualization framework.

**Availability**:
- macOS 11.0+

## Details

- **Name**: `com.apple.security.virtualization` (Virtualization)
- **Type**: boolean

#### Discussion

You can read the `VZVirtualMachine` property [`isSupported`](../../Virtualization/vzmachardwaremodel/issupported.md) to check for the availability of virtualization on the system. Calling [`validate()`](../../Virtualization/vzvirtualmachineconfiguration/validate%28%29.md) checks for the availability of the entitlement the framework requires to run guest OSes.

## See Also

### Hypervisor
- [com.apple.security.hypervisor](./com.apple.security.hypervisor.md)
  A Boolean value that indicates whether the app creates and manages virtual machines.
- [com.apple.vm.hypervisor](./com.apple.vm.hypervisor.md)
  A Boolean value that indicates whether the app creates and manages virtual machines.
- [com.apple.vm.device-access](./com.apple.vm.device-access.md)
  A Boolean value that indicates whether the app captures USB devices and uses them in the guest-operating system.
- [com.apple.vm.networking](./com.apple.vm.networking.md)
  A Boolean that indicates whether the app manages virtual network interfaces without escalating privileges to the root user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.virtualization)*