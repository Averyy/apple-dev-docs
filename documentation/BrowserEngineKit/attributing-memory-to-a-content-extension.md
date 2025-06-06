# Attributing memory to a content extension

**Framework**: BrowserEngineKit

Adhere to operating-system limits on GPU memory use.

#### Overview

A web browser’s GPU extension is limited to a small total memory allocation. To allocate large amounts of memory in a GPU extension on behalf of a content extension, attribute the memory to that content extension.

The GPU and the content extension both need specific memory transfer entitlements to participate in memory attribution. In the content extension, you create a token that identifies the extension to the kernel. Pass the token to the GPU using your interprocess communication (IPC) channel. Then, in the GPU extension, use the token to assign ownership of the memory region to the content process.

#### Use the Correct Entitlements

To participate in memory attribution, your content extension needs both the web-browser content extension entitlement `com.apple.developer.web-browser-engine.webcontent` and the `com.apple.developer.memory.transfer_accept` entitlement.

Your GPU extension needs both the `com.apple.developer.web-browser-engine.rendering` and `com.apple.developer.memory.transfer_send` entitlements.

Set the value for each of these entitlements to a string that matches the bundle ID of your browser app.

For more information about the entitlements web browser extensions use, see [`Designing your browser architecture`](designing-your-browser-architecture.md).

#### Create a Task Identity Token

Your content extension creates a task identity token that you pass to the GPU extension using your IPC protocol, for example, with [`XPC`](https://developer.apple.com/documentation/XPC). The task identity token is an unforgeable value that the operating system uses to identify the process to which it attributes memory in the GPU extension.

To create a task identity token:

```c
task_id_token_t identityToken;
mach_port_t port = mach_task_self();
kern_result_t result = task_create_identity_token(port, &identityToken);

if (result == KERN_SUCCESS) {
  // Send identityToken to the GPU extension.
} else {
  // Handle the error.
}
```

#### Attribute Memory to the Content Extension

Receive the task identity token in the GPU extension and use it to attribute memory to the content extension.

To attribute an [`IOSurfaceRef`](https://developer.apple.com/documentation/IOSurface/IOSurfaceRef) to a content extension, call `IOSurfaceSetOwnershipIdentity`:

```c
IOSurfaceRef surface = /* Create an IOSurface. */;
task_id_token_t identityToken = /* Receive the token using your IPC channel. */;
kern_return_t result = IOSurfaceSetOwnershipIdentity(surface,
	identityToken,
	kIOSurfaceMemoryLedgerTagGraphics,
	0);

if (result != KERN_SUCCESS) {
  // Handle the error.
}
```

To attribute a `MTLResource` to a content extension, send it a `setOwnerWithIdentity:` message:

```objc
MTLResource *resource = /* Create a resource. */;
task_id_token_t identityToken = /* Receive the token using your IPC channel. */;
kern_return_t result = [resource setOwnerWithIdentity: identityToken];

if (result != KERN_SUCCESS) {
  // Handle the error.
}
```

#### Free the Memory When the Content Extension Finishes

When the content extension exits, whether normally or due to an error, free the memory that’s attributed to it in your GPU extension.

If you use `libxpc` to implement your IPC protocol, use the connection’s invalidation handler to detect when the content extension exits.

## See Also

- [Limiting resource access in web content extensions](limiting-resource-access-in-content-extensions.md)
  Reduce the impact of vulnerabilities in web content extensions by limiting privileges.
- [Accessing files in browser extensions](accessing-files-in-browser-extensions.md)
  Grant extensions access to files from within your browser app.
- [protocol RestrictedSandboxAppliable](restrictedsandboxappliable.md)
  A protocol that browser extensions implement to opt into a more restricted sandbox.
- [enum RestrictedSandboxRevision](restrictedsandboxrevision.md)
  Revisions to the restricted sandbox rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/attributing-memory-to-a-content-extension)*