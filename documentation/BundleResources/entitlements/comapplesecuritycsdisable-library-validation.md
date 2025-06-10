# Disable Library Validation Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the app loads arbitrary plug-ins or frameworks, without requiring code signing.

**Availability**:
- macOS 10.7+

#### Discussion

The [`Hardened Runtime`](https://developer.apple.com/documentation/Security/hardened-runtime) enables library validation by default. This security-hardening feature prevents a program from loading frameworks, plug-ins, or libraries unless they’re either signed by Apple or signed with the same Team ID as the main executable. The macOS dynamic linker (`dyld`) provides a detailed error message when the system prevents code from loading due to library validation. Use the [`Disable Library Validation Entitlement`](entitlements/com.apple.security.cs.disable-library-validation.md) if your program loads plug-ins that are signed by other third-party developers.

To add this entitlement to your app, first enable the Hardened Runtime capability in Xcode, and then under Runtime Exceptions, select Disable Library Validation.

> ❗ **Important**:  Because library validation is such an important security-hardening feature, Gatekeeper runs extra security checks on programs that have it disabled. If your program is blocked by Gatekeeper, check whether you’ve unnecessarily disabled library validation.

## See Also

- [Allow execution of JIT-compiled code entitlement](entitlements/com.apple.security.cs.allow-jit.md)
  A Boolean value that indicates whether the app may create writable and executable memory using the `MAP_JIT` flag.
- [Allow Unsigned Executable Memory Entitlement](entitlements/com.apple.security.cs.allow-unsigned-executable-memory.md)
  A Boolean value that indicates whether the app may create writable and executable memory without the restrictions imposed by using the `MAP_JIT` flag.
- [Allow DYLD environment variables entitlement](entitlements/com.apple.security.cs.allow-dyld-environment-variables.md)
  A Boolean value that indicates whether the app may be affected by dynamic linker environment variables, which you can use to inject code into your app’s process.
- [Disable Executable Memory Protection Entitlement](entitlements/com.apple.security.cs.disable-executable-page-protection.md)
  A Boolean value that indicates whether to disable all code signing protections while launching an app, and during its execution.
- [Debugging tool entitlement](entitlements/com.apple.security.cs.debugger.md)
  A Boolean value that indicates whether the app is a debugger and may attach to other processes or get task ports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.cs.disable-library-validation)*