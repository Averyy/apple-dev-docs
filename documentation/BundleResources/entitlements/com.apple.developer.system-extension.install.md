# System Extension Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether your app has permission to activate or deactivate system extensions.

**Availability**:
- macOS 10.15+

## Details

- **Name**: `com.apple.developer.system-extension.install` (System Extension)
- **Type**: boolean

#### Discussion

To add this entitlement to your app, enable the System Extension capability in Xcode. Add this entitlement for all system extension types, including DriverKit extensions.

## See Also

### Essentials
- [System Extension Redistributable Entitlement](./com.apple.developer.system-extension.redistributable.md)
  A Boolean value that indicates whether other development teams may distribute a system extension you create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.system-extension.install)*