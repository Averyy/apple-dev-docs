# Disable Executable Memory Protection Entitlement

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether to disable all code signing protections while launching an app, and during its execution.

**Availability**:
- macOS 10.7+

#### Discussion

The system causes an app that attempts to directly modify sections of its own executable files on disk to forcefully exit. Use the [`Disable Executable Memory Protection Entitlement`](entitlements/com.apple.security.cs.disable-executable-page-protection.md) to enable this kind of unsafe software update. Even with this entitlement, however, updates that modify some files but not others may cause unexpected app state. Ensure that you perform updates atomically, with the final app bundle swapped out after app exit.

The entitlement effectively encompasses the behavior provided by the [`Allow Unsigned Executable Memory Entitlement`](entitlements/com.apple.security.cs.allow-unsigned-executable-memory.md), but not the [`Disable Library Validation Entitlement`](entitlements/com.apple.security.cs.disable-library-validation.md).

> ⚠️ **Warning**:  The [`Disable Executable Memory Protection Entitlement`](entitlements/com.apple.security.cs.disable-executable-page-protection.md) is an extreme entitlement that removes a fundamental security protection from your app, making it possible for an attacker to rewrite your app’s executable code without detection. Prefer narrower entitlements if possible.

 The [`Disable Executable Memory Protection Entitlement`](entitlements/com.apple.security.cs.disable-executable-page-protection.md) is an extreme entitlement that removes a fundamental security protection from your app, making it possible for an attacker to rewrite your app’s executable code without detection. Prefer narrower entitlements if possible.

To add this entitlement to your app, first enable the Hardened Runtime capability in Xcode, and then under Runtime Exceptions, select Disable Executable Memory Protection.

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

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.security.cs.disable-executable-page-protection)*