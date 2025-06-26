# Security entitlements

**Framework**: Bundle Resources

Key-value pairs that grant an executable access to secure resources, or enable hardening checks.

## Topics

### Automation
- [Apple Events Entitlement](entitlements/com.apple.security.automation.apple-events.md)
  A Boolean value that indicates whether the app may prompt the user for permission to send Apple events to other apps.
### Networking
- [com.apple.security.network.server](entitlements/com.apple.security.network.server.md)
  A Boolean value indicating whether your app may listen for incoming network connections.
- [com.apple.security.network.client](entitlements/com.apple.security.network.client.md)
  A Boolean value indicating whether your app may open outgoing network connections.
- [App Attest Environment](entitlements/com.apple.developer.devicecheck.appattest-environment.md)
  The environment for an app that uses the App Attest service to validate itself.
### Device access
- [Audio Input Entitlement](entitlements/com.apple.security.device.audio-input.md)
  A Boolean value that indicates whether the app may record audio using the built-in microphone and access audio input using Core Audio.
- [Camera entitlement](entitlements/com.apple.security.device.camera.md)
  A Boolean value that indicates whether the app may interact with the built-in and external cameras, and capture movies and still images.
- [com.apple.security.device.microphone](entitlements/com.apple.security.device.microphone.md)
  A Boolean value that indicates whether the app may use the microphone.
- [com.apple.security.device.usb](entitlements/com.apple.security.device.usb.md)
  A Boolean value indicating whether your app may interact with USB devices.
- [com.apple.security.print](entitlements/com.apple.security.print.md)
  A Boolean value indicating whether your app may print a document.
- [com.apple.security.device.bluetooth](entitlements/com.apple.security.device.bluetooth.md)
  A Boolean value indicating whether your app may interact with Bluetooth devices.
- [com.apple.security.smartcard](entitlements/com.apple.security.smartcard.md)
  A Boolean that indicates whether your app has access to smart card slots and smart cards.
### Personal information
- [Address book entitlement](entitlements/com.apple.security.personal-information.addressbook.md)
  A Boolean value that indicates whether the app may have read-write access to contacts in the user’s address book.
- [Location entitlement](entitlements/com.apple.security.personal-information.location.md)
  A Boolean value that indicates whether the app may access location information from Location Services.
- [Calendars entitlement](entitlements/com.apple.security.personal-information.calendars.md)
  A Boolean value that indicates whether the app may have read-write access to the user’s calendar.
- [Photos Library Entitlement](entitlements/com.apple.security.personal-information.photos-library.md)
  A Boolean value that indicates whether the app has read-write access to the user’s Photos library.
### Files and media
- [App Sandbox Entitlement](entitlements/com.apple.security.app-sandbox.md)
  A Boolean value that indicates whether the app may use access control technology to contain damage to the system and user data if an app is compromised.
- [com.apple.security.files.user-selected.read-only](entitlements/com.apple.security.files.user-selected.read-only.md)
  A Boolean value that indicates whether the app may have read-only access to files the user has selected using an Open or Save dialog.
- [com.apple.security.files.user-selected.read-write](entitlements/com.apple.security.files.user-selected.read-write.md)
  A Boolean value that indicates whether the app may have read-write access to files the user has selected using an Open or Save dialog.
- [com.apple.security.files.downloads.read-only](entitlements/com.apple.security.files.downloads.read-only.md)
  A Boolean value that indicates whether the app may have read-only access to the Downloads folder.
- [com.apple.security.files.downloads.read-write](entitlements/com.apple.security.files.downloads.read-write.md)
  A Boolean value that indicates whether the app may have read-write access to the Downloads folder.
- [Privileged File Operations](entitlements/com.apple.developer.security.privileged-file-operations.md)
  An entitlement that permits apps to create symbolic links, replace files, and set file attributes.
- [com.apple.security.assets.pictures.read-only](entitlements/com.apple.security.assets.pictures.read-only.md)
  A Boolean value that indicates whether the app may have read-only access to the Pictures folder.
- [com.apple.security.assets.pictures.read-write](entitlements/com.apple.security.assets.pictures.read-write.md)
  A Boolean value that indicates whether the app may have read-write access to the Pictures folder.
- [com.apple.security.assets.music.read-only](entitlements/com.apple.security.assets.music.read-only.md)
  A Boolean value that indicates whether the app may have read-only access to the Music folder.
- [com.apple.security.assets.music.read-write](entitlements/com.apple.security.assets.music.read-write.md)
  A Boolean value that indicates whether the app may have read-write access to the Music folder.
- [com.apple.security.assets.movies.read-only](entitlements/com.apple.security.assets.movies.read-only.md)
  A Boolean value that indicates whether the app may have read-only access to the Movies folder.
- [com.apple.security.assets.movies.read-write](entitlements/com.apple.security.assets.movies.read-write.md)
  A Boolean value that indicates whether the app may have read-write access to the Movies folder.
- [All files entitlement](entitlements/com.apple.security.files.all.md)
  A Boolean value that indicates whether the app may have access to all files.
- [Data Protection Entitlement](entitlements/com.apple.developer.default-data-protection.md)
  The level of data protection for sensitive user data when an app accesses it on a device.
### Hardened runtime
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
- [Debugging tool entitlement](entitlements/com.apple.security.cs.debugger.md)
  A Boolean value that indicates whether the app is a debugger and may attach to other processes or get task ports.
### Hardened process
- [Hardened Process](entitlements/com.apple.security.hardened-process.md)
  A Boolean value that indicates whether the executable opts in to additional security checks.
- [Enhanced Security](entitlements/com.apple.security.hardened-process.enhanced-security-version.md)
  The entitlement required for an executable to opt in to enhanced security protections.
- [Hardened Heap](entitlements/com.apple.security.hardened-process.hardened-heap.md)
  A Boolean value that indicates whether the process opts in to type-aware memory allocations.
- [Additional Runtime Platform Restrictions](entitlements/com.apple.security.hardened-process.platform-restrictions.md)
  An integer value that indicates the level of additional runtime security protections your app or extension opts in to.
- [Enable Read-Only Platform Memory](entitlements/com.apple.security.hardened-process.dyld-ro.md)
  An entitlement that marks memory used for internal platform state as read-only.
### Application groups
- [App Groups Entitlement](entitlements/com.apple.security.application-groups.md)
  A list of identifiers specifying the groups your app belongs to.
- [Keychain Access Groups Entitlement](entitlements/keychain-access-groups.md)
  The identifiers for the keychain groups that the app may share items with.

## See Also

- [App Sandbox](../Security/app-sandbox.md)
  Restrict access to system resources and user data in macOS apps to contain damage if an app becomes compromised.
- [Hardened Runtime](../Security/hardened-runtime.md)
  Manage security protections and resource access for your macOS apps.
- [Enabling enhanced security for your app](../Xcode/enabling-enhanced-security-for-your-app.md)
  Detect out-of-bounds memory access, use of freed memory, and other potential vulnerabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/security-entitlements)*