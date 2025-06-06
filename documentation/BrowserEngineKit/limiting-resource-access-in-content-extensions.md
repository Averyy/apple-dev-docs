# Limiting resource access in web content extensions

**Framework**: Browserenginekit

Reduce the impact of vulnerabilities in web content extensions by limiting privileges.

#### Overview

Web content extensions parse resources and run code from unknown sources. An attacker might supply malformed resources to mount an attack on your browser app and gain access to privileged operating system resources, and the data of the person using your browser app.

Mitigate the impact of any successful attack by reducing your content extension’s privilege before processing resources from remote websites.

#### Restrict the Sandbox for Your Web Content Extension

When the operating system launches your web content extension, the extension has permissive access to a variety of services and resources that you use to initialize the extension. Once your extension is ready to begin loading web content, call the [`applyRestrictedSandbox(revision:)`](restrictedsandboxappliable/applyrestrictedsandbox(revision:).md) method on your extension’s main object:

```swift
class MyWebContentExtension: WebContentExtension {

  func loadContent(from source: URL) {
	// Prepare the extension.
	self.applyRestrictedSandbox(revision: .revision1)
	// Start loading remote content.
  }
}
```

#### Restrict Resource Access

Once your web content extension is locked down, it’s unable to do any of the following.

Create, change, or set:

- Create new processes
- Create new work queues
- Change its working directory
- Duplicate file descriptors
- Set kernel debug tracing strings

Obtain or access:

- Obtain the full path to filesystem objects
- Get its process identifier (PID)
- Get the kernel tick frequency
- Get its own mach task
- Get special mach host ports
- Get or set special mach task ports
- Get information about the host system and its scheduler
- Get the version of the I/O Kit server
- Access shared dyld caches
- Access XPC services

Install or use:

- Use Objective-C branch prediction support
- Install POSIX signal handlers

Write or allocate:

- Write to file descriptors
- Allocate portions of the process address space

Design your web content extension so that it doesn’t need to do any of the above.

> **Note**:  The rendering extension and networking extension both conform to [`RestrictedSandboxAppliable`](restrictedsandboxappliable.md) and you can apply a restricted sandbox to them. Revision 1 of the restricted sandbox doesn’t apply any additional restrictions to those extensions.

#### Restrict Access to System Notifications

Limit the possibility for malicious code that runs in your web-content extension to post notifications using the system’s notification service by adding the `com.apple.developer.web-browser-engine.restrict.notifyd` entitlement with the value `true`. When it has this entitlement, your web-content extension can’t post notifications by connecting directly to the system’s notification daemon.

## See Also

- [Accessing files in browser extensions](accessing-files-in-browser-extensions.md)
  Grant extensions access to files from within your browser app.
- [Attributing memory to a content extension](attributing-memory-to-a-content-extension.md)
  Adhere to operating-system limits on GPU memory use.
- [protocol RestrictedSandboxAppliable](restrictedsandboxappliable.md)
  A protocol that browser extensions implement to opt into a more restricted sandbox.
- [enum RestrictedSandboxRevision](restrictedsandboxrevision.md)
  Revisions to the restricted sandbox rules.


---

*[View on Apple Developer](https://developer.apple.com/documentation/BrowserEngineKit/limiting-resource-access-in-content-extensions)*