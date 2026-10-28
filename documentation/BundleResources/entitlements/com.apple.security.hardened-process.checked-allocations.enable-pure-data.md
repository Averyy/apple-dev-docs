# com.apple.security.hardened-process.checked-allocations.enable-pure-data

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether to tag memory that contains only data.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Details

- **Name**: `com.apple.security.hardened-process.checked-allocations.enable-pure-data` (Hardened Process - Enable Memory Tag Pure Data)
- **Type**: boolean

## Discussion

Adding an additional class of allocations for data improves security at the cost of memory and performance overhead.

To enable this entitlement for your app or extension in Xcode, first add the Enhanced Security capability. Then, under Memory Safety, select Memory Tag Pure Data.

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
- [com.apple.security.hardened-process.checked-allocations.no-tagged-receive](./com.apple.security.hardened-process.checked-allocations.no-tagged-receive.md)
  A Boolean value that indicates whether to prevent receiving tagged memory from other processes.
- [Check for Overflow of Pointer Arithmetic](./com.apple.security.hardened-process.checked-allocations.enforce-checked-pointer-arithmetic-overflow.md)
  A Boolean value that enables checking pointers for arithmetic overflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.hardened-process.checked-allocations.enable-pure-data)*