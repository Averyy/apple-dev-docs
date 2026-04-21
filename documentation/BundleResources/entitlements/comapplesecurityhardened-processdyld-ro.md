# com.apple.security.hardened-process.dyld-ro

**Framework**: Bundle Resources  
**Kind**: typealias

An entitlement that marks memory used for internal platform state as read-only.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+



**Type**: boolean

**Default**: `true`

#### Overview

When you add this entitlement to your app or extension with the value `true`, the kernel and dynamic loader ensure that all memory regions that the system uses to manage internal state are read-only.

> ⚠️ **Warning**:  Your app or extension crashes if it tries to write to the read-only memory regions; for example, if your code writes to memory in `const` data segments.

Xcode adds this entitlement to your app or extension when you add the Enhanced Security capability. For more information, see [`Enabling enhanced security for your app`](https://developer.apple.com/documentation/Xcode/enabling-enhanced-security-for-your-app).

> **Note**: This entitlement requires the following entitlements: - [`com.apple.security.hardened-process`](entitlements/com.apple.security.hardened-process.md)
- [`com.apple.security.hardened-process.enhanced-security-version-string`](entitlements/com.apple.security.hardened-process.enhanced-security-version-string.md)

## See Also

- [com.apple.security.hardened-process](entitlements/com.apple.security.hardened-process.md)
  A Boolean value that indicates whether the executable opts in to additional security checks.
- [com.apple.security.hardened-process.enhanced-security-version](entitlements/com.apple.security.hardened-process.enhanced-security-version.md)
  The entitlement required for an executable to opt in to enhanced security protections.
- [com.apple.security.hardened-process.enhanced-security-version-string](entitlements/com.apple.security.hardened-process.enhanced-security-version-string.md)
  The entitlement required for an executable to opt in to enhanced security protections.
- [com.apple.security.hardened-process.hardened-heap](entitlements/com.apple.security.hardened-process.hardened-heap.md)
  A Boolean value that indicates whether the process opts in to type-aware memory allocations.
- [com.apple.security.hardened-process.platform-restrictions](entitlements/com.apple.security.hardened-process.platform-restrictions.md)
  An integer value that indicates the level of additional runtime security protections your app or extension opts in to.
- [com.apple.security.hardened-process.platform-restrictions-string](entitlements/com.apple.security.hardened-process.platform-restrictions-string.md)
  A string value that indicates the level of additional runtime security protections your app or extension opts in to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.hardened-process.dyld-ro)*