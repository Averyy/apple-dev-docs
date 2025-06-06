# com.apple.security.hypervisor

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the app creates and manages virtual machines.

**Availability**:
- macOS 11.0+

#### Discussion

The entitlement is required to use the Hypervisor APIs in any process.

> ❗ **Important**:  If your app has a deployment target of macOS 10.15 or earlier, add the [`com.apple.vm.hypervisor`](entitlements/com.apple.vm.hypervisor.md) entitlement to your app in addition to this entitlement.

 If your app has a deployment target of macOS 10.15 or earlier, add the [`com.apple.vm.hypervisor`](entitlements/com.apple.vm.hypervisor.md) entitlement to your app in addition to this entitlement.

## See Also

- [com.apple.vm.hypervisor](entitlements/com.apple.vm.hypervisor.md)
  A Boolean value that indicates whether the app creates and manages virtual machines.
- [com.apple.vm.device-access](entitlements/com.apple.vm.device-access.md)
  A Boolean value that indicates whether the app captures USB devices and uses them in the guest-operating system.
- [com.apple.vm.networking](entitlements/com.apple.vm.networking.md)
  A Boolean that indicates whether the app manages virtual network interfaces without escalating privileges to the root user.
- [com.apple.security.virtualization](entitlements/com.apple.security.virtualization.md)
  A Boolean value that indicates whether your app can use the Virtualization framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.hypervisor)*