# com.apple.security.hardened-process.checked-allocations.no-tagged-receive

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether to prevent receiving tagged memory from other processes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Details

- **Name**: `com.apple.security.hardened-process.checked-allocations.no-tagged-receive` (Hardened Process - Prevent Receiving Tagged Memory)
- **Type**: boolean

## Discussion

This behavior provides additional protection for processes that run arbitrary code, such as interpreters and JITs.

To enable this entitlement for your app or extension in Xcode, first add the Enhanced Security capability. Then, under Memory Safety, select Prevent Receiving Tagged Memory.

For more information, see [Enabling enhanced security for your app](../../Xcode/enabling-enhanced-security-for-your-app.md).

> **Note**: This entitlement requires the following entitlements:
>
> - [`com.apple.security.hardened-process`](./com.apple.security.hardened-process.md)
> - [`com.apple.security.hardened-process.enhanced-security-version-string`](./com.apple.security.hardened-process.enhanced-security-version-string.md)
> - [`com.apple.security.hardened-process.checked-allocations`](./com.apple.security.hardened-process.checked-allocations.md)

## See Also

### Hardware memory tagging
- [com.apple.security.hardened-process.checked-allocations](./com.apple.security.hardened-process.checked-allocations.md)
  A Boolean value that enables tagging of pointers and memory allocations.
- [com.apple.security.hardened-process.checked-allocations.soft-mode](./com.apple.security.hardened-process.checked-allocations.soft-mode.md)
  A Boolean value that indicates whether to log memory-tagging faults as a simulated crash, instead of terminating the process.
- [com.apple.security.hardened-process.checked-allocations.enable-pure-data](./com.apple.security.hardened-process.checked-allocations.enable-pure-data.md)
  A Boolean value that indicates whether to tag memory that contains only data.
- [Check for Overflow of Pointer Arithmetic](./com.apple.security.hardened-process.checked-allocations.enforce-checked-pointer-arithmetic-overflow.md)
  A Boolean value that enables checking pointers for arithmetic overflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.hardened-process.checked-allocations.no-tagged-receive)*