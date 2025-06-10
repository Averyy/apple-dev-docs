# Protecting code compiled just in time

**Framework**: BrowserEngineKit

Toggle memory between being writable and executable.

#### Overview

A just-in-time (JIT) compiler poses unique security challenges. To prepare the compiled code, the web content extension must be able to write to a region of memory. Then, to run the code, the extension must be able to execute the content of that memory. But, an attacker can use memory that is both writable and executable to run arbitrary code in your process.

The operating system uses hardware memory management to enforce that a page of memory allocated by your process is either writable, or executable, but not simultaneously both (W^X).

To toggle the writable or executable status of a memory page, your web content extension calls [`be_memory_inline_jit_restrict_rwx_to_rx_with_witness`](https://developer.apple.com/documentation/BrowserEngineCore/be_memory_inline_jit_restrict_rwx_to_rx_with_witness), and [`be_memory_inline_jit_restrict_rwx_to_rw_with_witness`](https://developer.apple.com/documentation/BrowserEngineCore/be_memory_inline_jit_restrict_rwx_to_rw_with_witness). You must call these functions only in certain restricted ways that are outlined below, to protect your process from possible malicious misuse.

#### Add Jit Entitlements

Add the following entitlements to your web content extension’s target, setting their values to `true`:

- [`Extended Virtual Addressing Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.kernel.extended-virtual-addressing)
- `com.apple.developer.cs.allow-jit`

> **Note**:  If you use `pthread_jit_write_with_callback_np()` to toggle JIT write protections for a memory region instead of `be_memory_inline_jit_restrict_rwx_to_rx_with_witness()`, add both the `com.apple.developer.cs.allow-jit` and `com.apple.security.cs.jit-write-allowlist` entitlements, each with the value `true`. For more information, see [`Porting just-in-time compilers to Apple silicon`](https://developer.apple.com/documentation/Apple-Silicon/porting-just-in-time-compilers-to-apple-silicon).

#### Adopt Pointer Authentication

When your app targets the `arm64e` instruction set, the [`be_memory_inline_jit_restrict_rwx_to_rw_with_witness`](https://developer.apple.com/documentation/BrowserEngineCore/be_memory_inline_jit_restrict_rwx_to_rw_with_witness) function inserts a cryptographically signed pointer authentication code (PAC) into the pointer to your JIT memory. The operating system authenticates the PAC when your extension process jumps to the JIT-compiled code after you call `be_memory_inline_jit_restrict_rwx_to_rx_with_witness()`, and only runs the code if the PAC is still valid. Otherwise, it stops your extension process.

Pointer authentication is only available with the `arm64e` instruction set. You can compile your browser app as a universal binary that includes both `arm64` and `arm64e`, but on devices that only support `arm64`, the W^X toggle functions don’t use PAC. For more information on building for `arm64e`, see “Build for pointer authentication” in [`Managing the browser extension life cycle`](managing-the-browser-extension-lifecycle.md).

> ❗ **Important**:  The iPhone Simulator doesn’t run `arm64e` code. You need to test your JIT code on an iPhone, not in the Simulator.

Additionally, your JIT compiler needs to emit `arm64e` code that uses PAC-protected pointers. Your browser engine needs to adopt PAC for any pointer that influences control flow in your interpreter code.

For more information on pointer authentication, see doc:improving-control-flow-integrity-with-pointer-authentication.

#### Inline Your Memory Protection Toggles

Your calls to `be_memory_inline_jit_restrict_rwx_to_rw_with_witness()` and its counterpart must be inlined into the critical section for your extension’s JIT compilation code, so they don’t provide an attacker with a general way to run arbitrary code while your JIT region is writable. An attacker might use a general PAC-signing mechanism to write and run instructions anywhere in your process’s memory.

> ❗ **Important**:  The Swift attribute `@inlinable`, described in [`Attributes`](https://developer.apple.comhttps://docs.swift.org/swift-book/documentation/the-swift-programming-language/attributes/), indicates that the compiler  inline a function, but doesn’t guarantee that it does. `@inlinable` isn’t suitable for inlining calls to the memory protection toggle functions for JIT compilation.

#### Avoid Spilling Variables to the Stack

Variables that your JIT code accesses between calls to the memory toggle functions must be in registers, or in heap memory that you access using PAC-protected pointers. Don’t rely on loop indexes or other variables that are in stack memory, because an attacker might gain control of the stack to change the behavior of your JIT compiler.

If necessary, disassemble your extension’s binary to inspect the JIT critical section and ensure that important variables aren’t stored on the stack. To disassemble the binary, use the command-line tool `llvm-objdump`. For example, if your JIT compiler is in a function called `runJavascript`, run this command in Terminal:

```None
% xcrun llvm-objdump --disassemble-symbols=runJavascript --macho /path/to/executable
```

> **Note**:  You can also use the path to the object file in your Xcode project’s derived data file that contains the relevant function, instead of your extension’s executable file.

## See Also

- [Improving control flow integrity with pointer authentication](../Apple-Silicon/improving-control-flow-integrity-with-pointer-authentication.md)
  Increase confidence that your code uses pointers correctly.
- [var BE_JIT_WRITE_PROTECT_TAG: Int { get }](../BrowserEngineCore/BE_JIT_WRITE_PROTECT_TAG.md)
  A discriminator value the system uses to generate pointer authentication codes for just-in-time compilation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/protecting-code-compiled-just-in-time)*