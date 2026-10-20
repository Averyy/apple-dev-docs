# com.apple.security.hardened-process.no-guard-objects

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that turns off guard objects for the process.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- visionOS 27.0+

## Details

- **Name**: `com.apple.security.hardened-process.no-guard-objects`
- **Type**: boolean



**Default**: `false`

#### Discussion

The system turns on guard objects automatically when you set [`com.apple.security.hardened-process.enhanced-security-version-string`](./com.apple.security.hardened-process.enhanced-security-version-string.md) to `2` or greater.

Guard objects can increase memory usage or decrease execution speed, depending on your app’s workload. If guard objects cause an unacceptable impact, set this entitlement’s value to `true` to turn off guard objects.

For more information, see [Enabling enhanced security for your app](../../Xcode/enabling-enhanced-security-for-your-app.md).

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
- [com.apple.security.hardened-process.platform-restrictions-string](./com.apple.security.hardened-process.platform-restrictions-string.md)
  A string value that indicates the level of additional runtime security protections your app or extension opts in to.
- [com.apple.security.hardened-process.dyld-ro](./com.apple.security.hardened-process.dyld-ro.md)
  An entitlement that marks memory used for internal platform state as read-only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.hardened-process.no-guard-objects)*