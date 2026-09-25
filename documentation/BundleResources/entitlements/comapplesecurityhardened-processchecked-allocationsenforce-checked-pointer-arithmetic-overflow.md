# Check for Overflow of Pointer Arithmetic

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that enables checking pointers for arithmetic overflow.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- watchOS 27.0+



**Type**: boolean

#### Discussion

To enable this entitlement for your app or extension in Xcode, navigate to the Signing and Capabilities editor for your Xcode target and add the Enhanced Security capability. Then, under Memory Safety, select Enable Hardware Memory Tagging and  Enforce Checking for Overflow Pointer Arithmetic.

Next, in your app’s build settings, in the Security section, add a new setting for `Hardware-Checked Pointer Arithmetic Slice` and set its value to  to `Yes`. You can also enable this capability through your app’s Project Build Settings in the Enhanced Security pane.

> **Note**: The Xcode build system surfaces a build configuration warning if the `com.apple.security.hardened-process.checked-allocations.enforce-checked-pointer-arithmetic-overflow` entitlement is present but a target dependency for the project doesn’t enable `HARDWARE_CHECKED_POINTER_ARITHMETIC_SLICE`.

For more information, see [`Enabling enhanced security for your app`](https://developer.apple.com/documentation/xcode/enabling-enhanced-security-for-your-app).

Hardware pointer arithmetic checking and other memory-related features have dependencies on specific keys. If you are manually adding entitlements, be sure to add all necessary keys.

> **Note**: This entitlement requires the following entitlements: - [`com.apple.security.hardened-process`](entitlements/com.apple.security.hardened-process.md)
- [`com.apple.security.hardened-process.enhanced-security-version-string`](entitlements/com.apple.security.hardened-process.enhanced-security-version-string.md)

## See Also

- [com.apple.security.hardened-process.checked-allocations](entitlements/com.apple.security.hardened-process.checked-allocations.md)
  A Boolean value that enables tagging of pointers and memory allocations.
- [com.apple.security.hardened-process.checked-allocations.soft-mode](entitlements/com.apple.security.hardened-process.checked-allocations.soft-mode.md)
  A Boolean value that indicates whether to log memory-tagging faults as a simulated crash, instead of terminating the process.
- [com.apple.security.hardened-process.checked-allocations.enable-pure-data](entitlements/com.apple.security.hardened-process.checked-allocations.enable-pure-data.md)
  A Boolean value that indicates whether to tag memory that contains only data.
- [com.apple.security.hardened-process.checked-allocations.no-tagged-receive](entitlements/com.apple.security.hardened-process.checked-allocations.no-tagged-receive.md)
  A Boolean value that indicates whether to prevent receiving tagged memory from other processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.hardened-process.checked-allocations.enforce-checked-pointer-arithmetic-overflow)*