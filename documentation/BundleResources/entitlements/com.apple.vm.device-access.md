# com.apple.vm.device-access

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether the app captures USB devices and uses them in the guest-operating system.

**Availability**:
- macOS 10.10+

## Details

- **Name**: `com.apple.vm.device-access`
- **Type**: boolean



**Default**: `NO`

## Discussion

The entitlement is required to use the [IOUSBHost](../../IOUSBHost/IOUSBHost.md) APIs for USB device capture.

## See Also

### Hypervisor
- [com.apple.security.hypervisor](./com.apple.security.hypervisor.md)
  A Boolean value that indicates whether the app creates and manages virtual machines.
- [com.apple.vm.hypervisor](./com.apple.vm.hypervisor.md)
  A Boolean value that indicates whether the app creates and manages virtual machines.
- [com.apple.vm.networking](./com.apple.vm.networking.md)
  A Boolean that indicates whether the app manages virtual network interfaces without escalating privileges to the root user.
- [com.apple.security.virtualization](./com.apple.security.virtualization.md)
  A Boolean value that indicates whether your app can use the Virtualization framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.vm.device-access)*