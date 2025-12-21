# Prevent Receiving Tagged Memory

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether to prevent receiving tagged memory from other processes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

#### Discussion

This behavior provides additional protection for processes that run arbitrary code, such as interpreters and JITs.

To enable this entitlement for your app or extension in Xcode, first add the Enhanced Security capability. Then, under Memory Safety, select Prevent Receiving Tagged Memory.

For more information, see [`Enabling enhanced security for your app`](https://developer.apple.com/documentation/Xcode/enabling-enhanced-security-for-your-app).

## See Also

- [Enable Hardware Memory Tagging](entitlements/com.apple.security.hardened-process.checked-allocations.md)
  A Boolean value that enables tagging of pointers and memory allocations.
- [Enable Soft Mode for Memory Tagging](entitlements/com.apple.security.hardened-process.checked-allocations.soft-mode.md)
  A Boolean value that indicates whether to log memory-tagging faults as a simulated crash, instead of terminating the process.
- [Memory Tag Pure Data](entitlements/com.apple.security.hardened-process.checked-allocations.enable-pure-data.md)
  A Boolean value that indicates whether to tag memory that contains only data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.hardened-process.checked-allocations.no-tagged-receive)*