# Preparing your app to work with pointer authentication

**Framework**: Security

Test your app against the arm64e architecture to ensure that it works seamlessly with enhanced security features.

#### Overview

> ❗ **Important**: Devices using the Apple A12 or later A-series processor — like the iPhone XS, iPhone XS Max, iPhone XR, and Apple TV 4K (2nd generation) — support the arm64e architecture, as do the Apple Watch Series 4 or later, and Mac and iPads with Apple silicon. To test your adoption, you need to run your app on one of these devices. You can’t test using Simulator.

The arm64e architecture introduces pointer authentication codes (PACs) to detect and guard against unexpected changes to pointers in memory. The addition of pointer authentication is transparent to most apps because the compiler manages the process. In rare cases — for example, if your app manipulates the stack directly, or if you pass pointers between C++ and Objective-C++ — you might have to adjust your code to work with PACs.

Pointer authentication works by offering a special CPU instruction to add a cryptographic signature — or PAC — to unused high-order bits of a pointer before storing the pointer. Another instruction removes and authenticates the signature after reading the pointer back from memory. Any change to the stored value between the write and the read invalidates the signature. The CPU interprets authentication failure as memory corruption and sets a high-order bit in the pointer, making the pointer invalid and causing the app to crash.

##### Build an Arm64e Binary to Adopt Pointer Authentication

You automatically adopt pointer authentication in your app when you build and deploy a binary that targets the arm64e architecture. You can do this starting in Xcode 10.1. To build an arm64e slice, go to your target’s build settings in Xcode and find the Architectures item. Click the current setting and choose Other. In the box that appears, add arm64e.

![Screenshot of Xcode showing the addition of arm64e to the Architectures item in the Build Settings pane for the iOS app target.](/images/com.apple.security/media-3682831@2x.png)

##### Recognize Pointer Authentication Failures

When pointer authentication fails, the system invalidates the failing pointer by setting a high-order bit. Subsequent use of the pointer results in a segmentation fault. The crash report contains a message that includes the value of the pointer both after and before invalidation:

```console
Exception Subtype: KERN_INVALID_ADDRESS at 0x0040000105394398 -> 0x0000000105394398 (possible pointer authentication failure)
```

Typically, the compiler adds the CPU instructions for both creating and authenticating the PAC. In the unusual case that you manage these steps yourself — for example, if you’re authoring your own compiler — and if you try to use a signed pointer without first applying the authentication instruction to remove the signature, that also triggers a segmentation fault. In this case, the presence of the signature in the high-order bits invalidates the pointer:

```console
Exception Subtype: KERN_INVALID_ADDRESS at 0x217c000105394398 -> 0x0000000105394398 (possible pointer authentication failure)
```

Be aware that other invalid memory accesses, where high-order bits are erroneously set, can also look like pointer authentication failures.

##### Update Your Code to Avoid Pointer Authentication Failures

Most code doesn’t require modification to run with pointer authentication, with the possible exception of some low-level code that relies on arm64-specific behavior. For example, a crash reporting library that examines the stack contents needs to strip the PAC out of return addresses. The Apple Clang compiler provides utilities in the `ptrauth.h` header file — like the `ptrauth_strip` macro — to help with these kinds of tasks.

Pointer authentication can also expose latent bugs in existing code. In C++, it’s incorrect to call a virtual method using a declaration that differs from its definition. In practice, such calls typically succeed in arm64, but trigger a pointer authentication failure in arm64e. You might encounter this bug when using `OS_OBJECT` types like [`dispatch_queue_t`](https://developer.apple.com/documentation/dispatch/dispatch_queue_t) and [`xpc_connection_t`](https://developer.apple.com/documentation/xpc/xpc_connection_t). You can’t pass instances of these types from C++ code to an Objective-C++ function (or vice versa) because they’re defined differently in Objective-C++ to support automatic reference counting (ARC).

More generally, the PAC calculation takes into account the pointer value, one of several keys loaded into the CPU, and an optional salt value. To prevent reuse of pointers in different contexts, the PAC calculation depends on the pointer type. Keep these rules in mind when looking for possible issues in your code:

- Return addresses are signed with a key that’s unique per process, using a salt derived from the stack pointer.
- Function pointers are signed with a key that’s fixed across all processes, allowing sharing of library code between processes.
- Virtual method table entries are signed with a key that’s shared across all apps, using a salt derived from the method signature.

###### Strengthen Return Address Protection Using Arm64ex1 with Pauthlr

The Hardware-Checked Pointer Arithmetic Slice (`arm64e.x1`) extends return address protection using PAuth_LR, a scheme that authenticates the link register (LR) around function calls and returns. As with the pointer authentication described in this article, the compiler manages PAuth_LR automatically, and adopting it requires no changes to your code or the ABI. For more information about `arm64e.x1` and its calling conventions, see [`Build settings reference`](https://developer.apple.com/documentation/xcode/build-settings-reference).

PAuth_LR is an optional, additive security measure. Existing arm64e code continues to behave as it does today. Adopting PAuth_LR closes off additional classes of return-oriented programming (ROP) attacks that reuse existing stack frames, by making forged or replayed return addresses detectable at authentication time.

Under PAuth_LR, the beginning of function uses the diversifier to sign the LR that incorporates the program counter as well as the stack pointer. As a result, unwinders and other tools that authenticate a saved LR value, rather than only reading it, can’t assume a single fixed authentication scheme. Whether or not a frame’s LR uses this PC-based scheme is based on that frame’s unwind info. Consult the frame’s compact unwind info or DWARF unwind info, whichever it uses, to determine the correct scheme.

This requirement applies only to tooling that authenticates the saved LR, most notably unwinders. Tools that only need the return address’s value, such as crash reporters that symbolicate backtraces, can continue to strip the Pointer Authentication Code (PAC) bits as before.

> ❗ **Important**: Devices with support for `arm64e.x1` include iPhones using the Apple A20 Pro or later A-series processors, Macs using the M6 chips or newer, and Apple Watch with the S11 chip or later. To test your adoption of `arm64e.x1`, you need to run your app on one of these devices. You can’t test using Simulator.

##### See Also

- [`Check for Overflow of Pointer Arithmetic`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.hardened-process.checked-allocations.enforce-checked-pointer-arithmetic-overflow).
- [`Enabling enhanced security for your app`](https://developer.apple.com/documentation/xcode/enabling-enhanced-security-for-your-app)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/preparing-your-app-to-work-with-pointer-authentication)*