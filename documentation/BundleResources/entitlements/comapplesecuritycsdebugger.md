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

- [App Sandbox](../Security/app-sandbox.md)
  Restrict access to system resources and user data in macOS apps to contain damage if an app becomes compromised.
- [App Sandbox Entitlement](entitlements/com.apple.security.app-sandbox.md)
  A Boolean value that indicates whether the app may use access control technology to contain damage to the system and user data if an app is compromised.
- [com.apple.security.network.server](entitlements/com.apple.security.network.server.md)
  A Boolean value indicating whether your app may listen for incoming network connections.
- [com.apple.security.network.client](entitlements/com.apple.security.network.client.md)
  A Boolean value indicating whether your app may open outgoing network connections.
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
- [Address book entitlement](entitlements/com.apple.security.personal-information.addressbook.md)
  A Boolean value that indicates whether the app may have read-write access to contacts in the user’s address book.
- [Location entitlement](entitlements/com.apple.security.personal-information.location.md)
  A Boolean value that indicates whether the app may access location information from Location Services.
- [Calendars entitlement](entitlements/com.apple.security.personal-information.calendars.md)
  A Boolean value that indicates whether the app may have read-write access to the user’s calendar.
- [com.apple.security.files.user-selected.read-only](entitlements/com.apple.security.files.user-selected.read-only.md)
  A Boolean value that indicates whether the app may have read-only access to files the user has selected using an Open or Save dialog.
- [com.apple.security.files.user-selected.read-write](entitlements/com.apple.security.files.user-selected.read-write.md)
  A Boolean value that indicates whether the app may have read-write access to files the user has selected using an Open or Save dialog.
- [com.apple.security.files.downloads.read-only](entitlements/com.apple.security.files.downloads.read-only.md)
  A Boolean value that indicates whether the app may have read-only access to the Downloads folder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.cs.debugger)*