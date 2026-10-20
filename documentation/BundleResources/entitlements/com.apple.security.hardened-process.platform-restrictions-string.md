# com.apple.security.hardened-process.platform-restrictions-string

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A string value that indicates the level of additional runtime security protections your app or extension opts in to.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- macOS 26.4+
- visionOS 26.4+

## Details

- **Name**: `com.apple.security.hardened-process.platform-restrictions-string` (Hardened Process - Additional Runtime Platform Restrictions)
- **Type**: string



**Default**: `2`

#### Discussion

Add this entitlement with the value “2” to your app or extension to instruct the system to protect against particular attacks that target the dynamic loader and Mach messaging.

Xcode adds this entitlement to your app or extension when you add the Enhanced Security capability. For more information, see [Enabling enhanced security for your app](../../Xcode/enabling-enhanced-security-for-your-app.md).

> **Note**: This entitlement requires the following entitlements:
>
> - [`com.apple.security.hardened-process`](./com.apple.security.hardened-process.md)
> - [`com.apple.security.hardened-process.enhanced-security-version-string`](./com.apple.security.hardened-process.enhanced-security-version-string.md)

## See Also

### Hardened process
- [com.apple.security.hardened-process](./com.apple.security.hardened-process.md)
  A Boolean value that indicates whether the executable opts in to additional security checks.
- [com.apple.security.hardened-process.enhanced-security-version](./com.apple.security.hardened-process.enhanced-security-version.md)
  The entitlement required for an executable to opt in to enhanced security protections.
- [com.apple.security.hardened-process.enhanced-security-version-string](./com.apple.security.hardened-process.enhanced-security-version-string.md)
  The entitlement required for an executable to opt in to enhanced security protections.
- [com.apple.security.hardened-process.hardened-heap](./com.apple.security.hardened-process.hardened-heap.md)
  A Boolean value that indicates whether your app or extension opts in to additional hardening for heap allocations.
- [com.apple.security.hardened-process.platform-restrictions](./com.apple.security.hardened-process.platform-restrictions.md)
  An integer value that indicates the level of additional runtime security protections your app or extension opts in to.
- [com.apple.security.hardened-process.dyld-ro](./com.apple.security.hardened-process.dyld-ro.md)
  An entitlement that marks memory used for internal platform state as read-only.
- [com.apple.security.hardened-process.no-guard-objects](./com.apple.security.hardened-process.no-guard-objects.md)
  A Boolean value that turns off guard objects for the process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.hardened-process.platform-restrictions-string)*