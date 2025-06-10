# Debugging tool entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the app is a debugger and may attach to other processes or get task ports.

**Availability**:
- macOS 10.7+

#### Discussion

Apps with the `Debugging tool entitlement` can call `task_for_pid()` to retrieve a valid task port for unsigned and third-party apps with the `Get task allow` entitlement set to `true`. However, even with the debugging tool entitlement, a debugger can’t get the task ports of processes that don’t have the `Get task allow` entitlement, and that are therefore protected by System Integrity Protection. See the man page for `taskgated(8)` for more information about getting task ports.

Xcode automatically adds the `Get task allow` entitlement to apps that you build for debugging, while removing the entitlement before App Store submission. This enables Xcode itself to attach to and debug your app during development.

When a non-root user runs an app with the debugging tool entitlement, the system presents an authorization dialog asking for a system administrator’s credentials. If authorization succeeds, the debugger receives a 10-hour session before authorization expires.

To add this entitlement to your app, first enable the Hardened Runtime capability in Xcode, and then under Runtime Exceptions, select Debugging Tool.

## See Also

- [Allow execution of JIT-compiled code entitlement](entitlements/com.apple.security.cs.allow-jit.md)
  A Boolean value that indicates whether the app may create writable and executable memory using the `MAP_JIT` flag.
- [Allow Unsigned Executable Memory Entitlement](entitlements/com.apple.security.cs.allow-unsigned-executable-memory.md)
  A Boolean value that indicates whether the app may create writable and executable memory without the restrictions imposed by using the `MAP_JIT` flag.
- [Allow DYLD environment variables entitlement](entitlements/com.apple.security.cs.allow-dyld-environment-variables.md)
  A Boolean value that indicates whether the app may be affected by dynamic linker environment variables, which you can use to inject code into your app’s process.
- [Disable Library Validation Entitlement](entitlements/com.apple.security.cs.disable-library-validation.md)
  A Boolean value that indicates whether the app loads arbitrary plug-ins or frameworks, without requiring code signing.
- [Disable Executable Memory Protection Entitlement](entitlements/com.apple.security.cs.disable-executable-page-protection.md)
  A Boolean value that indicates whether to disable all code signing protections while launching an app, and during its execution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.cs.debugger)*