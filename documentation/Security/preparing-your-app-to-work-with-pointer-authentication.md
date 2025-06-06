# Preparing your app to work with pointer authentication

**Framework**: Security

Test your app against the arm64e architecture to ensure that it works seamlessly with enhanced security features.

#### Overview

The arm64e architecture introduces pointer authentication codes (PACs) to detect and guard against unexpected changes to pointers in memory. The addition of pointer authentication is transparent to most apps because the compiler manages the process. In rare cases — for example, if your app manipulates the stack directly, or if you pass pointers between C++ and Objective-C++ — you might have to adjust your code to work with PACs.

Pointer authentication works by offering a special CPU instruction to add a cryptographic signature — or PAC — to unused high-order bits of a pointer before storing the pointer. Another instruction removes and authenticates the signature after reading the pointer back from memory. Any change to the stored value between the write and the read invalidates the signature. The CPU interprets authentication failure as memory corruption and sets a high-order bit in the pointer, making the pointer invalid and causing the app to crash.

##### Build an Arm64e Binary to Adopt Pointer Authentication

You automatically adopt pointer authentication in your app when you build and deploy a binary that targets the arm64e architecture. You can do this starting in Xcode 10.1. To build an arm64e slice, go to your target’s build settings in Xcode and find the Architectures item. Click the current setting and choose Other. In the box that appears, add arm64e.

![Screenshot of Xcode showing the addition of arm64e to the Architectures item in the Build Settings pane for the iOS app target.](https://docs-assets.developer.apple.com/published/9987567eb3333abe8a1c4a841d58bc78/media-3682831%402x.png)

Devices using the Apple A12 or later A-series processor — like the iPhone XS, iPhone XS Max, iPhone XR, and Apple TV 4K (2nd generation) — support the arm64e architecture, as do the Apple Watch Series 4 or later, and Mac and iPads with Apple silicon. To test your adoption, you have to run your app on one of these devices. You can’t test using the Simulator.

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

Pointer authentication can also expose latent bugs in existing code. In C++, it’s incorrect to call a virtual method using a declaration that differs from its definition. In practice, such calls typically succeed in arm64, but trigger a pointer authentication failure in arm64e. You might encounter this bug when using `OS_OBJECT` types like [`dispatch_queue_t`](https://developer.apple.com/documentation/Dispatch/dispatch_queue_t) and [`xpc_connection_t`](https://developer.apple.com/documentation/XPC/xpc_connection_t). You can’t pass instances of these types from C++ code to an Objective-C++ function (or vice versa) because they’re defined differently in Objective-C++ to support automatic reference counting (ARC).

More generally, the PAC calculation takes into account the pointer value, one of several keys loaded into the CPU, and an optional salt value. To prevent reuse of pointers in different contexts, the PAC calculation depends on the pointer type. Keep these rules in mind when looking for possible issues in your code:

- Return addresses are signed with a key that’s unique per process, using a salt derived from the stack pointer.
- Function pointers are signed with a key that’s fixed across all processes, allowing sharing of library code between processes.
- Virtual method table entries are signed with a key that’s shared across all apps, using a salt derived from the method signature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/preparing-your-app-to-work-with-pointer-authentication)*