# Memory Tag Pure Data

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether to tag memory that contains only data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

#### Discussion

Adding an additional class of allocations for data improves security at the cost of memory and performance overhead.

To enable this entitlement for your app or extension in Xcode, first add the Enhanced Security capability. Then, under Memory Safety, select Memory Tag Pure Data.

For more information, see [`Enabling enhanced security for your app`](https://developer.apple.com/documentation/Xcode/enabling-enhanced-security-for-your-app).

## See Also

- [Enable Hardware Memory Tagging](entitlements/com.apple.security.hardened-process.checked-allocations.md)
  A Boolean value that enables tagging of pointers and memory allocations.
- [Enable Soft Mode for Memory Tagging](entitlements/com.apple.security.hardened-process.checked-allocations.soft-mode.md)
  A Boolean value that indicates whether to log memory-tagging faults as a simulated crash, instead of terminating the process.
- [Prevent Receiving Tagged Memory](entitlements/com.apple.security.hardened-process.checked-allocations.no-tagged-receive.md)
  A Boolean value that indicates whether to prevent receiving tagged memory from other processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.hardened-process.checked-allocations.enable-pure-data)*