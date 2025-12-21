# Enable Soft Mode for Memory Tagging

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether to log memory-tagging faults as a simulated crash, instead of terminating the process.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

#### Discussion

Xcode adds this entitlement to your app or extension by default when you add the Enable Hardware Memory Tagging entitlement. To enable this entitlement for your app or extension in Xcode, first add the Enhanced Security capability. Then, under Memory Safety, select Enable Soft Mode for Memory Tagging.

For more information, see [`Enabling enhanced security for your app`](https://developer.apple.com/documentation/Xcode/enabling-enhanced-security-for-your-app).

## See Also

- [Enable Hardware Memory Tagging](entitlements/com.apple.security.hardened-process.checked-allocations.md)
  A Boolean value that enables tagging of pointers and memory allocations.
- [Memory Tag Pure Data](entitlements/com.apple.security.hardened-process.checked-allocations.enable-pure-data.md)
  A Boolean value that indicates whether to tag memory that contains only data.
- [Prevent Receiving Tagged Memory](entitlements/com.apple.security.hardened-process.checked-allocations.no-tagged-receive.md)
  A Boolean value that indicates whether to prevent receiving tagged memory from other processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.hardened-process.checked-allocations.soft-mode)*