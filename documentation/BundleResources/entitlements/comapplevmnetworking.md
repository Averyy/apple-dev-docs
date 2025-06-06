# com.apple.vm.networking

**Framework**: Bundleresources  
**Kind**: typealias

A Boolean that indicates whether the app manages virtual network interfaces without escalating privileges to the root user.

**Availability**:
- macOS 10.10+

#### Discussion

The entitlement is required to use the [`vmnet`](https://developer.apple.com/documentation/vmnet) APIs.

> **Note**:  This entitlement is restricted to developers of virtualization software. To request this entitlement, contact your Apple representative.

## See Also

- [com.apple.security.hypervisor](entitlements/com.apple.security.hypervisor.md)
  A Boolean value that indicates whether the app creates and manages virtual machines.
- [com.apple.vm.hypervisor](entitlements/com.apple.vm.hypervisor.md)
  A Boolean value that indicates whether the app creates and manages virtual machines.
- [com.apple.vm.device-access](entitlements/com.apple.vm.device-access.md)
  A Boolean value that indicates whether the app captures USB devices and uses them in the guest-operating system.
- [com.apple.security.virtualization](entitlements/com.apple.security.virtualization.md)
  A Boolean value that indicates whether your app can use the Virtualization framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.vm.networking)*