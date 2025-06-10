# Allow DYLD environment variables entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the app may be affected by dynamic linker environment variables, which you can use to inject code into your app’s process.

**Availability**:
- macOS 10.7+

#### Discussion

If your app relies on dynamic linker variables to modify its behavior at runtime, add the `Allow DYLD environment variables entitlement` to your app. This causes the macOS dynamic linker (`dyld`) to read from environment variables that begin with `DYLD_`. See the `dyld` man page for a list of these variables.

Injecting libraries or changing search paths with this feature may still require another entitlement. For example, you also need the [`Disable Library Validation Entitlement`](entitlements/com.apple.security.cs.disable-library-validation.md) if an injected library isn’t signed with the expected team ID.

To add the entitlement to your app, first enable the Hardened Runtime capability in Xcode, and then under Runtime Exceptions, select Allow DYLD Environment Variables.

## See Also

- [Allow execution of JIT-compiled code entitlement](entitlements/com.apple.security.cs.allow-jit.md)
  A Boolean value that indicates whether the app may create writable and executable memory using the `MAP_JIT` flag.
- [Allow Unsigned Executable Memory Entitlement](entitlements/com.apple.security.cs.allow-unsigned-executable-memory.md)
  A Boolean value that indicates whether the app may create writable and executable memory without the restrictions imposed by using the `MAP_JIT` flag.
- [Disable Library Validation Entitlement](entitlements/com.apple.security.cs.disable-library-validation.md)
  A Boolean value that indicates whether the app loads arbitrary plug-ins or frameworks, without requiring code signing.
- [Disable Executable Memory Protection Entitlement](entitlements/com.apple.security.cs.disable-executable-page-protection.md)
  A Boolean value that indicates whether to disable all code signing protections while launching an app, and during its execution.
- [Debugging tool entitlement](entitlements/com.apple.security.cs.debugger.md)
  A Boolean value that indicates whether the app is a debugger and may attach to other processes or get task ports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.cs.allow-dyld-environment-variables)*