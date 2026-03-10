# com.apple.security.hardened-process.enhanced-security-version

**Framework**: Bundle Resources  
**Kind**: typealias

The entitlement required for an executable to opt in to enhanced security protections.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+



**Type**: string

**Default**: `1`

#### Discussion

Set this entitlement’s value to `1` to adopt the current version of enhanced security protections in your app or extension. For more information, see [`Enabling enhanced security for your app`](https://developer.apple.com/documentation/Xcode/enabling-enhanced-security-for-your-app).

## See Also

- [com.apple.security.hardened-process](entitlements/com.apple.security.hardened-process.md)
  A Boolean value that indicates whether the executable opts in to additional security checks.
- [com.apple.security.hardened-process.enhanced-security-version-string](entitlements/com.apple.security.hardened-process.enhanced-security-version-string.md)
  The entitlement required for an executable to opt in to enhanced security protections.
- [com.apple.security.hardened-process.hardened-heap](entitlements/com.apple.security.hardened-process.hardened-heap.md)
  A Boolean value that indicates whether the process opts in to type-aware memory allocations.
- [com.apple.security.hardened-process.platform-restrictions](entitlements/com.apple.security.hardened-process.platform-restrictions.md)
  An integer value that indicates the level of additional runtime security protections your app or extension opts in to.
- [com.apple.security.hardened-process.platform-restrictions-string](entitlements/com.apple.security.hardened-process.platform-restrictions-string.md)
  A string value that indicates the level of additional runtime security protections your app or extension opts in to.
- [com.apple.security.hardened-process.dyld-ro](entitlements/com.apple.security.hardened-process.dyld-ro.md)
  An entitlement that marks memory used for internal platform state as read-only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.hardened-process.enhanced-security-version)*