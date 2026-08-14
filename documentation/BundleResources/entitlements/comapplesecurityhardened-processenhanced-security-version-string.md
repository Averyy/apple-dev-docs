# com.apple.security.hardened-process.enhanced-security-version-string

**Framework**: Bundle Resources  
**Kind**: typealias

The entitlement required for an executable to opt in to enhanced security protections.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- macOS 26.4+
- visionOS 26.4+



**Type**: string

**Default**: `*`

#### Discussion

The default value for this entitlement is the `*` wildcard.

Xcode adds this entitlement to your app or extension when you add the Enhanced Security capability. Set this value to `2` or greater to turn on guard objects automatically. To turn off guard objects, add the [`com.apple.security.hardened-process.no-guard-objects`](entitlements/com.apple.security.hardened-process.no-guard-objects.md) entitlement. For more information, see [`Enabling enhanced security for your app`](https://developer.apple.com/documentation/xcode/enabling-enhanced-security-for-your-app).

> **Note**: This entitlement requires the following entitlement: - [`com.apple.security.hardened-process`](entitlements/com.apple.security.hardened-process.md)

## See Also

- [com.apple.security.hardened-process](entitlements/com.apple.security.hardened-process.md)
  A Boolean value that indicates whether the executable opts in to additional security checks.
- [com.apple.security.hardened-process.enhanced-security-version](entitlements/com.apple.security.hardened-process.enhanced-security-version.md)
  The entitlement required for an executable to opt in to enhanced security protections.
- [com.apple.security.hardened-process.hardened-heap](entitlements/com.apple.security.hardened-process.hardened-heap.md)
  A Boolean value that indicates whether your app or extension opts in to additional hardening for heap allocations.
- [com.apple.security.hardened-process.platform-restrictions](entitlements/com.apple.security.hardened-process.platform-restrictions.md)
  An integer value that indicates the level of additional runtime security protections your app or extension opts in to.
- [com.apple.security.hardened-process.platform-restrictions-string](entitlements/com.apple.security.hardened-process.platform-restrictions-string.md)
  A string value that indicates the level of additional runtime security protections your app or extension opts in to.
- [com.apple.security.hardened-process.dyld-ro](entitlements/com.apple.security.hardened-process.dyld-ro.md)
  An entitlement that marks memory used for internal platform state as read-only.
- [com.apple.security.hardened-process.no-guard-objects](entitlements/com.apple.security.hardened-process.no-guard-objects.md)
  A Boolean value that turns off guard objects for the process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.hardened-process.enhanced-security-version-string)*