# System Extensions

**Framework**: Bundle Resources

Extend the capabilities of macOS from user space.

## Topics

### Essentials
- [System Extension Entitlement](entitlements/com.apple.developer.system-extension.install.md)
  A Boolean value that indicates whether your app has permission to activate or deactivate system extensions.
- [System Extension Redistributable Entitlement](entitlements/com.apple.developer.system-extension.redistributable.md)
  A Boolean value that indicates whether other development teams may distribute a system extension you create.
### Endpoint Security
- [com.apple.developer.endpoint-security.client](entitlements/com.apple.developer.endpoint-security.client.md)
  The entitlement required to monitor system events for potentially malicious activity.
### Human Interface Device Drivers
- [com.apple.developer.driverkit.family.hid.device](entitlements/com.apple.developer.driverkit.family.hid.device.md)
  A Boolean value that indicates whether the driver provides a HID-related service to the system.
- [com.apple.developer.driverkit.family.hid.eventservice](entitlements/com.apple.developer.driverkit.family.hid.eventservice.md)
  A Boolean value that indicates whether the driver provides a HID-related event service to the system.
- [DriverKit Family virtual HID](entitlements/com.apple.developer.driverkit.family.hid.virtual.device.md)
  An entitlement that lets an app create and manage virtual HID devices.
- [com.apple.developer.driverkit.transport.hid](entitlements/com.apple.developer.driverkit.transport.hid.md)
  A Boolean value that indicates whether the driver communicates with human interface devices.
- [com.apple.developer.hid.virtual.device](entitlements/com.apple.developer.hid.virtual.device.md)
  A Boolean value that indicates whether the driver creates a virtual HID device.

## See Also

- [DriverKit](driverkit.md)
  Develop device drivers in macOS and iPadOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/system-extensions)*