# System Extension Redistributable Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether other development teams may distribute a system extension you create.

**Availability**:
- macOS 10.15+

#### Discussion

Add this entitlement to a system extension that you create and sign using your development team credentials, but which other development teams distribute in their apps. This extension allows a distributing app to have a different team ID than the one associated with the system extension. If this entitlement isn’t present, the team ID of the app and system extension must match.

## See Also

- [System Extension Entitlement](entitlements/com.apple.developer.system-extension.install.md)
  A Boolean value that indicates whether your app has permission to activate or deactivate system extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.system-extension.redistributable)*