# com.apple.vm.device-access

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the app captures USB devices and uses them in the guest-operating system.

**Availability**:
- macOS 10.10+

#### Discussion

The entitlement is required to use the [`IOUSBHost`](https://developer.apple.com/documentation/IOUSBHost) APIs for USB device capture.

## See Also

- [com.apple.security.hypervisor](entitlements/com.apple.security.hypervisor.md)
  A Boolean value that indicates whether the app creates and manages virtual machines.
- [com.apple.vm.hypervisor](entitlements/com.apple.vm.hypervisor.md)
  A Boolean value that indicates whether the app creates and manages virtual machines.
- [com.apple.vm.networking](entitlements/com.apple.vm.networking.md)
  A Boolean that indicates whether the app manages virtual network interfaces without escalating privileges to the root user.
- [com.apple.security.virtualization](entitlements/com.apple.security.virtualization.md)
  A Boolean value that indicates whether your app can use the Virtualization framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.vm.device-access)*