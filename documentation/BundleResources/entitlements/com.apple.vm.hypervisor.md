# com.apple.vm.hypervisor

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether the app creates and manages virtual machines.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: For apps with a deployment target of macOS 11 and later, use [`com.apple.security.hypervisor`](./com.apple.security.hypervisor.md) instead. For deployment targets earlier than macOS 11, add both that and the [`com.apple.vm.hypervisor`](./com.apple.vm.hypervisor.md) entitlement to your app.

## Details

- **Name**: `com.apple.vm.hypervisor`
- **Type**: boolean

#### Discussion

The entitlement is required to use the Hypervisor APIs in a sandboxed process.

## See Also

### Hypervisor
- [com.apple.security.hypervisor](./com.apple.security.hypervisor.md)
  A Boolean value that indicates whether the app creates and manages virtual machines.
- [com.apple.vm.device-access](./com.apple.vm.device-access.md)
  A Boolean value that indicates whether the app captures USB devices and uses them in the guest-operating system.
- [com.apple.vm.networking](./com.apple.vm.networking.md)
  A Boolean that indicates whether the app manages virtual network interfaces without escalating privileges to the root user.
- [com.apple.security.virtualization](./com.apple.security.virtualization.md)
  A Boolean value that indicates whether your app can use the Virtualization framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.vm.hypervisor)*