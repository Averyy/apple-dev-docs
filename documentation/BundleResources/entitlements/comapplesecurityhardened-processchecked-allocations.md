# com.apple.security.hardened-process.checked-allocations

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that enables tagging of pointers and memory allocations.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+



**Type**: boolean

#### Discussion

To enable this entitlement for your app or extension in Xcode, first add the Enhanced Security capability. Then, under Memory Safety, select Enable Hardware Memory Tagging.

If your code uses pointer arithmetic, mask out bits 56–59 of pointers, which contain the tag.

If your code stores data in those bits of pointers, store than data elsewhere to avoid interfering with the tag.

For more information, see [`Enabling enhanced security for your app`](https://developer.apple.com/documentation/xcode/enabling-enhanced-security-for-your-app).

Hardware memory tagging and other memory-related features have dependencies on specific keys. If you are manually adding entitlements, be sure to add all necessary keys.

> **Note**: This entitlement requires the following entitlements: - [`com.apple.security.hardened-process`](entitlements/com.apple.security.hardened-process.md)
- [`com.apple.security.hardened-process.enhanced-security-version-string`](entitlements/com.apple.security.hardened-process.enhanced-security-version-string.md)

## See Also

- [com.apple.security.hardened-process.checked-allocations.soft-mode](entitlements/com.apple.security.hardened-process.checked-allocations.soft-mode.md)
  A Boolean value that indicates whether to log memory-tagging faults as a simulated crash, instead of terminating the process.
- [com.apple.security.hardened-process.checked-allocations.enable-pure-data](entitlements/com.apple.security.hardened-process.checked-allocations.enable-pure-data.md)
  A Boolean value that indicates whether to tag memory that contains only data.
- [com.apple.security.hardened-process.checked-allocations.no-tagged-receive](entitlements/com.apple.security.hardened-process.checked-allocations.no-tagged-receive.md)
  A Boolean value that indicates whether to prevent receiving tagged memory from other processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.hardened-process.checked-allocations)*