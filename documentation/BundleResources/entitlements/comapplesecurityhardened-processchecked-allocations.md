# Enable Hardware Memory Tagging

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that enables tagging of pointers and memory allocations.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

#### Discussion

To enable this entitlement for your app or extension in Xcode, first add the Enhanced Security capability. Then, under Memory Safety, select Enable Hardware Memory Tagging.

If your code uses pointer arithmetic, mask out bits 56–59 of pointers, which contain the tag.

If your code stores data in those bits of pointers, store than data elsewhere to avoid interfering with the tag.

For more information, see [`Enabling enhanced security for your app`](https://developer.apple.com/documentation/Xcode/enabling-enhanced-security-for-your-app).

## See Also

- [Enable Soft Mode for Memory Tagging](entitlements/com.apple.security.hardened-process.checked-allocations.soft-mode.md)
  A Boolean value that indicates whether to log memory-tagging faults as a simulated crash, instead of terminating the process.
- [Memory Tag Pure Data](entitlements/com.apple.security.hardened-process.checked-allocations.enable-pure-data.md)
  A Boolean value that indicates whether to tag memory that contains only data.
- [Prevent Receiving Tagged Memory](entitlements/com.apple.security.hardened-process.checked-allocations.no-tagged-receive.md)
  A Boolean value that indicates whether to prevent receiving tagged memory from other processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.hardened-process.checked-allocations)*