# Allow execution of JIT-compiled code entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the app may create writable and executable memory using the `MAP_JIT` flag.

**Availability**:
- macOS 10.7+

#### Discussion

You can create memory that’s both writable and executable by passing the `MAP_JIT` flag to the `mmap()` system function. The Hardened Runtime disallows this by default, because it creates a security risk. However, some apps and system frameworks rely on this functionality, typically for performance reasons. Examples include:

- The fast-path of the [`JavaScriptCore`](https://developer.apple.com/documentation/JavaScriptCore) framework
- Certain Python frameworks
- Perl-compatible regular expressions (PCRE)
- An app that creates a dynamically-compiled, proprietary macro language

Without the `Allow execution of JIT-compiled code entitlement`, frameworks that rely on just-in-time (JIT) compilation may fall back to an interpreter. Other code using JIT compilation may crash or behave in unexpected ways.

Digital rights management (DRM) solutions that currently use unsigned executable memory should instead change to using the `MAP_JIT` flag and the entitlement.

To add the entitlement to your app, first enable the Hardened Runtime capability in Xcode, and then under Runtime Exceptions, select Allow Execution of JIT-compiled Code.

## See Also

- [Allow Unsigned Executable Memory Entitlement](entitlements/com.apple.security.cs.allow-unsigned-executable-memory.md)
  A Boolean value that indicates whether the app may create writable and executable memory without the restrictions imposed by using the `MAP_JIT` flag.
- [Allow DYLD environment variables entitlement](entitlements/com.apple.security.cs.allow-dyld-environment-variables.md)
  A Boolean value that indicates whether the app may be affected by dynamic linker environment variables, which you can use to inject code into your app’s process.
- [Disable Library Validation Entitlement](entitlements/com.apple.security.cs.disable-library-validation.md)
  A Boolean value that indicates whether the app loads arbitrary plug-ins or frameworks, without requiring code signing.
- [Disable Executable Memory Protection Entitlement](entitlements/com.apple.security.cs.disable-executable-page-protection.md)
  A Boolean value that indicates whether to disable all code signing protections while launching an app, and during its execution.
- [Debugging tool entitlement](entitlements/com.apple.security.cs.debugger.md)
  A Boolean value that indicates whether the app is a debugger and may attach to other processes or get task ports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.cs.allow-jit)*