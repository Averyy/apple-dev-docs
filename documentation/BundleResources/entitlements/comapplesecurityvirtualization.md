# com.apple.security.virtualization

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether your app can use the Virtualization framework.

**Availability**:
- macOS 11.0+

#### Discussion

You can read the `VZVirtualMachine` property [`isSupported`](https://developer.apple.com/documentation/Virtualization/VZMacHardwareModel/isSupported) to check for the availability of virtualization on the system. Calling [`validate()`](https://developer.apple.com/documentation/Virtualization/VZVirtualMachineConfiguration/validate()) checks for the availability of the entitlement the framework requires to run guest OSes.

## See Also

- [com.apple.security.hypervisor](entitlements/com.apple.security.hypervisor.md)
  A Boolean value that indicates whether the app creates and manages virtual machines.
- [com.apple.vm.hypervisor](entitlements/com.apple.vm.hypervisor.md)
  A Boolean value that indicates whether the app creates and manages virtual machines.
- [com.apple.vm.device-access](entitlements/com.apple.vm.device-access.md)
  A Boolean value that indicates whether the app captures USB devices and uses them in the guest-operating system.
- [com.apple.vm.networking](entitlements/com.apple.vm.networking.md)
  A Boolean that indicates whether the app manages virtual network interfaces without escalating privileges to the root user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.virtualization)*